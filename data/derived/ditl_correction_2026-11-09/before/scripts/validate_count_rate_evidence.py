"""Independent, bounded audit of supplied IRENE count-rate evidence.

Read-only inputs; standard library only. Reproduces supplied idealized arithmetic,
not shielding, detector response or actual electronics triggers. Rejects invalid
units, extrapolation, duplicate cells and unequal cell sets. No raw script imports.
"""
import argparse
import bisect
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import statistics
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw/payload_count_rate_2026'
KEYS = ['datetime_mjd', 'alt_km', 'lat_deg', 'lon_deg']
RATES = ['proton_rate', 'electron_rate', 'total_rate', 'proton_rate_per_sr',
         'electron_rate_per_sr', 'total_rate_per_sr']


def finite_nonnegative(value):
    if not math.isfinite(value) or value < 0:
        raise ValueError('Expected finite nonnegative flux/rate')


def validate_spectrum(energies, flux):
    if not energies or len(energies) != len(flux):
        raise ValueError('Missing or inconsistent energy columns')
    if any(not math.isfinite(e) or e <= 0 for e in energies):
        raise ValueError('Energies must be finite and positive')
    if any(b <= a for a, b in zip(energies, energies[1:])):
        raise ValueError('Duplicate or unordered energy thresholds')
    for f in flux:
        finite_nonnegative(f)
    if any(b > a for a, b in zip(flux, flux[1:])):
        raise ValueError('Integral spectrum increases with threshold')


def interpolate_integral(energies, flux, threshold):
    validate_spectrum(energies, flux)
    if not math.isfinite(threshold) or not energies[0] <= threshold <= energies[-1]:
        raise ValueError('Threshold outside supplied energy grid; extrapolation forbidden')
    j = bisect.bisect_left(energies, threshold)
    if energies[j] == threshold:
        return flux[j]
    t = (math.log(threshold) - math.log(energies[j-1])) / (math.log(energies[j]) - math.log(energies[j-1]))
    a, b = flux[j-1:j+1]
    result = math.exp((1-t)*math.log(a) + t*math.log(b)) if a > 0 and b > 0 else (1-t)*a+t*b
    finite_nonnegative(result)
    return result


def isotropic_rate(flux, geometric_factor=1., flux_unit='#/cm^2/s', factor_unit='cm^2 sr'):
    if flux_unit != '#/cm^2/s' or factor_unit != 'cm^2 sr':
        raise ValueError('Expected integral omnidirectional flux and geometric factor, not area')
    finite_nonnegative(flux)
    finite_nonnegative(geometric_factor)
    result = flux / (4 * math.pi) * geometric_factor
    finite_nonnegative(result)
    return result


def index_rows(rows, expected_keys=None):
    indexed = {}
    for row in rows:
        key = tuple(row[k] for k in KEYS)
        if not all(math.isfinite(x) for x in key):
            raise ValueError('Nonfinite cell coordinate')
        if not -90 <= key[2] <= 90 or not -180 <= key[3] < 180 or key[1] < 0:
            raise ValueError('Invalid GDZ coordinate')
        if key in indexed:
            raise ValueError('Duplicate cell coordinate')
        indexed[key] = row
    if not indexed:
        raise ValueError('Empty cell table')
    if expected_keys is not None and set(indexed) != set(expected_keys):
        raise ValueError('Missing or extra geographic cells')
    return indexed


def align_rows(protons, electrons, expected_keys):
    p = index_rows(protons, expected_keys)
    e = index_rows(electrons, expected_keys)
    return [(p[k], e[k]) for k in p]


def read_csv(path):
    with path.open(newline='') as f:
        reader = csv.DictReader(f)
        names = reader.fieldnames
        if not names or len(names) != len(set(names)) or not set(KEYS) <= set(names):
            raise ValueError('Missing or duplicate column names')
        rows = [{k: float(v) for k, v in row.items()} for row in reader]
    index_rows(rows)
    if any(not math.isfinite(v) for row in rows for v in row.values()):
        raise ValueError('Nonfinite CSV data')
    return names, rows


def read_irene(path, model):
    lines = path.read_text().splitlines()
    header = '\n'.join(l for l in lines if l.startswith('#'))
    for pattern in (rf'Model type:\s+{model}\b', r'Flux type:\s+Integral\b',
                    r'Flux direction:\s+Omnidirectional\b', r'Coordinate system:\s+GDZ \(WGS84 Geodetic\) in km',
                    r'Time format:\s+Modified Julian Date', r'flux\(#/cm\^2/s\)'):
        if not re.search(pattern, header):
            raise ValueError('Unsupported IRENE metadata/units: ' + pattern)
    match = re.search(r'Energy levels \(MeV\):\s*([^\n]+)', header)
    labels = match[1].split()
    energies = [float(e) for e in labels]
    names = KEYS + ['flux_'+e+'MeV' for e in labels]
    rows = []
    for fields in csv.reader(l for l in lines if l and not l.startswith('#')):
        if len(fields) != len(names):
            raise ValueError('Malformed IRENE row length')
        values = list(map(float, fields))
        validate_spectrum(energies, values[4:])
        rows.append(dict(zip(names, values)))
    index_rows(rows)
    return names, energies, rows, header


def compare_numeric(actual, expected, columns, rounded=False):
    a = index_rows(actual)
    b = index_rows(expected, a)
    errors = {c: 0. for c in columns}
    for key in a:
        for c in columns:
            x, y = a[key][c], b[key][c]
            # Archived count-rate CSV uses %.6g; compare against its actual precision.
            target = float(format(y, '.6g')) if rounded else y
            if x != target:
                raise ValueError(f'Numeric mismatch at {key}, {c}: {x} != {target}')
            errors[c] = max(errors[c], abs(x-y))
    return errors


def ods_check(path, expected):
    ns = {'t':'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
          'o':'urn:oasis:names:tc:opendocument:xmlns:office:1.0'}
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('content.xml'))
    tables = root.findall('.//t:table', ns)
    if len(tables) != 1:
        raise ValueError('Unexpected ODS sheet count')
    records = []
    formula_count = 0
    summary_cells = []
    for row_number, row in enumerate(tables[0].findall('t:table-row', ns), 1):
        values = []
        for cell in row:
            formula_count += ('{'+ns['t']+'}formula') in cell.attrib
            if ('{'+ns['t']+'}formula') in cell.attrib:
                summary_cells.append({'row': row_number, 'column': len(values)+1, 'formula':cell.get('{'+ns['t']+'}formula'), 'cached_value':cell.get('{'+ns['o']+'}value')})
            value = cell.get('{'+ns['o']+'}value')
            text = ''.join(cell.itertext())
            repeat = int(cell.get('{'+ns['t']+'}number-columns-repeated', '1'))
            if value is None and not text.strip():
                # Blank tail is not data; ignore after known column extent.
                if len(values) >= 20:
                    break
            values.extend([float(value) if value is not None else text] * min(repeat, 20-len(values)))
        if not any(str(v).strip() for v in values):
            continue
        if int(row.get('{'+ns['t']+'}number-rows-repeated', '1')) != 1:
            raise ValueError('Unexpected repeated nonempty ODS row')
        if all(v == '' for v in values[:4]):
            if not summary_cells or summary_cells[-1]['row'] != row_number:
                raise ValueError('Unrecognized non-data ODS row')
            continue
        records.append(values)
    names = records[0]
    rows = [dict(zip(names, map(float, row))) for row in records[1:]]
    compare_numeric(rows, expected, names)
    return {'sheets': 1, 'data_rows': len(rows), 'formulas': formula_count, 'summary_cells': summary_cells, 'numeric_csv_match': True}


def audit(raw, output):
    files = sorted(f for f in raw.rglob('*') if f.is_file())
    if len(files) != 22:
        raise ValueError(f'Expected 22 original files, found {len(files)}')
    byname = {f.name: f for f in files}
    if len(byname) != len(files):
        raise ValueError('Duplicate source basenames')
    before = {str(f.relative_to(raw)): hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
    inventory = [{'path': str(f.relative_to(raw)), 'bytes': f.stat().st_size, 'sha256': before[str(f.relative_to(raw))]} for f in files]
    report = {'inventory': inventory, 'cases': {}}
    all_keys = None
    all_order = None
    products = {}
    for case, suffix in [('mean','mean_flux'), ('peak99','pctile_flux_99')]:
        loaded = []
        conversions = {}
        for species, model in [('protons','AP9'), ('electrons','AE9')]:
            stem = f'radiation_outputs_{species}_final_{suffix}'
            names, energies, rows, header = read_irene(byname[stem+'.txt'], model)
            csv_names, csv_rows = read_csv(byname[stem+'.csv'])
            if csv_names != names:
                raise ValueError('CSV energy header differs from raw IRENE header')
            compare_numeric(csv_rows, rows, names)
            keys = list(index_rows(rows))
            if len(keys) != 7940:
                raise ValueError('Expected 7940 cells in this evidence revision')
            if all_keys is None:
                all_keys, all_order = set(keys), keys
            index_rows(rows, all_keys)
            if keys != all_order:
                raise ValueError('Source cell ordering differs (audit can key-align but reports this change)')
            conversions[species] = {'rows': len(rows), 'energy_thresholds_mev': energies,
                                    'raw_to_csv_exact_numeric_match': True}
            loaded.append((names[4:], energies, rows))
        pcols, pe, prows = loaded[0]
        ecols, ee, erows = loaded[1]
        rates = []
        for p, e in align_rows(prows, erows, all_keys):
            pr = interpolate_integral(pe, [p[c] for c in pcols], 5.5)
            el = interpolate_integral(ee, [e[c] for c in ecols], .35)
            row = {k: p[k] for k in KEYS}
            row.update(proton_rate=pr, electron_rate=el, total_rate=pr+el)
            for c in ('proton','electron','total'):
                row[c+'_rate_per_sr'] = isotropic_rate(row[c+'_rate'])
            rates.append(row)
        names, archived = read_csv(byname[f'count_rate_per_cell_{case}.csv'])
        errors = compare_numeric(archived, rates, RATES, rounded=True)
        if list(index_rows(archived)) != all_order:
            raise ValueError('Archived rate order differs')
        stats = {}
        weights = [math.cos(math.radians(r['lat_deg'])) for r in rates]
        for col in RATES:
            peak = max(rates, key=lambda r: r[col])
            stats[col] = {'min': min(r[col] for r in rates), 'max': peak[col],
                          'mean': statistics.fmean(r[col] for r in rates),
                          'cos_lat_weighted_mean': math.fsum(r[col]*w for r,w in zip(rates,weights))/math.fsum(weights),
                          'max_cell': {k:peak[k] for k in KEYS}, 'max_csv_rounding_error': errors[col]}
        report['cases'][case] = {'conversions': conversions, 'statistics': stats,
                                  'all_47640_rate_values_match_six_significant_digits': True}
        products[case] = rates
        if case == 'mean':
            report['ods'] = ods_check(byname['radiation_outputs_protons_final_mean_flux.ods'], prows)
    report['grid'] = {'rows': len(all_keys), 'all_six_csv_tables_same_keys_and_order': True,
                      'duplicates': 0, 'relative_missing_cells': 0,
                      'bounds': {k:[min(x[i] for x in all_keys),max(x[i] for x in all_keys)] for i,k in enumerate(KEYS)},
                      'cell_keys_sha256': hashlib.sha256(json.dumps(sorted(all_keys)).encode()).hexdigest()}
    # Equal sets cannot prove completeness against an absent original domain/ephemeris.
    report['grid']['absolute_domain_completeness'] = 'Unestablished: original grid_ephemeris.txt/domain mask absent'
    report['raw_files_unchanged'] = all(hashlib.sha256(f.read_bytes()).hexdigest()==before[str(f.relative_to(raw))] for f in files)
    if not report['raw_files_unchanged']:
        raise ValueError('Raw input changed during validation')
    if output == raw or raw in output.parents:
        raise ValueError('Output must be outside raw evidence')
    output.mkdir(parents=True, exist_ok=True)
    for case, rates in products.items():
        with (output/f'reproduced_count_rate_per_cell_{case}.csv').open('w', newline='') as f:
            writer = csv.writer(f); writer.writerow(KEYS+RATES)
            writer.writerows([[format(r[c],'.6g') for c in KEYS+RATES] for r in rates])
    (output/'validation_summary.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('PASS: 22 files; 7940 aligned unique cells; four exact flux conversions; two reproduced rate tables; ODS match')
    return report


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--raw',type=Path,default=RAW)
    ap.add_argument('--output',type=Path,default=ROOT/'data/derived/payload_count_rate_2026_audit')
    args=ap.parse_args()
    audit(args.raw.resolve(),args.output.resolve())
