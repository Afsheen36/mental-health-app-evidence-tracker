import sqlite3

database_path = "database/evidence_tracker.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

print("=== DATABASE VERIFICATION ===")

cursor.execute("SELECT COUNT(*) FROM apps")
app_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM evidence")
evidence_count = cursor.fetchone()[0]

print("Apps in database:", app_count)
print("Evidence records in database:", evidence_count)

print("\n=== APPS ===")

cursor.execute("""
SELECT app_id, app_name, app_status
FROM apps
ORDER BY app_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

    print("\n=== ACTIVE APPS ===")

cursor.execute("""
SELECT app_id, app_name, app_status
FROM apps
WHERE app_status = 'Active'
ORDER BY app_name
""")

active_apps = cursor.fetchall()

for row in active_apps:
    print(row)

    print("\n=== APP STATUS SUMMARY ===")

cursor.execute("""
SELECT app_status, COUNT(*)
FROM apps
GROUP BY app_status
ORDER BY COUNT(*) DESC
""")

status_summary = cursor.fetchall()

for row in status_summary:
    print(row)

    print("\n=== APP + EVIDENCE JOIN ===")

cursor.execute("""
SELECT
    apps.app_name,
    evidence.evidence_id,
    evidence.finding_domain,
    evidence.finding_status
FROM apps
JOIN evidence
    ON apps.app_id = evidence.app_id
ORDER BY apps.app_name, evidence.evidence_id
""")

joined_rows = cursor.fetchall()

for row in joined_rows:
    print(row)

    print("\n=== EVIDENCE RECORDS PER APP ===")

cursor.execute("""
SELECT
    apps.app_name,
    COUNT(evidence.evidence_id) AS evidence_count
FROM apps
LEFT JOIN evidence
    ON apps.app_id = evidence.app_id
GROUP BY apps.app_id, apps.app_name
ORDER BY evidence_count DESC, apps.app_name
""")

for row in cursor.fetchall():
    print(row)


print("\n=== FINDING DOMAIN DISTRIBUTION ===")

cursor.execute("""
SELECT
    finding_domain,
    COUNT(*) AS record_count
FROM evidence
GROUP BY finding_domain
ORDER BY record_count DESC
""")

for row in cursor.fetchall():
    print(row)


print("\n=== CLINICAL EVIDENCE FINDINGS ===")

cursor.execute("""
SELECT
    apps.app_name,
    evidence.finding_status,
    evidence.evidence_strength,
    evidence.source_title
FROM evidence
JOIN apps
    ON evidence.app_id = apps.app_id
WHERE evidence.finding_domain = 'Clinical evidence'
ORDER BY apps.app_name
""")

for row in cursor.fetchall():
    print(row)


print("\n=== AI DISCLOSURE EVIDENCE ===")

cursor.execute("""
SELECT
    apps.app_name,
    evidence.source_type,
    evidence.finding_status,
    evidence.evidence_strength
FROM evidence
JOIN apps
    ON evidence.app_id = apps.app_id
WHERE evidence.finding_domain = 'AI disclosure'
ORDER BY apps.app_name
""")

for row in cursor.fetchall():
    print(row)
    
connection.close()