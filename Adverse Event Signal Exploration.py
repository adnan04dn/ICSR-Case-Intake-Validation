import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data = """ReportID,PatientAge,PatientGender,SuspectedDrug,Indication,AdverseReaction,ReactionOnsetDays,Severity,Outcome,ReporterType
ADR-9001,45,Female,Amoxicillin,Bacterial Infection,Skin Rash & Hives,2,Mild,Recovered,Pharmacist
ADR-9002,62,Male,Atorvastatin,Hyperlipidemia,Severe Muscle Myalgia,14,Moderate,Recovering,Physician
ADR-9003,71,Female,Ciprofloxacin,UTI,Tendonitis,7,Severe,Hospitalized,Physician
ADR-9004,28,Male,Ibuprofen,Headache,Gastric Ulcer Bleed,5,Severe,Hospitalized,Patient
ADR-9005,53,Female,Lisinopril,Hypertension,Persistent Dry Cough,21,Mild,Recovered,Pharmacist
ADR-9006,39,Male,Metformin,Diabetes,Nausea & Diarrhea,1,Mild,Recovered,Patient
ADR-9007,68,Male,Warfarin,Atrial Fibrillation,Uncontrolled Hemorrhage,10,Life-Threatening,Hospitalized,Physician
ADR-9008,50,Female,Paclitaxel,Chemotherapy,Peripheral Neuropathy,30,Moderate,Not Recovered,Oncologist
"""

df = pd.read_csv(StringIO(data))

# 1. Data validation
df["PatientAge"] = pd.to_numeric(df["PatientAge"], errors="coerce")
df["ReactionOnsetDays"] = pd.to_numeric(
    df["ReactionOnsetDays"], errors="coerce"
)

df = df.drop_duplicates(subset=["ReportID"])

print("DATASET OVERVIEW")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())

# 2. Reporting frequency by suspected drug
drug_frequency = df["SuspectedDrug"].value_counts()
print("\nReports by drug:")
print(drug_frequency)

# 3. Severity frequency
severity_frequency = df["Severity"].value_counts()
print("\nReports by severity:")
print(severity_frequency)

# 4. Serious-report proportion
serious_outcomes = ["Hospitalized", "Life-Threatening"]
serious_count = df["Outcome"].isin(serious_outcomes).sum()
total_reports = len(df)

print("\nTotal reports:", total_reports)
print("Reports with hospitalization/life-threatening outcome:",
      serious_count)
print("Proportion (%):",
      round(serious_count / total_reports * 100, 2))

# 5. Drug-event combinations
drug_event = (
    df.groupby(["SuspectedDrug", "AdverseReaction"])
      .size()
      .reset_index(name="ReportCount")
      .sort_values("ReportCount", ascending=False)
)
print("\nDrug-event combinations:")
print(drug_event)

# 6. Visualize report frequency
drug_frequency.plot(kind="bar")
plt.title("Adverse Event Reports by Suspected Drug")
plt.xlabel("Suspected Drug")
plt.ylabel("Number of Reports")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("reports_by_drug.png")
plt.show()

# 7. Visualize severity
severity_frequency.plot(kind="bar")
plt.title("Adverse Event Reports by Severity")
plt.xlabel("Severity")
plt.ylabel("Number of Reports")
plt.tight_layout()
plt.savefig("reports_by_severity.png")
plt.show()

print("\nLimitations:")
print("- This is a small synthetic dataset.")
print("- Reporting counts do not establish causation.")
print("- No incidence rates can be calculated without exposure data.")
print("- Potential signals require expert clinical and statistical review.")
