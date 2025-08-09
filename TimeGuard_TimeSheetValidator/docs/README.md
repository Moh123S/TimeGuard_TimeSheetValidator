ASSIGNMENT:
https://docs.google.com/document/d/1v142ZELMdSiEf0OVSV-dVRdObwEK_cW4FJYkw-6ywPs/edit?usp=drive_link

TimeGuard - Timesheet Validator
Project Overview
The "TimeGuard - Timesheet Validator" is a web-based application built with Python using the Flask framework. It compares timesheet CSV files with calendar events and flags discrepancies, such as missing events or incorrect hours. This document provides a step-by-step guide to the development process and setup instructions.
Development Journey
Step 1: Initial Project Structure
The project started with a well-organized directory structure to manage the code efficiently:

src/: Contains source code (config, utils, services, app).
tests/: For unit and integration tests.
docs/: For documentation (e.g., README.md, prompt.log).
src/static/: Stores sample data files (e.g., CSV, JSON).
src/templates/: Holds HTML templates for the web interface.
Root files: requirements.txt, .gitignore, .env (optional), run.py.

Step 2: Setting Up the Environment

Dependencies were managed using requirements.txt, listing Python packages like Flask, pandas, and python-dateutil.
A virtual environment (venv) was set up to isolate dependencies, activated with .\venv\Scripts\activate on Windows.

Step 3: Core Functionality Implementation
The application was built incrementally:

CSV Parsing: Created src/utils/csv_parser.py to read timesheet CSV files using pandas.
Date Utilities: Added src/utils/date_utils.py for date comparisons with python-dateutil.
Calendar Service: Implemented src/services/calendar_service.py to fetch mock calendar data from src/static/mock_calendar.json.
Validation Service: Developed src/services/validation_service.py to compare timesheets with calendar events, flagging discrepancies (e.g., hours ≠ 8).
Routes: Set up src/app/routes.py to handle file uploads and return validation reports using Flask.
Dashboard: Created src/templates/index.html with basic HTML and JavaScript for uploading CSV files and displaying results.

Step 4: Data and Templates

Added src/static/sample_timesheet.csv and src/static/mock_calendar.json as sample data.
Designed src/templates/index.html for the user interface.

Step 5: Running the Project

The application is run with python src/run.py after navigating to the project root (D:\Intern_P\TimeGuard_TimeSheetValidator).
The server starts on http://localhost:5000, accessible via a web browser.

Step 6: Troubleshooting

Resolved a ModuleNotFoundError: No module named 'src' by ensuring the script runs from the project root or modifying src/run.py to adjust the import path with sys.path.
Fixed a cd command syntax error (cd cd ...) by correcting it to cd D:\Intern_P\TimeGuard_TimeSheetValidator.

Step 7: Finalizing with .gitignore

Added .gitignore to exclude __pycache__, uploads/, .env, and *.log files from version control, keeping the repository clean.

Setup Instructions

Install Dependencies:
Navigate to the project root: cd D:\Intern_P\TimeGuard_TimeSheetValidator.
Activate the virtual environment: .\venv\Scripts\activate (Windows).
Install dependencies: pip install -r requirements.txt.


Run the Application:
Start the server: python src/run.py.
Open http://localhost:5000 in a browser.


Test:
Upload src/static/sample_timesheet.csv and verify the validation report.



Constraints

Used only free libraries (e.g., Flask, pandas) and mock data instead of free-tier APIs.

Result:
![alt text](<Screenshot 2025-08-09 110500.png>)