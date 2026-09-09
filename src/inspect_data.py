import pandas as pd

apps = pd.read_csv("data/raw/apps.csv")
evidence = pd.read_csv("data/raw/evidence.csv")

print("=== APPS DATASET ===")

print("Shape:")
print(apps.shape)

print("\nColumns:")
print(apps.columns.tolist())

print("\nData types:")
print(apps.dtypes)

print("\nMissing values:")
print(apps.isna().sum())

print("\n=== EVIDENCE DATASET ===")

print("Shape:")
print(evidence.shape)

print("\nColumns:")
print(evidence.columns.tolist())

print("\nData types:")
print(evidence.dtypes)

print("\nMissing values:")
print(evidence.isna().sum())
print("\n=== IMPORTANT CATEGORICAL VALUES ===")

print("\nApp status:")
print(apps["app_status"].value_counts())

print("\nAI disclosure status:")
print(apps["ai_disclosure_status"].value_counts())

print("\nSource types:")
print(evidence["source_type"].value_counts())

print("\nFinding domains:")
print(evidence["finding_domain"].value_counts())

print("\nFinding statuses:")
print(evidence["finding_status"].value_counts())

print("\nEvidence strength:")
print(evidence["evidence_strength"].value_counts())