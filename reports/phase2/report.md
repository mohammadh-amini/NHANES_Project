# Phase 2 Report: Probability and Probability Distributions

**Student:** Mohammad Hossein Amini (403100065)
**Course:** Statistics and Its Applications
**Instructor:** Dr. Kasra Alishahi

## 1. Defined Events
- **Event A:** Smoker (`SMQ020 == 1`)
- **Event B:** Tooth Decay (`OHQ660 == 1`)
- **Event C:** High Sugar Intake (`DR1TSUGR > 100`)

## 2. Marginal, Joint, and Conditional Probabilities
- **P(Smoker) = 0.4133**, **P(Decay) = 0.3718**, **P(High Sugar) = 0.3730**
- **P(Smoker AND Decay) = 0.1844**
- **P(Decay | Smoker) = 0.4462**
- **P(Decay | High Sugar) = 0.4087**
- **P(Smoker | Decay) = 0.4961** (Computed via Bayes' Theorem)

## 3. Independence Check
- P(Smoker) * P(Decay) = 0.1537
- Actual P(Smoker AND Decay) = 0.1844
- **Conclusion:** Because the difference is greater than 0.01, the events are **dependent**. (Smoking and tooth decay are associated).

## 4. Binomial Distribution
- We modeled the number of smokers in a sample of 10.
- Mean = 4.13, Variance = 2.42.
- **Assumption Violation:** The binomial model assumes a constant probability of smoking (p). However, our data shows that smoking rates vary by gender and age. We simulated 500 samples of size 10 to compare the empirical and theoretical distributions.

## 5. Normal Distribution Check (Sugar Intake)
- **Shapiro-Wilk p-value = 1.5099e-55**
- **Conclusion:** Sugar intake is **NOT normally distributed** (it is highly right-skewed). A Q-Q plot confirmed the deviation from normality.

## 6. Expectation and Variance
- **Sugar Intake:** Mean = 95.47, Variance = 4641.38, SD = 68.13.
- **Interpretation:** On average, participants consume 95.47 grams of sugar daily, but the variance is extremely high, indicating a wide spread in dietary habits.

## 7. Covariance and Correlation
- **Covariance(Sugar, Age) = -15.90**
- **Correlation(Sugar, Age) = -0.01**
- **Conclusion:** There is almost no linear relationship between age and sugar intake.

## 8. NHANES Special Requirements
- **A1. Conditional Probability by Subgroups:** 
  - P(Decay | Smoker, Male) = 0.4304
  - P(Decay | Smoker, Female) = 0.4625
- **A4. Unweighted vs. Weighted Probability:**
  - Unweighted P(Decay) = 0.3718
  - Weighted P(Decay) = 0.3465
  - **Interpretation:** The weighted probability (34.65%) is a more accurate estimate of the US population, as it accounts for the complex survey design of NHANES.