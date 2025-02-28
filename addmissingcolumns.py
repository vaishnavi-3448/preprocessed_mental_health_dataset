import pandas as pd


file_path = "mental_health_diagnosis_treatment_.csv"
df = pd.read_csv(file_path)


df["Scheduled Time"] = pd.NaT  
df["Taken Time"] = pd.NaT 
df["Missed Dose"] = "No"  
df["Pill Count Left"] = 0  
df["Notification Sent"] = "No"  
df["AI Prediction of Missed Dose"] = "No"  


df.to_csv(file_path, index=False)
print("✅ Columns added successfully!")
