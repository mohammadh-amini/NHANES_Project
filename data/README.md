# Data Source and Reconstruction

## Source
- NHANES 2021-2023 (CDC/NCHS)
- Link: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023

## Files Used
- `DEMO_L.xpt` (Demographics & Weights)
- `BMX_L.xpt` (Body Measures)
- `BPXO_L.xpt` (Blood Pressure)

## Reconstruction Steps
1. Download the three `.xpt` files from the CDC website.
2. Merge files using the unique identifier `SEQN` (inner join).
3. Calculate `SBP_mean` as the average of BPXOSY1, BPXOSY2, and BPXOSY3.
4. Drop rows with missing values in BMI or SBP.
5. Filter the analytical population to adults (Age >= 18).
6. Save the cleaned dataset as `clean_data.csv`.