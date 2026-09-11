import sqlite3
import pandas as pd

database_path = "database/evidence_tracker.db"

connection = sqlite3.connect(database_path)
connection.execute("PRAGMA foreign_keys = ON")

print("Database connection created.")

cursor = connection.cursor()

create_apps_table = """
CREATE TABLE IF NOT EXISTS apps (
    app_id TEXT PRIMARY KEY,
    app_name TEXT NOT NULL,
    developer TEXT NOT NULL,
    app_category TEXT NOT NULL,
    mental_health_focus TEXT NOT NULL,
    official_website_url TEXT,
    app_description_summary TEXT,
    ai_disclosure_status TEXT NOT NULL,
    ai_claim_summary TEXT,
    primary_claims TEXT,
    target_population TEXT,
    app_status TEXT NOT NULL,
    first_identified_date TEXT NOT NULL
);
"""

cursor.execute(create_apps_table)

create_evidence_table = """
CREATE TABLE IF NOT EXISTS evidence (
    evidence_id TEXT PRIMARY KEY,
    app_id TEXT NOT NULL,
    platform TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_title TEXT NOT NULL,
    source_url TEXT NOT NULL,
    publication_or_update_date TEXT,
    date_checked TEXT NOT NULL,
    version_observed TEXT,
    release_or_update_date_observed TEXT,
    finding_domain TEXT NOT NULL,
    finding_status TEXT NOT NULL,
    finding_detail TEXT NOT NULL,
    claim_text_or_summary TEXT,
    evidence_strength TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (app_id) REFERENCES apps(app_id)
);
"""

cursor.execute(create_evidence_table)

connection.commit()

print("Apps table created.")
print("Evidence table created.")

apps = pd.read_csv("data/processed/apps_clean.csv")
evidence = pd.read_csv("data/processed/evidence_clean.csv")

print("\nProcessed CSV files loaded.")

# Clear existing records so the script can be rerun safely.
cursor.execute("DELETE FROM evidence")
cursor.execute("DELETE FROM apps")

apps_sql = apps.where(pd.notna(apps), None)
evidence_sql = evidence.where(pd.notna(evidence), None)

apps_sql.to_sql(
    "apps",
    connection,
    if_exists="append",
    index=False
)

evidence_sql.to_sql(
    "evidence",
    connection,
    if_exists="append",
    index=False
)

connection.commit()

print(f"Apps inserted: {len(apps_sql)}")
print(f"Evidence records inserted: {len(evidence_sql)}")

connection.close()

print("Database connection closed.")