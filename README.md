# Mental Health App Evidence Tracker

A reproducible Python and SQLite research-data project for organizing, validating, querying, and analyzing structured evidence about mental health applications.

## Project Motivation

Mental health applications make a wide range of claims related to mental health support, clinical evidence, artificial intelligence, privacy, and wellbeing. Information relevant to evaluating these applications is often distributed across app stores, developer websites, privacy policies, terms of service, and peer-reviewed literature.

This project demonstrates a structured workflow for representing and analyzing that evidence while preserving the distinction between an app-level record and individual evidence observations.

## Project Scope

The current dataset contains:

- 14 mental health applications
- 36 structured evidence records
- multiple evidence domains including clinical evidence, privacy policy, AI disclosure, app/store metadata, terms of service, and health/wellbeing claims

The dataset is intended as a small research and software-development demonstration rather than a comprehensive assessment of the mental health app market.

## Data Model

The project uses two related datasets.

### Apps table

Each row represents one mental health application.

Primary key:

`app_id`

Example fields include:

- app name
- developer
- application category
- mental health focus
- official website
- AI disclosure status
- primary claims
- target population
- application status
- first identified date

### Evidence table

Each row represents one evidence observation associated with an application.

Primary key:

`evidence_id`

Foreign key:

`app_id -> apps.app_id`

Evidence fields include:

- source type
- source title and URL
- date checked
- version or release information
- finding domain
- finding status
- finding detail
- claim summary
- evidence strength
- notes

This structure supports a one-to-many relationship in which one application may have multiple evidence records.

## Evidence Representation

Clinical evidence is not represented as a simple yes/no field.

The evidence model distinguishes outcomes such as:

- evidence identified and relevant
- evidence identified but insufficient for the specified claim
- evidence identified but not directly applicable
- claim identified but supporting evidence not identified
- unclear or not assessable findings

This preserves uncertainty and avoids treating absence of identified evidence as proof that evidence does not exist.

## Workflow

The project implements the following reproducible pipeline:

```text
Raw CSV data
    |
    v
Data inspection
    |
    v
Data cleaning
    |
    v
Processed CSV data
    |
    v
Data validation
    |
    v
SQLite relational database
    |
    v
SQL queries
    |
    v
Pandas analysis
    |
    v
Matplotlib visualizations