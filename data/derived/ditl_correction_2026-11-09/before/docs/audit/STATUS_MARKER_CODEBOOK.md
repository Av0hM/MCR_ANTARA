# Combined mode and health marker

New v3 numeric assignments map actual FSM state names inspected at `src/simulations/ditl/ANTARA_Science_Sim.py:1347–1385`. They are serialization codes, not evidence that the simulator previously exported these integers.

| Bits | Meaning |
|---|---|
| 0–3 | Mode: 0 Cold and Dark; 1 Detumble; 2 Sun Pointing; 3 Detection; 4 Relay; 5 Slewing; 6 Safe; 7–14 reserved; 15 Unknown |
| 4–5 | OBC health |
| 6–7 | EPS health |
| 8–9 | ADCS health |
| 10–11 | COMMS health |
| 12–13 | Payload health |
| 14–15 | Other/thermal health |

Every health pair: 00 nominal, 01 degraded, 10 fault, 11 unknown. Unknown is not nominal. Health is the worst observed explicit state over the interval; if any subsystem's monitoring validity is unknown, encode unknown and retain details separately. Exact fault-to-summary mapping remains FSW/PDR work. Split on operating-mode changes. Reserved mode codes are rejected by the reference decoder. CRC covers the marker. Detailed diagnostics are separate, not appended to every science record.

