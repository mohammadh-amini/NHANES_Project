import pandas as pd

# Load Datasets
demo = pd.read_sas("../data/DEMO_L.xpt", format="xport")
dr1tot = pd.read_sas("../data/DR1TOT_L.xpt", format="xport")
ohq = pd.read_sas("../data/OHQ_L.xpt", format="xport")
smq = pd.read_sas("../data/SMQ_L.xpt", format="xport")

# Merge
demo_cols = ['SEQN', 'RIAGENDR', 'RIDAGEYR', 'WTMEC2YR']
dr1tot_cols = ['SEQN', 'DR1TSUGR']
ohq_cols = ['SEQN', 'OHQ660']
smq_cols = ['SEQN', 'SMQ020']

merged1 = demo[demo_cols].merge(dr1tot[dr1tot_cols], on='SEQN', how='inner')
merged2 = merged1.merge(ohq[ohq_cols], on='SEQN', how='inner')
merged3 = merged2.merge(smq[smq_cols], on='SEQN', how='inner')

merged3 = merged3.replace({7: pd.NA, 9: pd.NA})
merged3['OHQ660'] = merged3['OHQ660'].replace({1.0: 1, 2.0: 1, 3.0: 1, 4.0: 1, 5.0: 0})
merged3 = merged3.dropna(subset=['DR1TSUGR', 'OHQ660', 'SMQ020'])
df = merged3[merged3['RIDAGEYR'] >= 18].copy()
df['RIAGENDR'] = df['RIAGENDR'].replace({1.0: 'Male', 2.0: 'Female'})

# Data Flow Table
data_flow = pd.DataFrame({
    'Processing Step': ['Raw DEMO', 'After DEMO + Diet Merge', 'After Oral Health Merge', 'After Smoking Merge', 'Final Analytical Sample (Age 18+)'],
    'Count': [len(demo), len(merged1), len(merged2), len(merged3), len(df)]
})
print(data_flow)
data_flow.to_csv("../reports/phase1/data_flow.csv", index=False, encoding='utf-8-sig')

# Save Clean Data
df.to_csv("../data/clean_data.csv", index=False, encoding='utf-8-sig')
print(f"\nFinal sample size: {len(df)}")
print("Clean data saved to data/clean_data.csv")