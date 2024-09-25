import os
import PyPDF2
import google.generativeai as genai
from fpdf import FPDF

os.environ["API_KEY"] = "api_key"
genai.configure(api_key=os.environ["API_KEY"])

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
    return text

def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Summarize the following text: {text}")
    return response.text

def create_pdf(summary, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.output(output_path)

pdf_path = 'enter some relative path/ PATH of the pdf'
output_path = 'summary_output.pdf'  # Path to save the summary PDF

text = extract_text_from_pdf(pdf_path)
summary = summarize_text(text)

create_pdf(summary, output_path)
print(f"Summary saved as {output_path}.")
