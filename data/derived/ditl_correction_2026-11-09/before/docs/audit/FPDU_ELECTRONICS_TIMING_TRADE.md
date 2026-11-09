# Electronics timing trade

The user clarified that 200/250/300 ns concern the **coincidence acceptance window**. These planning references are not processor deadlines or detector dead time. No numerical hardware margin has been demonstrated.

| Field in current configuration | ns | Status |
|---|---:|---|
| asic_shaping_time_ns | 20 | Confirmed planning parameter |
| coincidence_target_ns | 200 | Nominal window target |
| timing_allowance_min_ns | 250 | Minimum margin-inclusive window reference |
| preferred_timing_allowance_ns | 300 | Preferred window reference |
| post_shaping_delay_ns | 20 | Stated interval, meaning open |
| adc_conversion_latency_ns | null | Unknown |
| digital_processing_latency_ns | null | Unknown |
| qualified_detector_dead_time_ns | null | Unknown |
| max_trigger_rate_hz | null | Unknown, unit Hz |

Wider windows may increase accidental coincidences; they are not proof of timing robustness. Define edge timestamps, inclusive boundaries, jitter/skew allocation and what constitutes a coincidence before comparing implementations. Do not sum shaping, coincidence, post-shaping and pipeline delays without an actual dependency diagram.

| Candidate architecture | Potential role | Required evidence |
|---|---|---|
| Analog/ASIC coincidence + MCU | Fast discriminator logic independent of software; MCU handles digitized event records | Selected ASIC timing/thresholds, coincidence outputs, ADC handshaking, DMA/buffers and measured MCU workload |
| MCU timer/capture | Hardware timestamps with downstream processing | Capture clock, channel skew, multi-hit behavior, interrupt/DMA contention and overflow |
| FPGA | Coincidence and acquisition/processing logic | Device/I/O/clock resources, synthesis timing closure, asynchronous input handling and power |
| Hybrid FPGA/MCU | Fast front end with software reconstruction/control | Defined partition, transport queues, backpressure, power and failure behavior |

MCU is preferred conditionally; no candidate is selected. Eleven sensors do not determine the number of analog or ADC channels. Simultaneous versus multiplexed acquisition affects conversion service rate, inter-channel timing and event association.

`timing_trade()` accepts explicit scenario trigger rate, processing service time, ADC service interval, optional processing deadline/jitter/margin and event energy. It returns processor/ADC utilization λs, mean queue-stability prerequisite, separate deadline margin and dynamic power where inputs exist; unknowns remain null. The coincidence window is deliberately not an execution deadline input. `queue_trace()` evaluates a specified arrival trace and finite FCFS buffer (capacity includes service slot); losses are queue losses, not detector dead time. No Poisson/burst law or component performance is invented. Zero service-time tests have no artificial loss. Tests at 500,000 Hz and selected service times are synthetic numerical fixtures, not device claims.

Qualification needs timestamp/jitter distributions, pulse-pair resolution, ADC acquisition/conversion and sustained bandwidth, per-event worst-case processing, channel aggregation, livetime/loss counters, measured queue behavior at accepted mixed-field rates and bursts, baseline plus event-dependent power, thermal limits and margin criteria. Queue stability alone cannot provide event-loss probability. A shared nonparalyzable correction exists only as an explicit hypothesis test; unknown dead time raises an error, and separate-channel topology is not guessed.
