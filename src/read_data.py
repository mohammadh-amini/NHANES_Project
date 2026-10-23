import pandas as pd

# Load the three datasets
demo = pd.read_sas("data/DEMO_L.xpt", format="xport")
bmx  = pd.read_sas("data/BMX_L.xpt", format="xport")
bpxo = pd.read_sas("data/BPXO_L.xpt", format="xport")

# Check dimensions
print("DEMO_L:", demo.shape)
print("BMX_L :", bmx.shape)
print("BPXO_L:", bpxo.shape)

# Key columns
print("\n--- DEMO_L ---")
print(demo[['SEQN','RIAGENDR','RIDAGEYR','WTMEC2YR']].head())

print("\n--- BMX_L ---")
print(bmx[['SEQN','BMXBMI']].head())

print("\n--- BPXO_L ---")
print(bpxo.head())

# Merge datasets
merged = demo[['SEQN','RIAGENDR','RIDAGEYR','WTMEC2YR','SDMVPSU','SDMVSTRA']].merge(
    bmx[['SEQN','BMXBMI']], on='SEQN', how='inner'
).merge(
    bpxo[['SEQN','BPXOSY1','BPXOSY2','BPXOSY3']], on='SEQN', how='inner'
)

print("\n--- Merge Result ---")
print("Row count after merge:", merged.shape)
print(merged.head())
print("\nMissing data percentage:")
print(merged.isnull().sum() / len(merged) * 100)