# Customer Data Pipeline

This project demonstrates a Python-based CI/CD data pipeline for generating, transforming, validating, and deploying customer profile data.  
It automates CSV-to-JSON transformation, enforces data validation, and deploys a static web application to GitHub Pages.

---

## Project Overview

The project simulates a production scenario where customer data is generated, processed, and served through a web application.  
The application reads customer data from a `data.json` file, which is produced and validated as part of the pipeline.

The solution includes:
- profile data generation
- CSV to JSON transformation
- automated validation tests
- CI/CD-based deployment to GitHub Pages

---

## Features

- CSV to JSON transformation using Python
- Automated validation of both input and output data
- Unit testing with `unittest`
- CI/CD pipeline built with GitHub Actions
- Automatic deployment to GitHub Pages
- Static frontend powered by `index.html`, `script.js`, and `data.json`

---

## CI/CD Workflow

The GitHub Actions pipeline performs the following steps:

1. Checks out the repository  
2. Sets up Python  
3. Installs dependencies  
4. Runs `generate.py`  
5. Runs `csvtojson.py`  
6. Executes unit tests (pipeline fails on errors)  
7. Prepares deployment artifacts  
8. Uploads build artifacts  
9. Deploys the application to GitHub Pages  

---

## Validation Tests

The test suite ensures data quality by verifying that:

- the CSV file contains exactly 12 columns  
- the CSV file contains more than 900 rows  
- the JSON file contains more than 900 objects  
- each JSON object contains all expected properties  
- the CI/CD pipeline can execute at least one guaranteed passing test  

Expected JSON properties:
- Givenname  
- Surname  
- Streetaddress  
- City  
- Zipcode  
- Country  
- CountryCode  
- NationalId  
- TelephoneCountryCode  
- Telephone  
- Birthday  
- ConsentToContact  

---

## Technical Highlights

- Built using Python  
- CSV parsing using the built-in `csv` module  
- JSON generation using the built-in `json` module  
- Automated testing with `unittest`  
- CI/CD pipeline implemented with GitHub Actions  
- Static deployment via GitHub Pages  
- Validation-first pipeline design to ensure data quality  
- Fail-fast strategy to prevent invalid deployments  

---

## Project Files

- `generate.py` – generates profile data  
- `csvtojson.py` – converts `profiles1.csv` into `data.json`  
- `tests/` – validation tests for CSV and JSON output  
- `index.html` – frontend page  
- `script.js` – frontend logic for displaying customer data  
- `data.json` – generated dataset used by the application  
- `.github/workflows/` – CI/CD workflow configuration  

---

## CI/CD

The pipeline is triggered on:
- push to `main`  
- pull requests targeting `main`  

Pull requests validate changes before merging, while pushes to `main` trigger deployment.  
The pipeline is configured to fail on any test error, ensuring only validated data is deployed.

---

## Documentation

This project demonstrates practical application of CI/CD principles, data validation, and automated deployment workflows in a data engineering context.
