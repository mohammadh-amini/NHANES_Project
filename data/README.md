# Data Directory

The raw data files (`.xpt`) are included in this repository for ease of access.

## Official Source
- **Source:** NHANES 2021-2023 (National Health and Nutrition Examination Survey)
- **Publisher:** Centers for Disease Control and Prevention (CDC)
- **Access Date:** November 2, 2025

## Required Files (Downloaded from CDC)
- **DEMO_L.xpt** (Demographic Variables and Sample Weights): https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt
- **DR1TOT_L.xpt** (Dietary Interview - Total Nutrient Intakes): https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR1TOT_L.xpt
- **OHQ_L.xpt** (Oral Health Questionnaire): https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/OHQ_L.xpt
- **SMQ_L.xpt** (Smoking - Cigarette Use): https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/SMQ_L.xpt

## Analytical Dataset Reconstruction Steps
1. Place the four `.xpt` files in this `data/` folder.
2. Run `src/read_data.py` to merge the datasets using the unique identifier `SEQN`, clean the missing data, and filter for adults (age >= 18).
3. The script will generate `clean_data.csv` in this folder, which is used by `src/descriptive.py` for the final analysis.