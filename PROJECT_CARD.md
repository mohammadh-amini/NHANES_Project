# PROJECT_CARD

## Project Title
Association Between Sugar Intake, Smoking, and Tooth Decay in US Adults (NHANES 2021-2023)

## Main Research Question
Is sugar intake and smoking associated with tooth decay in US adults, even after controlling for age and gender?

## Introduction
Tooth decay is a major public health concern influenced by dietary and lifestyle factors. This project uses data from the National Health and Nutrition Examination Survey (NHANES) to investigate whether sugar intake and smoking are associated with tooth decay, while controlling for age and gender.

## Unit of Observation and Population
- **Unit of Observation:** Each row represents one individual participant in NHANES.
- **Target Population:** US adults aged 18 and older with valid data on sugar intake, smoking, and oral health.

## Main Variables

| Variable | Role | Scale |
|----------|------|-------|
| Tooth Decay (OHQ660) | Response | Binary (Yes/No) |
| Total Sugar Intake (DR1TSUGR) | Main Explanatory | Continuous (grams) |
| Smoking Status (SMQ020) | Main Explanatory | Binary (Yes/No) |
| Age (RIDAGEYR) | Covariate | Continuous (years) |
| Gender (RIAGENDR) | Covariate | Categorical (Male/Female) |
| Survey Weight (WTMEC2YR) | Weight | Continuous |

## Question Type
- **Main:** Associative (relationship between sugar/smoking and tooth decay)
- **Sub-questions:**
  - Descriptive: Distribution of sugar intake, smoking, and tooth decay.
  - Comparative: Differences in sugar intake between genders.

## Initial Hypothesis
Higher sugar intake and smoking are associated with a higher prevalence of tooth decay.

## Missing Data
- Total Sugar Intake: 22.82%
- Tooth Decay: 15.78%
- Smoking: 12.00%

## Initial Descriptive Comparison
Comparison of sugar intake between males and females (mean, median, standard deviation).

## Final Research Question
Is sugar intake and smoking associated with tooth decay in US adults, even after controlling for age and gender?