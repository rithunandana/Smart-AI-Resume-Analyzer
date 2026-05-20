# app.py
import streamlit as st
from resume_analytics.analyzer import ResumeAnalyzer
from PyPDF2 import PdfReader
import docx

# --- 1. Define your Job Categories, Roles & Requirements ---
job_catalog = {
    "Project Management": {
        "Project Manager": {
            "description": "Lead and manage project delivery",
            "skills": {"project planning", "agile", "scrum", "risk management", "stakeholder management"}
        },
        "Scrum Master": {
            "description": "Facilitate Agile ceremonies and remove blockers",
            "skills": {"scrum", "agile", "servant leadership", "jira", "facilitation"}
        }
    },
    "Data & AI": {
        "Data Scientist": {
            "description": "Build models to extract insights from data",
            "skills": {"python", "machine learning", "data science", "analytics", "sql"}
        },
        "AI Engineer": {
            "description": "Productionize machine learning models",
            "skills": {"python", "tensorflow", "deep learning", "docker", "kubernetes"}
        },
        "Data Analyst": {
            "description": "Analyze and visualize data to support decision-making",
            "skills": {"excel", "sql", "data visualization", "python", "tableau"}
        },
        "Business Intelligence Analyst": {
            "description": "Use data to inform business decisions",
            "skills": {"sql", "tableau", "data modeling", "data analysis", "power bi"}
        }
    },
    "Web Development": {
        "Frontend Developer": {
            "description": "Build user-facing web applications",
            "skills": {"html", "css", "javascript", "react", "typescript"}
        },
        "Backend Developer": {
            "description": "Design and build server-side applications",
            "skills": {"python", "node.js", "sql", "docker", "cloud computing"}
        },
        "Full Stack Developer": {
            "description": "Work on both front-end and back-end development",
            "skills": {"html", "css", "javascript", "react", "node.js", "python", "sql"}
        }
    },
    "Software Engineering": {
        "Software Engineer": {
            "description": "Design, develop, and maintain software systems",
            "skills": {"python", "java", "c++", "algorithm design", "problem-solving"}
        },
        "Systems Engineer": {
            "description": "Build and maintain IT systems and infrastructure",
            "skills": {"linux", "windows", "networking", "system administration", "cloud services"}
        },
        "DevOps Engineer": {
            "description": "Bridge development and operations to automate and streamline systems",
            "skills": {"docker", "kubernetes", "ci/cd", "aws", "linux", "terraform"}
        }
    },
    "Cybersecurity": {
        "Cybersecurity Analyst": {
            "description": "Protect systems and networks from cyber threats",
            "skills": {"network security", "firewalls", "incident response", "ethical hacking", "siem"}
        },
        "Security Engineer": {
            "description": "Develop and implement security systems",
            "skills": {"network security", "firewalls", "cloud security", "vulnerability management"}
        },
        "Penetration Tester": {
            "description": "Test systems for vulnerabilities and weaknesses",
            "skills": {"ethical hacking", "penetration testing", "network security", "linux"}
        }
    },
    "Marketing": {
        "Digital Marketing Specialist": {
            "description": "Manage online marketing campaigns and strategies",
            "skills": {"SEO", "PPC", "email marketing", "content marketing", "google analytics"}
        },
        "SEO Specialist": {
            "description": "Optimize website content for search engines",
            "skills": {"SEO", "google analytics", "keyword research", "on-page SEO", "link building"}
        },
        "Content Marketing Manager": {
            "description": "Oversee content creation and marketing strategy",
            "skills": {"content writing", "social media", "SEO", "email marketing", "copywriting"}
        }
    },
    "Finance & Accounting": {
        "Financial Analyst": {
            "description": "Analyze financial data and create reports for business decisions",
            "skills": {"excel", "financial modeling", "accounting", "forecasting", "budgeting"}
        },
        "Accountant": {
            "description": "Prepare financial statements and ensure compliance",
            "skills": {"bookkeeping", "financial reporting", "accounting software", "tax preparation"}
        },
        "Investment Banker": {
            "description": "Provide financial advice and services related to mergers, acquisitions, and capital markets",
            "skills": {"financial modeling", "valuation", "M&A", "capital raising", "equity analysis"}
        }
    },
    "Sales & Business Development": {
        "Sales Manager": {
            "description": "Lead a sales team to achieve revenue targets",
            "skills": {"sales strategy", "negotiation", "lead generation", "customer relationship management"}
        },
        "Business Development Manager": {
            "description": "Identify and develop new business opportunities",
            "skills": {"sales", "business strategy", "market research", "client acquisition"}
        },
        "Account Executive": {
            "description": "Manage client accounts and drive sales",
            "skills": {"sales", "customer service", "client relations", "negotiation"}
        }
    }
}

# --- 2. Helpers to read PDF / DOCX ---
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join(para.text for para in doc.paragraphs)

# --- 3. Streamlit UI ---
st.set_page_config(page_title="Smart AI Resume Analyzer", layout="wide")
st.title("📄 Smart AI Resume Analyzer")

# Step 1: Category & Role
st.markdown("**1. Select a job category and target role**")
category = st.selectbox("Job Category", options=["▶ Select category"] + list(job_catalog.keys()))
role = None
if category and category != "▶ Select category":
    role = st.selectbox("Target Job Role", options=["▶ Select role"] + list(job_catalog[category].keys()))

# Display Requirements
if role and role != "▶ Select role":
    req = job_catalog[category][role]
    st.markdown("### View Job Role Requirements")
    st.markdown(f"**{role}**\n\n{req['description']}")
    st.markdown(f"**Key Skills Required:**  {', '.join(sorted(req['skills']))}")

st.markdown("---")
st.markdown("**2. Upload your resume (PDF or DOCX)**")
uploaded = st.file_uploader("Drag and drop file here", type=["pdf", "docx"], accept_multiple_files=False)

# Step 3: Process Upload
if uploaded and role and role != "▶ Select role":
    # Extract text
    if uploaded.type == "application/pdf":
        resume_text = read_pdf(uploaded)
    else:
        resume_text = read_docx(uploaded)

    # Preview
    st.subheader("📝 Extracted Resume Text")
    st.text_area("", resume_text, height=200)

    # Core analysis
    analyzer = ResumeAnalyzer()
    base = analyzer.analyze_resume(resume_text)

    # Role-specific matching
    req_skills = job_catalog[category][role]["skills"]
    ext_skills = set(base["skills"])
    matched = ext_skills & req_skills
    missing = req_skills - ext_skills

    # Attach to result
    base["for_role"] = {
        "role": role,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }

    # === Display nicely ===
    st.subheader("✅ Resume Analysis Results")
    st.markdown(f"**Profile Summary**")
    st.markdown(f"- 🔑 **Word Count**: {base['metrics']['word_count']}")
    st.markdown(f"- 📝 **Sentence Count**: {base['metrics']['sentence_count']}")
    st.markdown(f"- 💼 **Experience Years**: {base['metrics']['experience_years']}")
    st.markdown(f"- 🧠 **Profile Score**: {base['metrics']['profile_score']} / 100")

    st.markdown("---")
    st.markdown("### 🎯 Role-Specific Skills Match")
    st.markdown(f"- **Matched Skills:**  {', '.join(sorted(matched)) or 'None'}")
    st.markdown(f"- **Missing Skills:**  {', '.join(sorted(missing)) or 'None'}")

    st.markdown("---")
    st.markdown("### 💡 General Suggestions")
    for sug in base["suggestions"]:
        st.markdown(f"- {sug['text']}")

    st.markdown("---")
    st.subheader("🎯 Other Job Recommendations")
    # Show other roles you’ve coded in analyzer
    for jr in base["job_recommendations"]:
        st.markdown(f"**{jr['job']}**")
        st.markdown(f"  - Matched: {', '.join(jr['matched_skills'])}")
        st.markdown(f"  - Missing: {', '.join(jr['missing_skills'])}")

elif uploaded:
    st.warning("Please select a Job Category and Target Role before uploading.")

