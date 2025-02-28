import pandas as pd

# Load the dataset
file_path = "mental_health_diagnosis_treatment_.csv"
df = pd.read_csv(file_path)

# Print all column names
print("Columns in dataset:", df.columns.tolist())
