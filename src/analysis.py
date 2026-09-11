import sqlite3
import pandas as pd

database_path = "database/evidence_tracker.db"

connection = sqlite3.connect(database_path)

print("=== MENTAL HEALTH APP EVIDENCE ANALYSIS ===")


# --------------------------------------------------
# 1. Evidence coverage by app
# --------------------------------------------------

evidence_per_app = pd.read_sql_query(
    """
    SELECT
        apps.app_id,
        apps.app_name,
        apps.app_status,
        COUNT(evidence.evidence_id) AS evidence_count
    FROM apps
    LEFT JOIN evidence
        ON apps.app_id = evidence.app_id
    GROUP BY apps.app_id, apps.app_name, apps.app_status
    ORDER BY evidence_count DESC, apps.app_name
    """,
    connection,
)

print("\n=== EVIDENCE RECORDS PER APP ===")
print(evidence_per_app.to_string(index=False))


# --------------------------------------------------
# 2. Finding-domain distribution
# --------------------------------------------------

finding_domains = pd.read_sql_query(
    """
    SELECT
        finding_domain,
        COUNT(*) AS record_count
    FROM evidence
    GROUP BY finding_domain
    ORDER BY record_count DESC
    """,
    connection,
)

finding_domains["percentage"] = (
    finding_domains["record_count"]
    / finding_domains["record_count"].sum()
    * 100
).round(1)

print("\n=== FINDING DOMAIN DISTRIBUTION ===")
print(finding_domains.to_string(index=False))


# --------------------------------------------------
# 3. Clinical evidence assessment
# --------------------------------------------------

clinical_findings = pd.read_sql_query(
    """
    SELECT
        finding_status,
        COUNT(*) AS record_count
    FROM evidence
    WHERE finding_domain = 'Clinical evidence'
    GROUP BY finding_status
    ORDER BY record_count DESC
    """,
    connection,
)

clinical_findings["percentage"] = (
    clinical_findings["record_count"]
    / clinical_findings["record_count"].sum()
    * 100
).round(1)

print("\n=== CLINICAL EVIDENCE ASSESSMENT ===")
print(clinical_findings.to_string(index=False))


# --------------------------------------------------
# 4. AI disclosure evidence
# --------------------------------------------------

ai_disclosure = pd.read_sql_query(
    """
    SELECT
        finding_status,
        COUNT(*) AS record_count
    FROM evidence
    WHERE finding_domain = 'AI disclosure'
    GROUP BY finding_status
    ORDER BY record_count DESC
    """,
    connection,
)

ai_disclosure["percentage"] = (
    ai_disclosure["record_count"]
    / ai_disclosure["record_count"].sum()
    * 100
).round(1)

print("\n=== AI DISCLOSURE EVIDENCE ===")
print(ai_disclosure.to_string(index=False))


# --------------------------------------------------
# 5. Source-type distribution
# --------------------------------------------------

source_types = pd.read_sql_query(
    """
    SELECT
        source_type,
        COUNT(*) AS record_count
    FROM evidence
    GROUP BY source_type
    ORDER BY record_count DESC
    """,
    connection,
)

source_types["percentage"] = (
    source_types["record_count"]
    / source_types["record_count"].sum()
    * 100
).round(1)

print("\n=== SOURCE TYPE DISTRIBUTION ===")
print(source_types.to_string(index=False))


connection.close()

print("\nAnalysis complete.")