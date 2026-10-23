# PROJECT_CARD

## Tentative Title
Association Between BMI and Systolic Blood Pressure in US Adults (NHANES 2021–2023)

## Primary Question
Is BMI associated with systolic blood pressure, even after controlling for age and gender?

## Introduction
Systolic blood pressure is influenced by numerous factors. BMI is one such factor, but age and gender also play significant roles. To isolate the effect of BMI from age and gender, these variables must be controlled for in the analysis.

## Unit of Observation and Population
- **Unit of Observation:** Each row = one participant in NHANES.
- **Target Population:** US adults (Age ≥ 18) with valid BMI and blood pressure measurements.

## Primary Variables

| Variable | Role | Scale |
| :--- | :--- | :--- |
| BPXOSY1 (Mean of 3 measurements) | Response | Quantitative (Continuous) |
| BMXBMI | Main Explanatory | Quantitative (Continuous) |
| RIDAGEYR | Confounder | Quantitative |
| RIAGENDR | Confounder | Categorical (Binary) |
| WTMEC2YR | Weight | — |
| SDMVPSU, SDMVSTRA | Design | — |

## Question Type
- **Primary:** Associational
- **Sub-questions:**
  - Descriptive: Distribution of BMI and Blood Pressure
  - Comparative: Blood Pressure between males and females

## Initial Hypothesis
There is a positive, moderate association between BMI and systolic blood pressure.

## Missing Data
- **Final Row Count:** 7,801
- **BMXBMI:** 1.41%
- **BPXOSY1:** 3.64%

## Initial Descriptive Comparison
Comparison of systolic blood pressure between males and females (mean, median, standard deviation). No hypothesis testing yet.

## Final Question
Is BMI associated with systolic blood pressure, even after controlling for age and gender?