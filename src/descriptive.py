import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Load Clean Data
df = pd.read_csv("../data/clean_data.csv")

# Map SMQ020 to labels
df['Smoking_Label'] = df['SMQ020'].map({1.0: 'Smoker', 2.0: 'Non-Smoker'})

sns.set_theme(style="whitegrid")

# 1. Histogram of Sugar Intake
plt.figure(figsize=(8, 5))
sns.histplot(df['DR1TSUGR'], kde=True, color='royalblue', bins=50)
plt.axvline(df['DR1TSUGR'].mean(), color='red', linestyle='--', label=f"Mean: {df['DR1TSUGR'].mean():.1f}")
plt.axvline(df['DR1TSUGR'].median(), color='green', linestyle='-', label=f"Median: {df['DR1TSUGR'].median():.1f}")
plt.title('Distribution of Total Sugar Intake')
plt.xlabel('Sugar (grams)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# 2. Boxplot of Sugar by Tooth Decay
plt.figure(figsize=(8, 5))
sns.boxplot(x='OHQ660', y='DR1TSUGR', data=df, hue='OHQ660', palette='Set2', legend=False)
plt.xticks([0, 1], ['No Decay', 'Tooth Decay'])
plt.title('Sugar Intake by Tooth Decay Status')
plt.xlabel('Tooth Decay')
plt.ylabel('Sugar (grams)')
plt.show()

# 3. Boxplot of Sugar by Smoking
plt.figure(figsize=(8, 5))
sns.boxplot(x='Smoking_Label', y='DR1TSUGR', data=df, hue='Smoking_Label', palette='Set1', legend=False)
plt.title('Sugar Intake by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Sugar (grams)')
plt.show()

# 4. Scatterplot (Sugar vs Age)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='RIDAGEYR', y='DR1TSUGR', data=df, alpha=0.3, color='teal')
plt.title('Sugar Intake vs Age')
plt.xlabel('Age (years)')
plt.ylabel('Sugar (grams)')
plt.show()

# 5. Countplot of Tooth Decay by Gender
plt.figure(figsize=(8, 5))
sns.countplot(x='RIAGENDR', hue='OHQ660', data=df, palette='coolwarm')
plt.title('Tooth Decay Frequency by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Tooth Decay', labels=['No', 'Yes'])
plt.show()

# 6. Barplot of Mean Sugar by Age Group
df['AgeGroup'] = pd.cut(df['RIDAGEYR'], bins=[18, 30, 45, 60, 80], labels=['18-30', '31-45', '46-60', '60+'])
plt.figure(figsize=(8, 5))
sns.barplot(x='AgeGroup', y='DR1TSUGR', data=df, hue='AgeGroup', palette='viridis', errorbar=None, legend=False)
plt.title('Mean Sugar Intake by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Mean Sugar (grams)')
plt.show()

# 7. Line Plot: Mean Sugar Intake by Age Group
plt.figure(figsize=(8, 5))
sns.lineplot(x='AgeGroup', y='DR1TSUGR', data=df, marker='o', color='purple')
plt.title('Trend of Mean Sugar Intake Across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Mean Sugar (grams)')
plt.show()

# 8. Interaction Plot: Sugar by Tooth Decay, Split by Gender
plt.figure(figsize=(8, 5))
sns.catplot(x='OHQ660', y='DR1TSUGR', hue='RIAGENDR', data=df, kind='bar', palette='Set1', height=5, aspect=1.5)
plt.title('Interaction of Tooth Decay and Gender on Sugar Intake')
plt.xlabel('Tooth Decay (0=No, 1=Yes)')
plt.ylabel('Mean Sugar (grams)')
plt.show()

# 9. Split Boxplot: Sugar by Smoking and Tooth Decay
plt.figure(figsize=(8, 5))
sns.boxplot(x='Smoking_Label', y='DR1TSUGR', hue='OHQ660', data=df, palette='Set2')
plt.title('Sugar Intake by Smoking and Tooth Decay')
plt.xlabel('Smoking Status')
plt.ylabel('Sugar (grams)')
plt.legend(title='Tooth Decay', labels=['No', 'Yes'])
plt.show()

# 10. KDE Plot: Distribution of Sugar Intake by Gender
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='DR1TSUGR', hue='RIAGENDR', fill=True, palette='coolwarm', alpha=0.5)
plt.title('Density of Sugar Intake by Gender')
plt.xlabel('Sugar (grams)')
plt.ylabel('Density')
plt.show()

# 11. Pie Charts: Tooth Decay Percentage by Smoking Status
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
non_smokers = df[df['Smoking_Label'] == 'Non-Smoker']['OHQ660'].value_counts(normalize=True)
axes[0].pie(non_smokers, labels=['No Decay', 'Decay'], autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'], startangle=90)
axes[0].set_title('Tooth Decay in Non-Smokers')
smokers = df[df['Smoking_Label'] == 'Smoker']['OHQ660'].value_counts(normalize=True)
axes[1].pie(smokers, labels=['No Decay', 'Decay'], autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'], startangle=90)
axes[1].set_title('Tooth Decay in Smokers')
plt.tight_layout()
plt.show()

# 12. Correlation Heatmap
plt.figure(figsize=(8, 6))
corr_cols = ['DR1TSUGR', 'RIDAGEYR', 'OHQ660', 'SMQ020']
corr_matrix = df[corr_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap (Descriptive)')
plt.tight_layout()
plt.show()

# 13. Shape Statistics
print("\n=== Shape Statistics ===")
for col in ['DR1TSUGR', 'RIDAGEYR']:
    skewness = df[col].skew()
    kurt = df[col].kurtosis()
    print(f"{col}: Skewness = {skewness:.2f}, Kurtosis = {kurt:.2f}")

print(f"Mode of Tooth Decay (OHQ660): {df['OHQ660'].mode()[0]}")
print(f"Mode of Smoking (SMQ020): {df['SMQ020'].mode()[0]}")
print(f"Mode of Gender (RIAGENDR): {df['RIAGENDR'].mode()[0]}")

# 14. Weighted Proportions
print("\n=== Weighted Proportions ===")
w_tooth_decay = (df['OHQ660'] * df['WTMEC2YR']).sum() / df['WTMEC2YR'].sum() * 100
print(f"Weighted % of Tooth Decay: {w_tooth_decay:.2f}%")
w_smoking = (df['SMQ020'] * df['WTMEC2YR']).sum() / df['WTMEC2YR'].sum() * 100
print(f"Weighted % of Smokers: {w_smoking:.2f}%")

# 15. QQ-Plot for Sugar
plt.figure(figsize=(6, 5))
stats.probplot(df['DR1TSUGR'], dist="norm", plot=plt)
plt.title('QQ-Plot of Total Sugar Intake')
plt.show()

# 16. Boxplot of Age by Tooth Decay
plt.figure(figsize=(8, 5))
sns.boxplot(x='OHQ660', y='RIDAGEYR', data=df, hue='OHQ660', palette='Set2', legend=False)
plt.xticks([0, 1], ['No Decay', 'Tooth Decay'])
plt.title('Age Distribution by Tooth Decay Status')
plt.xlabel('Tooth Decay')
plt.ylabel('Age (years)')
plt.show()

print("\n✅ All plots and statistics have been displayed successfully.")