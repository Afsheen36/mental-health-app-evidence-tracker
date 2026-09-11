import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

database_path = "database/evidence_tracker.db"
connection = sqlite3.connect(database_path)


# ------------------------------------------
# Figure 1: Finding-domain distribution
# ------------------------------------------

domains = pd.read_sql_query(
    """
    SELECT finding_domain, COUNT(*) AS record_count
    FROM evidence
    GROUP BY finding_domain
    ORDER BY record_count ASC
    """,
    connection,
)

plt.figure(figsize=(9, 5))
plt.barh(domains["finding_domain"], domains["record_count"])
plt.xlabel("Number of evidence records")
plt.ylabel("Finding domain")
plt.title("Distribution of Evidence Domains")
plt.tight_layout()
plt.savefig(
    "outputs/figures/finding_domain_distribution.png",
    dpi=300
)
plt.close()


# ------------------------------------------
# Figure 2: Clinical evidence assessment
# ------------------------------------------

clinical = pd.read_sql_query(
    """
    SELECT finding_status, COUNT(*) AS record_count
    FROM evidence
    WHERE finding_domain = 'Clinical evidence'
    GROUP BY finding_status
    ORDER BY record_count ASC
    """,
    connection,
)

plt.figure(figsize=(10, 5))
plt.barh(clinical["finding_status"], clinical["record_count"])
plt.xlabel("Number of clinical-evidence records")
plt.ylabel("Assessment")
plt.title("Clinical Evidence Assessment")
plt.tight_layout()
plt.savefig(
    "outputs/figures/clinical_evidence_assessment.png",
    dpi=300
)
plt.close()


# ------------------------------------------
# Figure 3: Evidence coverage by app
# ------------------------------------------

coverage = pd.read_sql_query(
    """
    SELECT
        apps.app_name,
        COUNT(evidence.evidence_id) AS evidence_count
    FROM apps
    LEFT JOIN evidence
        ON apps.app_id = evidence.app_id
    GROUP BY apps.app_id, apps.app_name
    ORDER BY evidence_count ASC
    """,
    connection,
)

plt.figure(figsize=(10, 7))
plt.barh(coverage["app_name"], coverage["evidence_count"])
plt.xlabel("Number of evidence records")
plt.ylabel("Application")
plt.title("Evidence Records per Mental Health Application")
plt.tight_layout()
plt.savefig(
    "outputs/figures/evidence_records_per_app.png",
    dpi=300
)
plt.close()


connection.close()

print("Figures created:")
print("- finding_domain_distribution.png")
print("- clinical_evidence_assessment.png")
print("- evidence_records_per_app.png")