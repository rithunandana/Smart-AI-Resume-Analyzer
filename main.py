from resume_analytics.analyzer import ResumeAnalyzer
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()
    return resume_text

if __name__ == "__main__":
    analyzer = ResumeAnalyzer()

    # Extract resume text from the PDF
    resume_text = extract_text_from_pdf("sample_resume.pdf")  # Replace with your resume file

    # Analyze the resume
    analysis_result = analyzer.analyze_resume(resume_text)

    # Print the analysis result
    print(analysis_result)
