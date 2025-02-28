import pandas as pd

file_path = "mental_health_diagnosis_treatment_.csv"
df = pd.read_csv(file_path)


num_cols = ["Symptom Severity (1-10)", "Mood Score (1-10)", "Sleep Quality (1-10)", 
            "Physical Activity (hrs/week)", "Treatment Duration (weeks)", 
            "Stress Level (1-10)", "Treatment Progress (1-10)", 
            "Adherence to Treatment (%)", "Pill Count Left"]

df[num_cols] = df[num_cols].fillna(df[num_cols].mean())


cat_cols = ["Gender", "Diagnosis", "Medication", "Therapy Type", "Outcome", 
            "AI-Detected Emotional State", "Notification Sent", "AI Prediction of Missed Dose"]

df[cat_cols] = df[cat_cols].fillna("Unknown")


date_cols = ["Treatment Start Date", "Scheduled Time", "Taken Time"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

df[['Scheduled Time', 'Taken Time']] = df[['Scheduled Time', 'Taken Time']].fillna(0)


df.to_csv("preprocessed_mental_health_dataset.csv", index=False)

print("✅ Dataset preprocessing complete! Saved as 'preprocessed_mental_health_dataset.csv'.")
