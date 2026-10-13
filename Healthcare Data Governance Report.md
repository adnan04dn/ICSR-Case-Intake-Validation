# Task 02: Healthcare Data Governance and Cleaning

## 1. Objective

To assess the quality of synthetic patient records, define data
validation rules, document data fields, and identify data-quality
issues without inventing clinical values.

## 2. Dataset Overview

The dataset contains 10 synthetic patient records, from PAT-201
to PAT-210.

Fields:
- PatientID
- Age
- Gender
- Diagnosis
- PrimaryMedication
- DosageMg
- TreatmentDurationDays
- Readmitted
- BloodPressure
- CholesterolLevel

The dataset is intended for educational purposes only.

## 3. Data Dictionary

| Field | Description | Validation Rule |
|---|---|---|
| PatientID | Unique patient identifier | Must be present and unique |
| Age | Patient age in years | Must be numeric and within a defined plausible range |
| Gender | Recorded gender | Must follow the dataset's allowed categories |
| Diagnosis | Recorded diagnosis | Must not be blank |
| PrimaryMedication | Main medication | Must not be blank |
| DosageMg | Recorded dose in mg | Must be numeric and clinically reviewed |
| TreatmentDurationDays | Treatment duration | Must be a positive number |
| Readmitted | Readmission status | Must be Yes or No |
| BloodPressure | Blood pressure reading | Must follow the defined format |
| CholesterolLevel | Cholesterol measurement | Must be numeric and have a documented unit |

## 4. Validation Results

- Total records: 10
- Patient IDs shown: PAT-201 to PAT-210
- Duplicate IDs: None apparent in the supplied screenshot
- Missing values: None visibly apparent
- Readmission values: Yes/No format appears consistent
- Blood pressure: Values appear in systolic/diastolic format
- Numeric fields: Require validation in a spreadsheet or script

The screenshot alone cannot verify every data-quality rule.

## 5. Data Cleaning Rules

1. Preserve the original dataset as a read-only source.
2. Check that PatientID values are unique.
3. Validate numeric fields and documented ranges.
4. Standardize categorical values only when their intended meaning
   is clear.
5. Preserve missing values as missing; do not invent clinical data.
6. Check blood pressure formatting and cholesterol units.
7. Record every change in the exception log.
8. Keep the cleaned output separate from the original dataset.

## 6. Exception Log

| Field or Check | Finding | Action |
|---|---|---|
| PatientID | No duplicate apparent in screenshot | Verify programmatically |
| Age | Numeric values shown | Validate permitted range |
| DosageMg | Numeric values shown | Check medication-specific units and plausibility |
| TreatmentDurationDays | Numeric values shown | Validate positive duration |
| Readmitted | Yes/No values shown | Standardize if needed |
| BloodPressure | Slash-separated readings | Validate format and units |
| CholesterolLevel | Numeric values shown | Confirm measurement units |

No clinical values have been changed or inferred in this report.

## 7. Privacy and Governance

- The supplied records are synthetic and de-identified training data.
- Do not add real patient identifiers or personal information.
- Restrict access to data according to organisational requirements.
- Preserve an audit trail of cleaning decisions.
- Share only the minimum data necessary for the task.

## 8. Conclusion

The supplied sample contains 10 synthetic patient records. Initial
visual inspection shows no obvious duplicate identifiers or blank
fields, but a complete validation requires checking the original CSV
using reproducible spreadsheet or code-based rules.

The cleaned dataset, validation output, data dictionary, and exception
log should be retained together for review.

Training purposes only.
