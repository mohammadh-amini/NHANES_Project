import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import comb

# Set plot style
sns.set_theme(style="whitegrid")

# ==========================================
# Load Data
# ==========================================
df = pd.read_csv("../data/clean_data.csv")

# ==========================================
# Task 1: Define Events and Random Variables
# ==========================================
# Event A: Smoker (SMQ020 == 1)
# Event B: Tooth Decay (OHQ660 == 1)
# Event C: High Sugar Intake (DR1TSUGR > 100)
# Random Variable X: Number of smokers in a random sample of 10 (Binomial)

df['Event_A_Smoker'] = (df['SMQ020'] == 1.0).astype(int)
df['Event_B_Decay'] = (df['OHQ660'] == 1.0).astype(int)
df['Event_C_HighSugar'] = (df['DR1TSUGR'] > 100).astype(int)

print("=== 1. Marginal Probabilities ===")
p_smoker = df['Event_A_Smoker'].mean()
p_decay = df['Event_B_Decay'].mean()
p_high_sugar = df['Event_C_HighSugar'].mean()
print(f"P(Smoker) = {p_smoker:.4f}")
print(f"P(Tooth Decay) = {p_decay:.4f}")
print(f"P(High Sugar > 100g) = {p_high_sugar:.4f}")

# ==========================================
# Task 2: Joint Probabilities
# ==========================================
print("\n=== 2. Joint Probabilities ===")
p_smoker_and_decay = ((df['Event_A_Smoker'] == 1) & (df['Event_B_Decay'] == 1)).mean()
p_smoker_and_sugar = ((df['Event_A_Smoker'] == 1) & (df['Event_C_HighSugar'] == 1)).mean()
p_decay_and_sugar = ((df['Event_B_Decay'] == 1) & (df['Event_C_HighSugar'] == 1)).mean()

print(f"P(Smoker AND Decay) = {p_smoker_and_decay:.4f}")
print(f"P(Smoker AND High Sugar) = {p_smoker_and_sugar:.4f}")
print(f"P(Decay AND High Sugar) = {p_decay_and_sugar:.4f}")

# ==========================================
# Task 3: Conditional Probabilities
# ==========================================
print("\n=== 3. Conditional Probabilities ===")
p_decay_given_smoker = p_smoker_and_decay / p_smoker
p_decay_given_sugar = p_decay_and_sugar / p_high_sugar
p_smoker_given_decay = p_smoker_and_decay / p_decay

print(f"P(Decay | Smoker) = {p_decay_given_smoker:.4f}")
print(f"P(Decay | High Sugar) = {p_decay_given_sugar:.4f}")
print(f"P(Smoker | Decay) = {p_smoker_given_decay:.4f}")

# ==========================================
# Task 4: Independence Check
# ==========================================
print("\n=== 4. Independence Check ===")
expected_joint = p_smoker * p_decay
print(f"P(Smoker) * P(Decay) = {expected_joint:.4f}")
print(f"Actual P(Smoker AND Decay) = {p_smoker_and_decay:.4f}")
if abs(p_smoker_and_decay - expected_joint) < 0.01:
    print("-> Events seem independent.")
else:
    print("-> Events are likely dependent (difference > 0.01).")

# ==========================================
# Task 5 & A2: Binomial Distribution
# ==========================================
print("\n=== 5. Binomial Distribution (n=10) ===")
n = 10
p = p_smoker
x_values = np.arange(0, n + 1)
binomial_probs = [comb(n, x) * (p ** x) * ((1 - p) ** (n - x)) for x in x_values]

mean_binomial = n * p
var_binomial = n * p * (1 - p)
std_binomial = np.sqrt(var_binomial)

print(f"Expected Value (Mean) = {mean_binomial:.2f}")
print(f"Variance = {var_binomial:.2f}")
print(f"Standard Deviation = {std_binomial:.2f}")

plt.figure(figsize=(8, 5))
plt.bar(x_values, binomial_probs, color='skyblue', edgecolor='black')
plt.title(f'Binomial Distribution (n=10, p={p:.2f})')
plt.xlabel('Number of Smokers in Sample')
plt.ylabel('Probability')
plt.xticks(x_values)
plt.show()

# ==========================================
# Task 6 & A3: Normal Distribution Check
# ==========================================
print("\n=== 6. Normal Distribution Check (Sugar Intake) ===")
sugar = df['DR1TSUGR'].dropna()

plt.figure(figsize=(8, 5))
sns.histplot(sugar, kde=True, color='royalblue', bins=50)
plt.title('Distribution of Sugar Intake')
plt.xlabel('Sugar (grams)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(6, 5))
stats.probplot(sugar, dist="norm", plot=plt)
plt.title('Q-Q Plot: Sugar Intake vs Normal Distribution')
plt.show()

# Shapiro-Wilk Test (using a sample for performance)
sample_sugar = sugar.sample(min(5000, len(sugar)), random_state=42)
shapiro_stat, shapiro_p = stats.shapiro(sample_sugar)
print(f"Shapiro-Wilk p-value = {shapiro_p:.4e}")
if shapiro_p < 0.05:
    print("-> Sugar intake is NOT normally distributed (p < 0.05).")
else:
    print("-> Sugar intake is approximately normally distributed.")

# ==========================================
# Task 7: Expectation and Variance
# ==========================================
print("\n=== 7. Expectation & Variance of Sugar Intake ===")
print(f"Mean (Expected Value) = {sugar.mean():.2f}")
print(f"Variance = {sugar.var():.2f}")
print(f"Standard Deviation = {sugar.std():.2f}")

# ==========================================
# Task 8: Covariance and Correlation
# ==========================================
print("\n=== 8. Covariance & Correlation (Sugar vs Age) ===")
cov_sugar_age = df['DR1TSUGR'].cov(df['RIDAGEYR'])
corr_sugar_age = df['DR1TSUGR'].corr(df['RIDAGEYR'])
print(f"Covariance(Sugar, Age) = {cov_sugar_age:.2f}")
print(f"Correlation(Sugar, Age) = {corr_sugar_age:.2f}")

plt.figure(figsize=(8, 5))
sns.scatterplot(x='RIDAGEYR', y='DR1TSUGR', data=df, alpha=0.3, color='teal')
plt.title('Sugar Intake vs Age')
plt.xlabel('Age (years)')
plt.ylabel('Sugar (grams)')
plt.show()

# ==========================================
# Task 9: Bayes Theorem
# ==========================================
print("\n=== 9. Bayes Theorem ===")
# Formula: P(A|B) = P(B|A) * P(A) / P(B)
# We already calculated P(Smoker | Decay) above.
print(f"P(Smoker | Decay) computed via Bayes = {p_smoker_given_decay:.4f}")

# ==========================================
# Path A1: Conditional Probability in Subgroups
# ==========================================
print("\n=== A1. Conditional Probability by Gender ===")
male_df = df[df['RIAGENDR'] == 'Male']
female_df = df[df['RIAGENDR'] == 'Female']

p_decay_given_smoker_male = ((male_df['Event_A_Smoker'] == 1) & (male_df['Event_B_Decay'] == 1)).sum() / (male_df['Event_A_Smoker'] == 1).sum()
p_decay_given_smoker_female = ((female_df['Event_A_Smoker'] == 1) & (female_df['Event_B_Decay'] == 1)).sum() / (female_df['Event_A_Smoker'] == 1).sum()

print(f"P(Decay | Smoker, Male) = {p_decay_given_smoker_male:.4f}")
print(f"P(Decay | Smoker, Female) = {p_decay_given_smoker_female:.4f}")

# ==========================================
# Path A4: Role of Survey Weights in Empirical Probability
# ==========================================
print("\n=== A4. Unweighted vs Weighted Probability ===")
# Unweighted probability of tooth decay
unweighted_p_decay = df['Event_B_Decay'].mean()

# Weighted probability of tooth decay
weighted_p_decay = (df['Event_B_Decay'] * df['WTMEC2YR']).sum() / df['WTMEC2YR'].sum()

print(f"Unweighted P(Decay) = {unweighted_p_decay:.4f}")
print(f"Weighted P(Decay) = {weighted_p_decay:.4f}")
print("-> Weighted probability is a better estimate for the US population.")

print("\n✅ All Phase 2 probability tasks completed.")