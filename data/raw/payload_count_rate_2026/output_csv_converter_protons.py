import pandas as pd

input_filename = "radiation_outputs_protons_final_pctile_flux_99.txt"
output_filename = "radiation_outputs_protons_final_pctile_flux_99.csv"

# Extract energy levels from comments
energy_levels = []
with open(input_filename, "r") as f:
    for line in f:
        if "Energy levels (MeV):" in line:
            energy_levels = line.split(":")[1].strip().split()
            break

# Define explicit column names
base_cols = ["datetime_mjd", "alt_km", "lat_deg", "lon_deg"]
flux_cols = [f"flux_{e}MeV" for e in energy_levels]
columns = base_cols + flux_cols if energy_levels else None

# Read and save CSV
df = pd.read_csv(
    input_filename, comment="#", header=None, names=columns, delimiter=","
)
df.to_csv(output_filename, index=False)