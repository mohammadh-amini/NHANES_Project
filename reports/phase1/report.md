# Phase 1 Report: Descriptive Analysis

## Research Question
Is sugar intake and smoking associated with tooth decay in US adults, even after controlling for age and gender?

## Data Source
- **Source:** NHANES 2021-2023 (National Health and Nutrition Examination Survey)
- **Datasets Used:** DEMO_L, DR1TOT_L, OHQ_L, SMQ_L
- **Analytical Sample:** 4,788 adults (age ≥ 18)

## Key Findings
- **Tooth Decay:** 37.18% of participants reported having tooth decay.
- **Smoking:** 41.33% had a history of smoking (at least 100 cigarettes).
- **Sugar Intake:** Mean = 95.47 grams, Median = 81.12 grams, SD = 68.13 grams.
- **Gender Differences:** Males consumed significantly more sugar (107.79 g) than females (85.75 g).

## Data Flow
| Processing Step | Count |
|-----------------|-------|
| Raw DEMO | 11,933 |
| After DEMO + Diet Merge | 8,860 |
| After Oral Health Merge | 7,801 |
| After Smoking Merge | 7,453 |
| Final Analytical Sample (Age 18+) | **4,788** |

## Visualizations
Six high-quality plots were generated:
1. Histogram of Sugar Intake (with Mean and Median lines)
2. Boxplot: Sugar by Tooth Decay
3. Boxplot: Sugar by Smoking
4. Scatterplot: Sugar vs Age
5. Barplot: Tooth Decay by Gender
6. Barplot: Mean Sugar by Age Group

## Files in this Phase
- `read_data.py`: Data loading, merging, and cleaning.
- `descriptive.py`: Descriptive statistics and visualization.
- `data_flow.csv`: Data flow summary.
- `descriptive_stats.csv`: Summary statistics.
- `gender_table.csv`, `tooth_decay_table.csv`, `smoking_table.csv`: Frequency tables.
- `sugar_by_gender.csv`: Gender comparison.
- `report.tex` / `report.pdf`: Full journal-style report.