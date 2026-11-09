# Current science data interface

`science_record_v3.json` defines the current MCR compact encoding; its companion schema and `scripts/science_record_v3.py` validate codec inputs. The original `fpdu_histogram_v1.schema.json` remains the historical logical/analysis interface and preserves the same provisional bin edges. It is not the current binary record format.

No numerical minimum duration is imposed. Valid zero-count exposures are preserved. Hardware timing boundaries and exact geographic crossings must be verified before flight scheduler adoption. Metadata for calibration, response, livetime/background and quality remains separately linked and must be budgeted. The 292 bytes exclude radio framing and external metadata.

No production simulator is modified by these reference interfaces.
