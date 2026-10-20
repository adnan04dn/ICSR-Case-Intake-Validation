# Adverse Event Signal Exploration Report

## 1. Objective
To explore synthetic adverse-event reports, summarize reporting
patterns, identify frequently reported drug-event combinations,
and highlight potential safety signals requiring expert review.

## 2. Dataset Description
The dataset contains 8 fictional adverse-event reports.

Fields include:
- Report ID
- Patient age and gender
- Suspected drug
- Indication
- Adverse reaction
- Reaction onset in days
- Severity
- Outcome
- Reporter type

## 3. Data Cleaning and Validation
- Checked the report structure and field names.
- Converted patient age and reaction onset to numeric values.
- Checked for missing values.
- Removed duplicate records based on Report ID.
- Retained the supplied clinical values without inventing replacements.

## 4. Reporting Frequency by Drug
Each suspected drug appears once in this dataset:
- Amoxicillin: 1 report
- Atorvastatin: 1 report
- Ciprofloxacin: 1 report
- Ibuprofen: 1 report
- Lisinopril: 1 report
- Metformin: 1 report
- Warfarin: 1 report
- Paclitaxel: 1 report

No drug has a higher report count than the others.

## 5. Severity and Outcomes
Severity classifications:
- Mild: 3 reports
- Moderate: 2 reports
- Severe: 2 reports
- Life-threatening: 1 report

Outcomes:
- Recovered: 3 reports
- Recovering: 1 report
- Hospitalized: 3 reports
- Not recovered: 1 report

Three reports have hospitalization recorded as the outcome.
One additional report has a life-threatening outcome.

These outcomes warrant careful safety review. Formal seriousness
classification should be checked against the applicable criteria
and full case information.

## 6. Potential Drug-Event Patterns
The dataset includes the following reported combinations:
- Amoxicillin — Skin rash and hives
- Atorvastatin — Severe muscle myalgia
- Ciprofloxacin — Tendonitis
- Ibuprofen — Gastric ulcer bleed
- Lisinopril — Persistent dry cough
- Metformin — Nausea and diarrhea
- Warfarin — Uncontrolled hemorrhage
- Paclitaxel — Peripheral neuropathy

These are reported associations in a fictional dataset, not proof
that the suspected drugs caused the events.

## 7. Limitations
- The dataset contains only eight reports.
- Each suspected drug appears only once.
- There is no drug-exposure denominator or control group.
- Reporting frequency cannot establish incidence or causation.
- The data are synthetic and must not be interpreted as real
  patient evidence.

## 8. Conclusion and Recommendations
This exploratory analysis identifies several clinically important
events for expert review, including hospitalization, bleeding,
tendonitis, and peripheral neuropathy.

The dataset is too small to establish a statistical safety signal.
Further review should consider case validity, medical history,
concomitant medicines, timing, alternative causes, and additional
reports.

A potential signal is a reason for further investigation, not
proof of causation.

## 9. Reproducibility
The accompanying Python script performs data checks, summarizes
report frequency and severity, and generates bar charts.

All findings should be verified against the supplied dataset before
final submission.
