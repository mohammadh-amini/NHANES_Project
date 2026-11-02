# Data Directory

The raw data files (`.xpt`) are not included in this repository due to their size and to comply with project guidelines. 
Please download the following files from the NHANES 2021-2023 website and place them in this folder:

- **DEMO_L.xpt** (Demographic Variables and Sample Weights): 
  [Download Link](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt)

- **DR1TOT_L.xpt** (Dietary Interview - Total Nutrient Intakes): 
  [Download Link](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DR1TOT_L.xpt)

- **OHQ_L.xpt** (Oral Health Questionnaire): 
  [Download Link](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/OHQ_L.xpt)

- **SMQ_L.xpt** (Smoking - Cigarette Use): 
  [Download Link](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/SMQ_L.xpt)

## Processed Data
After running `src/read_data.py`, a cleaned dataset (`clean_data.csv`) will be generated in this folder. This file is also excluded from the repository via `.gitignore`.