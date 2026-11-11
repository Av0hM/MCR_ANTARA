"""Reader-facing assessments; underlying requirements and model results are unchanged."""
ASSESS = {
'eps': 'The corrected annual scenario sustains the modeled load schedule with positive recorded battery energy throughout. This supports operational energy feasibility for that scenario. Applying the result to the selected array and battery remains conditional on common load, degradation, reserve and cell-limit assumptions.',
'com': 'The eligible Relay capacity accommodates the sampled annual histogram workload at the modeled gross rate. Communications feasibility is conditional on the selected RF link delivering the required service and on the accepted outage envelope.',
'pld': 'The scintillator geometry, distributed SiPM readout and compact histogram interface define a coherent instrument concept. Incident-rate and acceptance calculations support sizing studies. Scientific feasibility remains conditional on energy-dependent detector response, mixed-species handling, effective acceptance and reconstruction uncertainty. Section 1 retains all tier criteria, including the MSC channel-count discrepancy requiring resolution.',
'adcs': 'The integrated scenario demonstrates a startup-to-operations sequence with time allocated to attitude transitions, science and Relay. Applicability to the intended reaction-wheel/magnetorquer system remains conditional on actuator authority, deployment conditions and pointing allocations. The incompatible Monte Carlo campaign cannot establish startup reliability.',
'obc': 'The calculated reference workload fits the candidate nominal science queue. Seven-day outage recovery requires persistent spill, which the candidate store accommodates before reserves. The separate 187498164-byte no-downlink grid sensitivity exceeds 128 MiB and is retained as a distinct retention case. Total execution and memory allocations remain to be established.',
'int': 'The common body frame gives a consistent geometric interface for payload, antenna and array. Integrated performance remains conditional on alignment, time/position accuracy and compatible electrical and command interfaces.',
 'thermal_structural': 'The thermal model predicts a finite temperature envelope for its evaluated heat schedule, providing a basis for component selection and thermal design. Component compliance and structural feasibility are not yet assessed against selected-part limits, a complete mass allocation and launch-provider loads.',
'gso': 'The annual scenario demonstrates repeated acquisition and Relay opportunities over a complete operations year. The resulting service schedule supports the sampled data workload. Mission-tier delivery remains conditional on detector response, independent-pass accounting and station availability.',
'sys': 'The evidence supports scenario-level operations and resource feasibility. Each study retains its own configuration; the integrated mission conclusion in Section 5 distinguishes demonstrated results, conditional applications and unassessed constraints.'}
# The scientific obligations remain verbatim in the Requirements Edition.
EVIDENCE = {
'ANT-EPS-FR-001':'Annual solar/load integrals: 50288.809/30866.103 Wh. Generation exceeds modeled demand; application to the selected EOL configuration is conditional.',
'ANT-EPS-FR-003':'Mode loads are represented; peak current and bus voltage/ripple allocations have not been assessed.',
'ANT-COM-FR-003':'Contact study identifies GS1_India; elevation-mask and RAAN inputs are unspecified.',
'ANT-COM-FR-005':'RF margin and net application throughput have not been calculated for the selected link.',
'ANT-PLD-FR-006':'20 ns shaping and coincidence timing are separate inputs; end-to-end latency and dead time are undetermined.',
'ANT-ADCS-FR-005':'Selected actuator/field coupling is undetermined; archived zero wheel momentum does not establish unloading capability.',
'ANT-OBC-FR-006':'The state-machine concept defines control and fault sequencing; command-integrity implementation is not assessed.',
'ANT-INT-FR-001':'Body-frame configuration and diagrams agree, providing a consistent geometric interface.',
'ANT-STR-FR-002':'Launch-provider load envelope and structural/modal analysis are not available.',
'ANT-STR-FR-003':'Deployment architecture is defined; mechanism loads, clearances and retention life are not assessed.',
'ANT-GSO-FR-001':'A complete annual operations timeline is available; accepted detector observations and tier pass counts are not yet assessed.',
'ANT-GSO-FR-002':'Reference record codec defines the ground interface; calibrated map reconstruction is not yet assessed.',
'ANT-SYS-FR-001':'Studies retain distinct epoch, mass and detector-response assumptions; no combined margin is inferred.'}
# Partial model evidence is conditional; absent performance evidence is unassessed.
CONDITIONAL=set()
def assessment(r):
 if r['id']=='ANT-INT-FR-001': return 'CONDITIONALLY SUPPORTED'
 if r['status']=='SUPPORTED': return 'SUPPORTED BY SIMULATION'
 if r['status']=='CONDITIONAL' or r['id'] in CONDITIONAL: return 'CONDITIONALLY SUPPORTED'
 if r['status']=='NOT MET': return 'NOT SUPPORTED BY CURRENT RESULTS'
 return 'NOT YET ASSESSED'
def evidence(r): return EVIDENCE.get(r['id'],r['evidence'])
