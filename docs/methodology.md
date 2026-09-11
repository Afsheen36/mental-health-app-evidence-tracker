# Methodology

## Overview

The Mental Health App Evidence Tracker is a small, purposively assembled research dataset and reproducible software workflow for organizing structured information about mental health applications and the evidence sources associated with them.

The project was designed primarily as a research-software and biomedical-informatics demonstration. It should not be interpreted as a systematic review, clinical guideline, regulatory assessment, or comprehensive evaluation of the mental health app market.

## Unit of Observation

The project contains two related units of observation.

### Application records

Each row in `apps.csv` represents one distinct mental health application or product.

Applications are assigned project-specific identifiers such as `APP001`.

### Evidence records

Each row in `evidence.csv` represents one structured observation from a source examined in relation to an application.

Evidence records are assigned project-specific identifiers such as `EV001`.

Multiple evidence records may therefore be associated with a single application.

The relationship is:

`apps.app_id -> evidence.app_id`

This produces a one-to-many relational structure.

## Application Selection

The current dataset contains a small purposively assembled sample of mental health and wellbeing applications.

Applications were included to support development and testing of the evidence-tracking workflow and to provide variation in areas such as mental health focus, application characteristics, AI-related claims, and availability of public evidence.

The current set should not be interpreted as a representative sample of all mental health applications.

## Sources

Information was structured from publicly accessible sources relevant to the applications examined.

Source categories represented in the dataset include:

- official application or developer websites
- Apple App Store listings
- Google Play listings
- privacy policies
- terms of service
- peer-reviewed literature
- other authoritative public sources

Each evidence record retains source-level information, including a source title, source type, URL, and date checked where applicable.

This allows app-level metadata to remain separate from individual evidence observations.

## Evidence Domains

Evidence observations are classified into domains relevant to evaluating mental health applications.

Domains represented in the current dataset include:

- clinical evidence
- privacy policy
- AI disclosure
- app/store metadata
- terms of service
- health/wellbeing claims

These domains organize the type of question addressed by an evidence record rather than imply the quality of the evidence itself.

## Finding Status

Finding status is designed to preserve distinctions that would be lost in a simple yes/no evidence variable.

Depending on the evidence domain and source examined, classifications may include:

- `Identified`
- `Claim identified but supporting evidence not identified`
- `Evidence identified and relevant`
- `Evidence identified but insufficient for specified claim`
- `Evidence identified but not directly applicable`
- `Unclear`

These classifications describe the result of examining the recorded sources under the operational definitions used in this project.

## Interpretation of Evidence Absence

A central methodological principle of this project is that failure to identify evidence is not equivalent to demonstrating that evidence does not exist.

For example:

`Claim identified but supporting evidence not identified`

means that a claim was observed, but supporting evidence was not identified in the sources examined for that record.

It should not be interpreted as:

`No supporting evidence exists anywhere.`

Similarly, `Not identified in sources examined` describes the scope of the search or observation rather than establishing universal absence.

## Evidence Strength

The `evidence_strength` field provides a structured description of the relationship between the recorded source and the finding.

Categories used in the current dataset include:

- direct primary source
- direct peer-reviewed evidence
- indirect/supporting evidence
- insufficient to assess

Evidence-strength categories are project-level classifications intended to support structured comparison. They are not equivalent to formal clinical evidence-grading systems.

## Observed and Researcher-Assigned Information

The dataset contains both source-derived information and structured classifications.

Examples of primarily source-derived information include:

- application name
- developer
- source URL
- source title
- application descriptions
- publicly stated claims
- observed application or policy information

Examples of researcher-assigned or project-structured fields include:

- project identifiers
- finding domain
- finding status
- evidence strength
- standardized summaries
- selected categorical labels

This distinction is important because structured classifications represent interpretation under the project's operational framework rather than statements copied directly from the source.

## Missing Information

Missing information is distinguished from information that is not applicable.

Where a source did not specify information that could reasonably have been present, the processed dataset may represent that value as missing.

Where a field does not conceptually apply to a particular evidence record, it may be represented separately as not applicable.

This distinction prevents missingness from being interpreted as a substantive negative finding.

## Data Processing

The reproducible workflow separates raw and processed data.

`data/raw/` contains the original project input datasets.

`src/clean_data.py` performs documented transformations and generates cleaned files in:

`data/processed/`

The raw input files are not overwritten by the cleaning script.

## Validation

`src/validate_data.py` performs computational validation of the processed datasets.

Checks include:

- missing required identifiers
- duplicate primary identifiers
- app-to-evidence referential integrity
- controlled vocabulary consistency
- required-field completeness
- date validity

A successful validation result means that the processed data satisfy the implemented computational rules.

It does not independently verify the factual accuracy, clinical validity, or completeness of the underlying sources.

## Relational Database

Validated processed data are loaded into a SQLite database.

The database contains two principal tables:

- `apps`
- `evidence`

`app_id` functions as the primary key of the apps table and as a foreign key in the evidence table.

This allows multiple evidence observations to be associated with one application while avoiding unnecessary duplication of app-level metadata.

## Analysis

SQL queries are used to examine relationships and aggregate evidence records.

Pandas is used for additional descriptive analysis, including counts and percentages.

Matplotlib is used to generate visual summaries of:

- evidence-domain distribution
- clinical-evidence assessments
- evidence coverage across applications

The analyses are descriptive and exploratory.

## Limitations

The current version has several important limitations.

1. The application sample is small and purposively assembled rather than systematically sampled.
2. Evidence coverage is not necessarily equivalent across applications.
3. Publicly available app information, policies, product features, and app-store listings can change over time.
4. Source availability may differ across applications.
5. Failure to identify evidence in the sources examined does not establish evidence absence.
6. Structured classifications depend on the operational definitions and interpretation used in this project.
7. The dataset is not intended to provide clinical recommendations or definitive assessments of application effectiveness or safety.
8. The current evidence search should not be interpreted as a systematic review unless a future version implements and documents a formal systematic-search protocol.

## Future Development

Potential extensions include:

- larger and more systematically selected application samples
- formalized search strategies
- independent duplicate evidence classification
- inter-rater agreement assessment
- longitudinal tracking of application and policy changes
- expanded evidence-quality frameworks
- automated source-update monitoring

These extensions would move the project from a portfolio-scale evidence-tracking demonstration toward a more formal research infrastructure.