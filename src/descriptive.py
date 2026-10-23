import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
demo = pd.read_sas("data/DEMO_L.xpt", format="xport")
bmx = pd.read_sas("data/BMX_L.xpt", format="xport")
bpxo = pd.read_sas("data/BPXO_L.xpt", format="xport")

# --- Merge & Clean ---
merged = demo[['SEQN', 'RIAGENDR', 'RIDAGEYR', 'WTMEC2YR']].merge(
    bmx[['SEQN', 'BMXBMI']], on='SEQN', how='inner'
).merge(
    bpxo[['SEQN', 'BPXOSY1', 'BPXOSY2', 'BPXOSY3']], on='SEQN', how='inner'
)
merged['SBP_mean'] = merged[['BPXOSY1', 'BPXOSY2', 'BPXOSY3']].mean(axis=1)

# Filter Adults & Drop NaNs
df = merged.dropna(subset=['BMXBMI', 'SBP_mean'])
df = df[df['RIDAGEYR'] >= 18].copy()

# --- Descriptive Stats ---
print(df[['BMXBMI', 'SBP_mean', 'RIDAGEYR']].describe().round(2))
print(f"IQR BMI: {df['BMXBMI'].quantile(.75) - df['BMXBMI'].quantile(.25):.2f}")

# --- Raw vs Weighted ---
raw_bmi = df['BMXBMI'].mean()
weighted_bmi = (df['BMXBMI'] * df['WTMEC2YR']).sum() / df['WTMEC2YR'].sum()
print(f"BMI Raw: {raw_bmi:.2f} | Weighted: {weighted_bmi:.2f}")

# --- Save CSVs ---
df.to_csv("data/clean_data.csv", index=False, encoding='utf-8-sig')

# --- Plots ---
sns.set_theme(style="whitegrid")

# 1. BMI Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['BMXBMI'], kde=True, color='royalblue')
plt.title('BMI Distribution')
plt.savefig('figures/hist_bmi.png', dpi=300)
plt.close()

# 2. SBP Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['SBP_mean'], kde=True, color='darkorange')
plt.title('SBP Distribution')
plt.savefig('figures/hist_sbp.png', dpi=300)
plt.close()

# 3. Gender Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x='RIAGENDR', y='SBP_mean', data=df, hue='RIAGENDR', palette='Set2', legend=False)
plt.xticks([0, 1], ['Male', 'Female'])
plt.title('SBP by Gender')
plt.savefig('figures/box_gender.png', dpi=300)
plt.close()

# 4. Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='BMXBMI', y='SBP_mean', data=df, alpha=0.3, color='teal')
plt.title('BMI vs SBP')
plt.savefig('figures/scatter_bmi_sbp.png', dpi=300)
plt.close()

print("✅ Data and plots saved successfully.")