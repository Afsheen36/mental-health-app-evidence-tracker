import pandas as pd

apps = pd.read_csv("data/processed/apps_clean.csv")
evidence = pd.read_csv("data/processed/evidence_clean.csv")

print("=== DATA VALIDATION REPORT ===")

# Check app_id
missing_app_ids = apps["app_id"].isna().sum()
duplicate_app_ids = apps["app_id"].duplicated().sum()

print("\nApp ID checks:")
print("Missing app_id:", missing_app_ids)
print("Duplicate app_id:", duplicate_app_ids)

# Check evidence_id
missing_evidence_ids = evidence["evidence_id"].isna().sum()
duplicate_evidence_ids = evidence["evidence_id"].duplicated().sum()

print("\nEvidence ID checks:")
print("Missing evidence_id:", missing_evidence_ids)
print("Duplicate evidence_id:", duplicate_evidence_ids)

# Check relationships between the two datasets
invalid_app_references = ~evidence["app_id"].isin(apps["app_id"])

print("\nRelationship check:")
print(
    "Evidence records with unknown app_id:",
    invalid_app_references.sum()
)
print("\nControlled vocabulary checks:")

allowed_app_status = {
    "Active",
    "Retired",
    "Unavailable",
    "Unclear",
}

allowed_ai_status = {
    "Explicitly disclosed",
    "Not identified in sources examined",
    "Unclear",
    "Not assessed",
}

allowed_finding_status = {
    "Identified",
    "Not identified in sources examined",
    "Claim identified but supporting evidence not identified",
    "Evidence identified and relevant",
    "Evidence identified but insufficient for specified claim",
    "Evidence identified but not directly applicable",
    "Unclear",
    "Not assessable",
    "Not applicable",
}

allowed_evidence_strength = {
    "Direct primary source",
    "Direct peer-reviewed evidence",
    "Indirect/supporting evidence",
    "Insufficient to assess",
    "Not applicable",
}

invalid_app_status = ~apps["app_status"].isin(allowed_app_status)
invalid_ai_status = ~apps["ai_disclosure_status"].isin(allowed_ai_status)
invalid_finding_status = ~evidence["finding_status"].isin(allowed_finding_status)
invalid_evidence_strength = ~evidence["evidence_strength"].isin(
    allowed_evidence_strength
)

print("Invalid app_status:", invalid_app_status.sum())
print("Invalid ai_disclosure_status:", invalid_ai_status.sum())
print("Invalid finding_status:", invalid_finding_status.sum())
print("Invalid evidence_strength:", invalid_evidence_strength.sum())
print("\n=== REQUIRED FIELD CHECKS ===")

required_app_columns = [
    "app_id",
    "app_name",
    "developer",
    "app_category",
    "mental_health_focus",
    "app_status",
    "first_identified_date",
]

required_evidence_columns = [
    "evidence_id",
    "app_id",
    "platform",
    "source_type",
    "source_title",
    "source_url",
    "date_checked",
    "finding_domain",
    "finding_status",
    "finding_detail",
    "evidence_strength",
]

print("\nApps:")
for column in required_app_columns:
    missing_count = apps[column].isna().sum()
    print(f"{column}: {missing_count} missing")

print("\nEvidence:")
for column in required_evidence_columns:
    missing_count = evidence[column].isna().sum()
    print(f"{column}: {missing_count} missing")

print("\n=== DATE VALIDATION ===")

invalid_app_dates = (
    apps["first_identified_date"].notna()
    & pd.to_datetime(
        apps["first_identified_date"],
        errors="coerce"
    ).isna()
).sum()

invalid_checked_dates = (
    evidence["date_checked"].notna()
    & pd.to_datetime(
        evidence["date_checked"],
        errors="coerce"
    ).isna()
).sum()

print(
    "Invalid first_identified_date values:",
    invalid_app_dates
)

print(
    "Invalid date_checked values:",
    invalid_checked_dates
)
print("\n=== FINAL VALIDATION SUMMARY ===")

total_required_missing = (
    apps[required_app_columns].isna().sum().sum()
    + evidence[required_evidence_columns].isna().sum().sum()
)

validation_errors = (
    missing_app_ids
    + duplicate_app_ids
    + missing_evidence_ids
    + duplicate_evidence_ids
    + invalid_app_references.sum()
    + invalid_app_status.sum()
    + invalid_ai_status.sum()
    + invalid_finding_status.sum()
    + invalid_evidence_strength.sum()
    + total_required_missing
    + invalid_app_dates
    + invalid_checked_dates
)

if validation_errors == 0:
    print("PASS: All validation checks passed.")
else:
    print(f"FAIL: {validation_errors} validation issue(s) detected.")