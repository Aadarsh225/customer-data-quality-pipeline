# Customer Data Quality Pipeline

## Overview
This project is a mini data engineering and data quality pipeline built using Python, MongoDB, and Great Expectations.

It focuses on cleaning messy transaction data, loading it into a database, running queries, and validating data quality.

---

## Tech Stack
- Python
- Pandas
- MongoDB
- Great Expectations
- Git / GitHub

---

## Project Structure
customer-data-quality/
│── data/
│   └── transactions.csv
│── output/
│   └── clean_transactions.csv
│── etl.py
│── gx_validation.py
│── mongo.mongodb.js
│── requirements.txt
│── README.md

---

## Features

### 1. ETL Pipeline
- Extract transaction data from CSV
- Remove duplicates
- Handle missing values
- Fix invalid amounts
- Standardize columns
- Create fraud flag

### 2. MongoDB Operations
- Insert cleaned transaction data
- Query fraud transactions
- Aggregate transaction amount
- Filter suspicious customers

### 3. Great Expectations Validation
- Unique transaction_id validation
- Null checks
- Amount range validation
- Payment method validation
- Email / phone pattern checks
- Row count checks
- Fraud flag validation

---

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt