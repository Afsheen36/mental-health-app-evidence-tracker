# Data Dictionary

## Purpose

This document defines the structure, meaning, and interpretation of fields used in the Mental Health App Evidence Tracker.

The project uses publicly available information about mental health and wellbeing applications. Raw data should not be interpreted as independently verified evidence of clinical effectiveness, safety, privacy quality, or regulatory compliance.

## Core Data Principles

- Developer or app claims are recorded as claims, not researcher conclusions.
- "Not identified in sources examined" does not mean that something does not exist.
- Missing information is different from evidence of absence.
- `date_checked` records when a source was examined and is different from a publication, release, or update date.
- Raw data are preserved unchanged. Corrections and standardization will be performed reproducibly during data processing.

---

## apps.csv

**Unit of observation:** One row represents one distinct app/product.

| Field | Type | Required | Description |
|---|---|---|---|
| `app_id` | Text | Yes | Unique project-assigned identifier for an app, such as `APP001`. |
| `app_name` | Text | Yes | Current app/product name identified from public sources. |
| `developer` | Text | Yes | Developer, company, or organization associated with the app. |
| `app_category` | Text | Yes | Standardized broad category assigned to the app. |
| `mental_health_focus` | Text | Yes | Main mental-health or wellbeing areas addressed by the app. |
| `official_website_url` | Text/URL | No | Official website for the app or developer. |
| `app_description_summary` | Text | Yes | Neutral summary of the app's publicly described functionality. |
| `ai_disclosure_status` | Categorical text | Yes | Whether explicit AI use was identified in the sources examined. |
| `ai_claim_summary` | Text | No | Neutral summary of explicit AI-related claims. |
| `primary_claims` | Text | No | Major health or wellbeing claims made by the app/developer. |
| `target_population` | Text | No | Population explicitly described as the intended audience. |
| `app_status` | Categorical text | Yes | Observed availability/status of the app. |
| `first_identified_date` | Date | Yes | Date the app was first recorded for this portfolio dataset. |

### Controlled values

#### `ai_disclosure_status`

- `Explicitly disclosed`
- `Not identified in sources examined`
- `Unclear`
- `Not assessed`

`Not identified in sources examined` must not be interpreted as evidence that the app does not use AI.

#### `app_status`

Proposed processed-data values:

- `Active`
- `Retired`
- `Unavailable`
- `Unclear`

`Retired` means that an authoritative source indicates that the product was intentionally discontinued or retired.

Raw values are preserved in `data/raw/`; standardized values may differ after verification and cleaning.