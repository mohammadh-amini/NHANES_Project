# Phase 1 Report: Understanding the Study, Data, and Descriptive Statistics

## 1. Data Source and Collection Mechanism (Task 1)
- **Official Source:** The data were extracted from the National Health and Nutrition Examination Survey (NHANES) for the 2021-2023 cycle (Source: CDC/NCHS).
- **Study Type:** This data comes from an **Observational Study**, not a randomized controlled trial. Therefore, causal relationships cannot be established, and only associations can be described.
- **Access Limitations:** The data are public and do not require special permissions. They can be downloaded directly from the official CDC website.

## 2. Unit of Observation and Data Structure (Task 2)
- **Unit of Observation:** Each row in the dataset represents **one individual participant** in the survey.
- **Data Structure:** The data are cross-sectional, meaning there is only one observation recorded per individual.
- **Merge Key:** To link the three datasets—Demographic (`DEMO_L`), Anthropometric (`BMX_L`), and Blood Pressure (`BPXO_L`)—the unique identifier `SEQN` was used.
- **Data Flow Table:**
  - Total individuals in DEMO file: 11,933
  - Total in BMX file: 8,860
  - Total in BPXO file: 7,801
  - After merging DEMO+BMX: 8,860
  - After merging with BPXO: 7,801
  - After dropping missing values: 7,453
  - After filtering Age ≥ 18: **6,061** (Final Analytical Population)

## 3. Sampling, Selection, and Generalizability (Task 3)
- **Sampling Method:** NHANES uses a complex, multistage, stratified, and clustered probability sampling design.
- **Generalizability:** Due to the use of survey weights, the results of this survey are generalizable to the civilian, non-institutionalized US population (provided the weights are applied correctly).

## 4. Variable Classification (Task 4)
| Variable | Name in Data | Type | Scale |
| :--- | :--- | :--- | :--- |
| Individual ID | `SEQN` | Quantitative (Discrete) | Numeric |
| Gender | `RIAGENDR` | Categorical (Binary) | Nominal (1=Male, 2=Female) |
| Age | `RIDAGEYR` | Quantitative (Discrete) | Numeric (Years) |
| Body Mass Index | `BMXBMI` | Quantitative (Continuous) | Numeric (kg/m²) |
| Systolic Blood Pressure | `BPXOSY1-3` | Quantitative (Continuous) | Numeric (mmHg) |
| Survey Weight | `WTMEC2YR` | Quantitative (Continuous) | Numeric |

## 5. Data Quality Audit (Task 5)
- **Missing Data:** In the raw data, BMI had approximately 1.41% missing values, and Blood Pressure had about 3.64%.
- **Handling Method:** Records with missing values in the primary variables (BMI and BP) were dropped from the analysis to ensure calculations were based on valid data.
- **Special Codes:** No impossible values (e.g., BMI < 10 or negative blood pressure) were observed.

## 6. Frequency Tables and Empirical Distribution (Tasks 6 & 7)
- **Gender Distribution in Final Sample:**
  - Males: 3,313 (54.66%)
  - Females: 2,748 (45.34%)
- **Summary of Quantitative Variables:**
  - **BMI:** Mean = 29.56, Median = 28.30, SD = 7.19. (Right-skewed distribution due to high BMI values).
  - **Systolic BP:** Mean = 122.36, Median = 120.00, SD = 17.91. (Relatively symmetric distribution).

## 7. Proper Visualization (Task 8)
Four meaningful plots were generated and saved in the `figures/` folder:
1. `hist_bmi_sbp.png`: Histograms of BMI and Systolic BP distributions.
2. `box_gender.png`: Comparison of Systolic BP between males and females.
3. `scatter_bmi_sbp.png`: Scatter plot showing the relationship between BMI and Systolic BP.

## 8. Initial Descriptive Comparison (Task 9)
- **Males:** Mean BMI = 29.06, Mean Systolic BP = 124.76
- **Females:** Mean BMI = 29.99, Mean Systolic BP = 120.37
- **Initial Interpretation:** In this sample, females have a higher mean BMI but lower systolic BP. This indicates that gender may act as a **confounder** and should be controlled for in subsequent phases.

## 9. Special Requirements for Path A (NHANES)
### A2. Identifying Weights and Sampling Design
- The appropriate weight variable for examination-based analyses in this section is `WTMEC2YR`. In NHANES, each individual represents a different number of people in the population because their probability of selection varies (e.g., some groups are oversampled). Weighting corrects this imbalance, making the results generalizable to the entire population.

### A3. Comparison of Raw vs. Weighted Estimates
| Variable | Raw Mean (Unweighted) | Weighted Mean |
| :--- | :--- | :--- |
| BMI | 29.56 | 29.47 |
| Systolic BP | 122.36 | 120.77 |
- **Discussion:** The difference between the raw and weighted means shows that our sample does not perfectly reflect the population. The weighted BP mean is lower, meaning individuals with high blood pressure are slightly underrepresented in the raw sample.

## 10. Finalizing the Statistical Question (Task 10)
Based on our understanding of the data, the primary question is:
**"Is BMI associated with systolic blood pressure in US adults (Age ≥ 18), even after controlling for the effects of age and gender?"**
The available data, containing both variables in complete quantitative form, are perfectly suited to answer this question.