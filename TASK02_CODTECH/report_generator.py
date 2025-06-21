import pandas as pd
from fpdf import FPDF

# Step 1: Read Excel file
df = pd.read_excel("data.xlsx")

# Step 2: Analyze
average_marks = df['Marks'].mean()
highest_scorer = df.loc[df['Marks'].idxmax(), 'Name']
lowest_scorer = df.loc[df['Marks'].idxmin(), 'Name']

# Step 3: Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')
pdf.ln(10)

pdf.cell(200, 10, txt=f"Total Students: {len(df)}", ln=True)
pdf.cell(200, 10, txt=f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Top Scorer: {highest_scorer}", ln=True)
pdf.cell(200, 10, txt=f"Lowest Scorer: {lowest_scorer}", ln=True)

pdf.ln(10)
pdf.cell(200, 10, txt="Full Data Table:", ln=True)

for index, row in df.iterrows():
    pdf.cell(200, 10, txt=f"{row['Name']} - {row['Marks']} marks", ln=True)

# Save PDF
pdf.output("marks_report.pdf")
print(" PDF report generated: marks_report.pdf")
