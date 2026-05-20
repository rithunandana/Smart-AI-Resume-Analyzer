# Smart AI Resume Analyzer

An AI-powered resume analysis platform that helps users evaluate, improve, and optimize their resumes for specific job roles using intelligent resume parsing, ATS-style scoring, and personalized recommendations.

## Features

- Resume upload and analysis (PDF/DOCX support)
- ATS-style resume scoring
- Job role compatibility matching
- Skill gap analysis
- AI-powered resume feedback and improvement suggestions
- Resume parsing and information extraction
- Resume builder support
- Resume analytics dashboard with visual insights
- Admin/user management functionality
- OCR support for scanned resumes
- Export reports and analytics

## Tech Stack

**Frontend**
- Streamlit

**Backend**
- Python

**Libraries & Tools**
- Pandas
- NumPy
- Scikit-learn
- NLTK
- SpaCy
- PyPDF2
- pdfplumber
- pytesseract
- pdf2image
- Selenium
- SQLAlchemy
- Plotly
- Matplotlib
- Seaborn
- Google Generative AI API

## Project Structure

```bash
Smart-AI-Resume-Analyzer/
│
├── app.py                    # Main Streamlit application
├── main.py                   # Application entry point
├── requirements.txt          # Project dependencies
├── sample_resume.pdf         # Sample resume for testing
│
├── resume_analytics/
│   └── analyzer.py          # Resume analytics engine
│
├── utils/
│   ├── ai_resume_analyzer.py
│   ├── database.py
│   ├── excel_manager.py
│   ├── resume_analyzer.py
│   ├── resume_builder.py
│   └── resume_parser.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Smart-AI-Resume-Analyzer.git
cd Smart-AI-Resume-Analyzer
```

### 2. Create a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your API keys:

```env
GOOGLE_API_KEY=your_api_key_here
OPENROUTER_API_KEY=your_api_key_here
```

## Run the Application

```bash
streamlit run app.py
```

Then open:

```bash
http://localhost:8501
```

## How It Works

1. Upload your resume (PDF/DOCX)
2. Select the target job role
3. The system parses your resume
4. Skills, keywords, and experience are analyzed
5. ATS compatibility score is generated
6. AI provides suggestions to improve your resume

## Use Cases

- Students preparing for placements
- Job seekers optimizing resumes
- Career counselors
- Recruiters for quick resume screening

## Future Enhancements

- LinkedIn profile analysis
- Real-time job recommendations
- Cover letter generation
- Multi-language resume support
- Resume benchmarking against industry standards

## Screenshots

Add application screenshots here.

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

