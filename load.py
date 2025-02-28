import pandas as pd

# Load the dataset
file_path = "mental_health_diagnosis_treatment_.csv"
df = pd.read_csv(file_path)

# View the first few rows and check for missing values
print(df.head())
print(df.info())
print(df.isnull().sum())  # Check how many missing values are in each column
