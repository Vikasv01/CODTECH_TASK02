#  Automated PDF Report Generator (Task 02 - CODTECH Python Internship)

This project is part of **Task 02** of the **CODTECH Python Internship**. It reads student data from an Excel file, performs simple analysis, and generates a formatted **PDF report** using Python.

---

##  Technologies Used

- **Python 3.11+**
- **pandas** – for reading and analyzing Excel data
- **fpdf** – for creating PDF reports

---

##  Objective

> Read data from a file, analyze it (average, highest and lowest scorer), and generate a PDF report automatically.

---

##  How to Run

### 1. Clone the Repository


git clone https://github.com/your-username/task02-report-generator.git
cd task02-report-generator

### 2.  Install Required Packages

pip install pandas fpdf openpyxl

### 3. File Structure

📁 TASK02_CODTECH/
├── data.xlsx         # Input Excel file with student names and marks
├── report_generator.py   # Main Python script
├── marks_report.pdf      # Output PDF report (generated after running the script)
└── README.md

### 4. Run the Script

python report_generator.py

If successful, the script will print:
PDF report generated: marks_report.pdf

---


