import pandas as pd

apps = pd.read_csv("data/raw/apps.csv")
evidence = pd.read_csv("data/raw/evidence.csv")

print("Raw apps:", apps.shape)
print("Raw evidence:", evidence.shape)
print("\n=== POTENTIAL MISSING-VALUE MARKERS ===")

markers = [
    "Not specified in source examined",
    "Not applicable",
    "Not identified in sources examined",
]

for marker in markers:
    print(f"\n{marker}")

    print("Apps:")
    print((apps == marker).sum().sum())

    print("Evidence:")
    print((evidence == marker).sum().sum())
    print("\n=== MARKERS BY EVIDENCE COLUMN ===")

for column in evidence.columns:
    not_specified = (evidence[column] == "Not specified in source examined").sum()
    not_applicable = (evidence[column] == "Not applicable").sum()

    if not_specified > 0 or not_applicable > 0:
        print(
            column,
            "| not specified:", not_specified,
            "| not applicable:", not_applicable,
        )
        print("\n=== APPLYING INITIAL CLEANING RULES ===")

missing_marker = "Not specified in source examined"

date_and_version_columns = [
    "publication_or_update_date",
    "version_observed",
    "release_or_update_date_observed",
]

for column in date_and_version_columns:
    apps_count = 0

    evidence_count = (evidence[column] == missing_marker).sum()

    evidence[column] = evidence[column].replace(
        missing_marker,
        pd.NA
    )

    print(
        f"{column}: converted {evidence_count} "
        "source-not-specified values to missing"
    )

print("\nCleaning step complete.")
print("\n=== CONVERTING DATE COLUMNS ===")

apps["first_identified_date"] = pd.to_datetime(
    apps["first_identified_date"],
    errors="coerce"
)

evidence["date_checked"] = pd.to_datetime(
    evidence["date_checked"],
    errors="coerce"
)

print("Apps first_identified_date type:")
print(apps["first_identified_date"].dtype)

print("\nEvidence date_checked type:")
print(evidence["date_checked"].dtype)
print("\n=== APPLYING VERIFIED CORRECTIONS ===")

woebot_mask = apps["app_id"] == "APP001"

apps.loc[woebot_mask, "app_status"] = "Retired"

print(
    "APP001 status:",
    apps.loc[woebot_mask, "app_status"].iloc[0]
)
print("\n=== SAVING PROCESSED DATA ===")

apps.to_csv(
    "data/processed/apps_clean.csv",
    index=False
)

evidence.to_csv(
    "data/processed/evidence_clean.csv",
    index=False
)

print("Saved: data/processed/apps_clean.csv")
print("Saved: data/processed/evidence_clean.csv")
print("\n=== VERIFYING OUTPUT ===")

raw_apps_check = pd.read_csv("data/raw/apps.csv")
processed_apps_check = pd.read_csv("data/processed/apps_clean.csv")
processed_evidence_check = pd.read_csv("data/processed/evidence_clean.csv")

raw_woebot_status = raw_apps_check.loc[
    raw_apps_check["app_id"] == "APP001",
    "app_status"
].iloc[0]

processed_woebot_status = processed_apps_check.loc[
    processed_apps_check["app_id"] == "APP001",
    "app_status"
].iloc[0]

print("Raw APP001 status:", raw_woebot_status)
print("Processed APP001 status:", processed_woebot_status)

print("\nProcessed evidence missing values:")
print(
    processed_evidence_check[
        [
            "publication_or_update_date",
            "version_observed",
            "release_or_update_date_observed",
        ]
    ].isna().sum()
)