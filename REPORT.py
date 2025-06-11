import pandas as pd
from fpdf import FPDF

# Step 1: Read data from  the CSV file
df = pd.read_csv('data.csv')

# Step 2: Analyze the data (example: basic statistics)
average_score = df['Score'].mean()
highest_score = df['Score'].max()
lowest_score = df['Score'].min()

# Step 3: Create a PDF report from
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Student Score Report', ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_summary(self, avg, high, low):
        self.set_font('Arial', '', 12)
        self.ln(10)
        self.cell(0, 10, f'Average Score: {avg:.2f}', ln=True)
        self.cell(0, 10, f'Highest Score: {high}', ln=True)
        self.cell(0, 10, f'Lowest Score: {low}', ln=True)

    def add_table(self, dataframe):
        self.ln(10)
        self.set_font('Arial', 'B', 12)
        self.cell(60, 10, 'Name', border=1)
        self.cell(40, 10, 'Score', border=1)
        self.ln()

        self.set_font('Arial', '', 12)
        for index, row in dataframe.iterrows():
            self.cell(60, 10, row['Name'], border=1)
            self.cell(40, 10, str(row['Score']), border=1)
            self.ln()

# Step 4: Generate  PDF
pdf = PDFReport()
pdf.add_page()
pdf.add_summary(average_score, highest_score, lowest_score)
pdf.add_table(df)
pdf.output("report.pdf")

print("PDF report generated as 'report.pdf'")