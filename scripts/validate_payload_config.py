"""Check the current FPDU revision by default; explicit old inputs remain historical.

The schema uses the JSON Schema `const` keyword only, so validation needs no
third-party package. Its duplicate object is the machine-checkable contract,
not an independently editable payload specification.
"""
import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'config/payload/fpdu_2026-11-04.json'
SCHEMA = ROOT / 'config/payload/fpdu_2026-11-04.schema.json'


def validate(config):
    contract = json.loads(SCHEMA.read_text())['const']
    # JSON canonicalization distinguishes Boolean from integer values and fails NaN.
    if json.dumps(config, sort_keys=True, allow_nan=False) != json.dumps(contract, sort_keys=True):
        raise ValueError('Input differs from immutable FPDU-2026-11-04 contract; new revision required')
    return config


def material_volumes_mm3(config):
    """Scintillator only; no coating, grease, housing or inferred assembly bounds."""
    g = config['geometry']
    main = math.prod(g['main']['material_dimensions'])
    front = math.prod(g['front']['material_dimensions'])
    return {'main_each': main, 'main_total': main * g['main']['quantity'],
            'front_total': front * g['front']['quantity'],
            'total': main * g['main']['quantity'] + front * g['front']['quantity']}


def require_qualified_response(config, response_id):
    """Fail closed: this revision supplies no qualified response of any kind."""
    validate(config)
    if config['response']['qualified_response_id'] is None:
        raise ValueError('REQUIRES VALIDATION: no response is qualified for this geometry')
    if response_id != config['response']['qualified_response_id']:
        raise ValueError('Response/configuration mismatch')


if __name__ == '__main__':
    if __package__:
        from .fpdu_contracts import current_configuration
    else:
        from fpdu_contracts import current_configuration
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', nargs='?', type=Path,
                        help='Explicit revision; omit to validate current.json')
    args = parser.parse_args()
    current = current_configuration()
    c = current if args.config is None else json.loads(args.config.read_text())
    if c.get('configuration_id') == current['configuration_id']:
        if c != current:
            raise ValueError('Current revision differs from immutable schema')
        print(c['configuration_id'], 'current input contract PASS; detector response REQUIRES VALIDATION')
        print('Active scintillator volume [mm^3]:', c['geometry']['total_material_volume_mm3'])
    else:
        validate(c)
        print(c['configuration_id'], 'SUPERSEDED historical snapshot PASS; not current design')
        print('Scintillator material volumes [mm^3]:', material_volumes_mm3(c))
