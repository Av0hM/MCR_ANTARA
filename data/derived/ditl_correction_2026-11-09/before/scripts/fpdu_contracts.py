"""Explicit FPDU accounting interfaces, not a qualified detector response.

Rates supplied to these functions must already have the stated physical meaning.
No legacy response, acceptance, dead time or electronics performance is inferred.
"""
from bisect import bisect_right
from collections import deque
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def current_configuration():
    directory = ROOT / 'config/payload'
    pointer = json.loads((directory / 'current.json').read_text())
    config = json.loads((directory / pointer['configuration_file']).read_text())
    schema = json.loads((directory / pointer['schema_file']).read_text())
    if config != schema['const']:
        raise ValueError('Immutable payload revision differs from its schema')
    return config


def nonnegative(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError('Expected finite nonnegative number')
    return value


def edges_checked(edges):
    if len(edges) < 2 or any(not math.isfinite(x) for x in edges) or any(b <= a for a, b in zip(edges, edges[1:])):
        raise ValueError('Finite strictly increasing edges required')
    return edges


def differential_counts(edges_mev, bin_average_intensity, geometric_factor_cm2_sr, efficiency, exposure_sec):
    """Directional intensity [cm^-2 sr^-1 s^-1 MeV^-1] -> counts.

    Requires bin averages, not spectral samples masquerading as bin integrals.
    G already integrates angle. This is idealized accounting, not acceptance.
    """
    edges_checked(edges_mev)
    if len(bin_average_intensity) != len(edges_mev) - 1:
        raise ValueError('Missing energy channels')
    scale = nonnegative(geometric_factor_cm2_sr) * nonnegative(efficiency) * nonnegative(exposure_sec)
    if efficiency > 1:
        raise ValueError('Efficiency exceeds unity')
    result = [nonnegative(f) * (b-a) * scale for a,b,f in zip(edges_mev, edges_mev[1:], bin_average_intensity)]
    for value in result:
        nonnegative(value)
    return result


def shared_nonparalyzable_rates(science_rates_hz, total_trigger_rate_hz, dead_time_ns):
    """Hypothesis-only shared-chain correction; unknown dead time is an error."""
    if dead_time_ns is None or total_trigger_rate_hz is None:
        raise ValueError('Qualified trigger and dead-time inputs required')
    total = nonnegative(total_trigger_rate_hz)
    rates = [nonnegative(x) for x in science_rates_hz]
    if sum(rates) > total + 1e-12:
        raise ValueError('Science subset exceeds total triggers')
    live = 1 / (1 + total * nonnegative(dead_time_ns) * 1e-9)
    return [r * live for r in rates], live


def histogram_reconstructed(energies_mev, edges_mev):
    """Input is reconstructed energy, never an implicit truth-energy adapter."""
    edges_checked(edges_mev)
    bins = [0] * (len(edges_mev)-1)
    result = dict(histogram=bins, underflow=0, overflow=0, invalid=0)
    for energy in energies_mev:
        if not math.isfinite(energy):
            result['invalid'] += 1
        elif energy < edges_mev[0]:
            result['underflow'] += 1
        elif energy > edges_mev[-1]:
            result['overflow'] += 1
        else:
            bins[min(bisect_right(edges_mev, energy)-1, len(bins)-1)] += 1
    return result


def merge_histogram(counts, edges_mev, boundaries):
    edges_checked(edges_mev)
    if len(counts)+1 != len(edges_mev) or boundaries[0] != 0 or boundaries[-1] != len(counts) or any(type(i) is not int for i in boundaries) or any(b<=a for a,b in zip(boundaries,boundaries[1:])):
        raise ValueError('Groups must partition all channels')
    for count in counts:
        nonnegative(count)
    return {'counts': [sum(counts[a:b]) for a,b in zip(boundaries,boundaries[1:])],
            'edges_mev': [edges_mev[i] for i in boundaries],
            'widths_mev': [edges_mev[b]-edges_mev[a] for a,b in zip(boundaries,boundaries[1:])]}


def net_precision(observed_counts, background_counts, background_variance, systematic_fraction):
    """Gaussian relative-uncertainty diagnostic, not low-count confidence interval.

    Background variance and systematic floor must be explicitly supplied.
    Zero/nonpositive net signal is not assigned artificial precision.
    """
    observed, background, variance, systematic = map(nonnegative, (observed_counts, background_counts, background_variance, systematic_fraction))
    signal = observed-background
    return None if signal <= 0 else math.sqrt(observed + variance + (systematic*signal)**2)/signal


def cell_index(latitude, longitude, resolution):
    if not math.isfinite(latitude) or not -90 <= latitude < 90 or not math.isfinite(longitude) or resolution <= 0 or not math.isfinite(resolution):
        raise ValueError('Invalid geographic coordinate/resolution')
    lon = (longitude+180) % 360 - 180
    return (math.floor((latitude+90)/resolution), math.floor((lon+180)/resolution))


class VisitAccounting:
    """Continuous interval visits and unique regional passages, NOT independence."""
    def __init__(self):
        self.end = None
        self.previous_cell = None
        self.passage = 0
        self.cells = {}

    def add(self, start, duration, cell, science_enabled=False):
        nonnegative(start)
        if nonnegative(duration) == 0:
            raise ValueError('Use positive exposure intervals')
        if self.end is not None and not math.isclose(start, self.end, rel_tol=0, abs_tol=1e-9):
            raise ValueError('Missing, overlapping or out-of-order interval')
        if cell is not None:
            if self.previous_cell is None:
                self.passage += 1
            data = self.cells.setdefault(cell, dict(visits=0, passages=set(), geometric_sec=0., science_sec=0.))
            data['visits'] += int(cell != self.previous_cell)
            data['passages'].add(self.passage)
            data['geometric_sec'] += duration
            data['science_sec'] += duration if science_enabled else 0
        elif science_enabled:
            raise ValueError('Region science exposure without a cell')
        self.end = start+duration
        self.previous_cell = cell


def checkpoint_identity(configuration):
    """Caller must include epoch, grid, dt, response, input hashes and state shapes."""
    required = {'epoch', 'grid', 'step_sec', 'response_id', 'input_hashes', 'state_shapes'}
    if not required <= configuration.keys():
        raise ValueError('Incomplete checkpoint identity')
    return hashlib.sha256(json.dumps(configuration, sort_keys=True, allow_nan=False, separators=(',', ':')).encode()).hexdigest()


def validate_checkpoint(saved_identity, configuration, state_shapes):
    if saved_identity != checkpoint_identity(configuration) or state_shapes != configuration['state_shapes']:
        raise ValueError('Checkpoint configuration/data/shape mismatch')


def validate_complete_intervals(rows, horizon_sec):
    """Science format: contiguous intervals plus a zero-duration terminal row."""
    nonnegative(horizon_sec)
    if not rows or tuple(rows[-1]) != (horizon_sec, 0):
        raise ValueError('Missing terminal observation or incomplete horizon')
    end = 0.
    for start, duration in rows[:-1]:
        if nonnegative(duration) == 0 or not math.isclose(start,end,rel_tol=0,abs_tol=1e-9):
            raise ValueError('Invalid or missing interval')
        end = start+duration
    if not math.isclose(end,horizon_sec,rel_tol=0,abs_tol=1e-9):
        raise ValueError('Exposure does not close at horizon')
    return end


def battery_exchange(stored_wh, capacity_wh, requested_delta_wh):
    """Energy at battery boundary after upstream efficiencies; no aging model."""
    nonnegative(capacity_wh)
    if not 0 <= stored_wh <= capacity_wh or not math.isfinite(requested_delta_wh):
        raise ValueError('Invalid battery state')
    accepted = max(-stored_wh, min(requested_delta_wh, capacity_wh-stored_wh))
    return dict(stored_wh=stored_wh+accepted, throughput_wh=abs(accepted),
                curtailed_wh=max(0.,requested_delta_wh-accepted), unserved_wh=max(0.,accepted-requested_delta_wh))


def run_soc_summary(runs):
    """runs: {(RAAN, run_id): sequence of valid SOC samples}."""
    if not runs or any(not values for values in runs.values()):
        raise ValueError('Missing runs/samples')
    groups = {}
    for (raan, run_id), values in runs.items():
        if any(not math.isfinite(v) or not 0 <= v <= 1 for v in values):
            raise ValueError('Invalid SOC')
        groups.setdefault(raan, {})[run_id] = min(values)
    return {raan: dict(run_minima=mins, worst_min_soc=min(mins.values()), mean_run_min_soc=sum(mins.values())/len(mins)) for raan,mins in groups.items()}


def timing_trade(trigger_rate_hz, service_time_ns=None, adc_service_interval_ns=None, deadline_ns=None, jitter_ns=None, margin_ns=0, energy_per_event_j=None):
    """Scenario arithmetic only; no device or physical arrival model is assumed."""
    rate = nonnegative(trigger_rate_hz)
    for value in (service_time_ns,adc_service_interval_ns,deadline_ns,jitter_ns,energy_per_event_j):
        if value is not None:
            nonnegative(value)
    nonnegative(margin_ns)
    occupancy = None if service_time_ns is None else rate*service_time_ns*1e-9
    adc_occupancy = None if adc_service_interval_ns is None else rate*adc_service_interval_ns*1e-9
    deadline_margin = None if None in (service_time_ns,deadline_ns,jitter_ns) else deadline_ns-service_time_ns-jitter_ns-margin_ns
    for value in (occupancy, adc_occupancy):
        if value is not None:
            nonnegative(value)
    return dict(processor_utilization=occupancy, adc_utilization=adc_occupancy,
                queue_stable_mean=None if occupancy is None else occupancy < 1,
                adc_capacity_sufficient=None if adc_occupancy is None else adc_occupancy < 1,
                deadline_margin_ns=deadline_margin,
                dynamic_power_w=None if energy_per_event_j is None else rate*energy_per_event_j,
                qualification='NOT QUALIFIED: burst, timing, power and hardware evidence required')


def queue_trace(arrivals_ns, service_time_ns, capacity_events):
    """Deterministic one-server trace; capacity includes event in service.

    Simultaneous completions free space before arrivals. No detector dead time.
    """
    service = nonnegative(service_time_ns)
    if type(capacity_events) is not int or capacity_events < 1:
        raise ValueError('Positive integer capacity required')
    pending = deque()
    previous = -1.
    lost = accepted = peak = 0
    max_residence = 0.
    for arrival in arrivals_ns:
        nonnegative(arrival)
        if arrival < previous:
            raise ValueError('Arrival timestamps out of order')
        previous = arrival
        while pending and pending[0] <= arrival:
            pending.popleft()
        if len(pending) == capacity_events:
            lost += 1
            continue
        finish = max(arrival, pending[-1] if pending else arrival) + service
        nonnegative(finish)
        pending.append(finish)
        accepted += 1
        peak = max(peak,len(pending))
        max_residence = max(max_residence,finish-arrival)
    return dict(accepted=accepted,lost=lost,peak_occupancy=peak,max_residence_ns=max_residence)


def clipped_area(polygon, xmin, xmax, ymin, ymax):
    """Degree-plane polygon/rectangle clipping; positive area excludes touches."""
    points = [tuple(p) for p in polygon]
    for axis, bound, sign in ((0,xmin,1),(0,xmax,-1),(1,ymin,1),(1,ymax,-1)):
        output = []
        if not points:
            return 0.
        for a,b in zip(points[-1:]+points[:-1], points):
            inside_a = sign*(a[axis]-bound) >= 0
            inside_b = sign*(b[axis]-bound) >= 0
            if inside_a != inside_b:
                ratio = (bound-a[axis])/(b[axis]-a[axis])
                output.append(tuple(a[i]+ratio*(b[i]-a[i]) for i in range(2)))
            if inside_b:
                output.append(b)
        points = output
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(points,points[1:]+points[:1])))/2


def polygon_cells(polygon, resolution):
    if not math.isfinite(resolution) or resolution <= 0 or 180/resolution != int(180/resolution):
        raise ValueError('Resolution must divide 180 degrees')
    if polygon[0] != polygon[-1] or any(not -180 <= x < 180 or not -90 <= y <= 90 for x,y in polygon):
        raise ValueError('Closed unwrapped lon/lat polygon required')
    # This contract is for the supplied simple SAA polygon, not dateline polygons.
    xmin,xmax = min(p[0] for p in polygon),max(p[0] for p in polygon)
    ymin,ymax = min(p[1] for p in polygon),max(p[1] for p in polygon)
    return {(round(-90+(i+.5)*resolution,9), round(-180+(j+.5)*resolution,9))
            for i in range(math.floor((ymin+90)/resolution),math.ceil((ymax+90)/resolution))
            for j in range(math.floor((xmin+180)/resolution),math.ceil((xmax+180)/resolution))
            if clipped_area(polygon,-180+j*resolution,-180+(j+1)*resolution,-90+i*resolution,-90+(i+1)*resolution)>1e-10}


def require_qualified_response(response_id):
    # No qualified response for the approved geometry is currently registered.
    raise ValueError(f'No qualified current-geometry response: {response_id!r}')


def validate_science_record(record):
    """Validate the logical schema and extra cross-field accounting constraints."""
    from datetime import datetime
    schema = json.loads((ROOT/'config/science/fpdu_histogram_v1.schema.json').read_text())
    def check(value, spec):
        if 'const' in spec and value != spec['const']:
            raise ValueError('Wrong schema/configuration/edges identity')
        if 'enum' in spec and value not in spec['enum']:
            raise ValueError('Invalid enum')
        kinds = spec.get('type',[])
        kinds = [kinds] if isinstance(kinds,str) else kinds
        types = {'object':lambda x:isinstance(x,dict), 'array':lambda x:isinstance(x,list),
                 'string':lambda x:isinstance(x,str), 'null':lambda x:x is None,
                 'integer':lambda x:type(x) is int, 'number':lambda x:type(x) in (int,float) and math.isfinite(x)}
        if kinds and not any(types[k](value) for k in kinds):
            raise ValueError('Invalid field type')
        if value is None:
            return
        if isinstance(value,dict):
            if not set(spec.get('required',[])) <= value.keys():
                raise ValueError('Missing required fields')
            properties = spec.get('properties',{})
            if spec.get('additionalProperties') is False and set(value)-properties.keys():
                raise ValueError('Unknown fields')
            for key,child in value.items():
                if key in properties: check(child,properties[key])
        if isinstance(value,list):
            if not spec.get('minItems',0) <= len(value) <= spec.get('maxItems',math.inf):
                raise ValueError('Wrong array length')
            for child in value: check(child,spec.get('items',{}))
        if type(value) in (int,float):
            if not math.isfinite(value) or value < spec.get('minimum',-math.inf) or value > spec.get('maximum',math.inf) or value >= spec.get('exclusiveMaximum',math.inf):
                raise ValueError('Out-of-range value')
    check(record,schema)
    timestamp = record['timestamp_utc']
    if not timestamp.endswith('Z'):
        raise ValueError('UTC timestamp must end in Z')
    datetime.fromisoformat(timestamp[:-1]+'+00:00')
    if record['histogram_kind']=='observed_counts' and any(type(x) is not int for x in record['histogram']):
        raise ValueError('Observed counts must be integers')
    metadata=record['metadata']
    live,elapsed = metadata.get('livetime_sec'),metadata.get('interval_duration_sec')
    if live is not None and elapsed is not None and live>elapsed:
        raise ValueError('Livetime exceeds acquisition duration')
    # Accepted/rejected/lost counting points must first be defined by the ICD;
    # no unjustified sum-to-trigger relationship is imposed by this validator.
    return record
