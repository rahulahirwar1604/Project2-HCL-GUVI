📄🔎 Resume Skill Extractor (Streamlit + OOP)

A Streamlit web app that extracts skills from resumes (PDF/TXT) and compares them with job-required skills. It highlights matched skills, missing skills, and calculates match percentage — making hiring easier and faster.

The project is built with a modular OOP design, making it easy to debug, extend, and maintain.

⸻
📂 Project Structure
Project2-HCL-GUVI/
│── app.py                # Entry point (Streamlit main file)
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
│
├── core/                  # Core business logic
│   ├── __init__.py
│   ├── parsers.py         # ResumeParser + FileReaders
│   ├── skills.py          # SkillRepository + SkillExtractor
│   ├── matcher.py         # JDMatcher
│   ├── report.py          # ReportBuilder
│   └── utils.py           # TextNormalizer
│
├── models/                # Domain models
│   ├── __init__.py
│   └── resume_result.py   # ResumeResult dataclass
│
└── ui/                    # Streamlit UI logic
    ├── __init__.py
    └── app_ui.py          # ResumeSkillApp (UI Orchestration)

    ⚙️ Requirements

Python Version
	•	Python 3.9+ (recommended 3.10 or 3.11)

Dependencies

Installed via requirements.txt:
streamlit>=1.36.0
pandas>=2.0.0
PyPDF2>=3.0.0
rapidfuzz>=3.0.0

Optional Extras
	•	python-docx → Add support for .docx resumes
	•	spacy → Advanced NLP-based skill extraction
	•	matplotlib / seaborn → Custom charts

⸻

🚀 Setup Instructions
	1.	Clone the Repository
    git clone <your-repo-url>
    cd resume-skill-extractor

    2.	Create Virtual Environment (recommended)
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows

    3.	Install Requirements
    pip install -r requirements.txt

    ▶️ Run the App
    streamlit run app.py


🖥️ How to Use
	1.	Upload Resumes → Select one or more resumes (PDF/TXT).
	2.	Enter Job Skills → Type comma-separated skills (e.g., Python, SQL, Machine Learning, AWS).
	3.	Click Extract & Match → The app will parse, extract skills, and compare.
	4.	View Results → See matched/missing skills, match percentage, and a summary table.
	5.	Download Report → Export results as CSV.


🔧 Features
	•	Upload multiple resumes (PDF/TXT)
	•	Customizable skills list (via CSV or text input)
	•	Exact + fuzzy matching (RapidFuzz)
	•	Match percentage calculation
	•	Downloadable CSV report
	•	Clean Streamlit interface with charts

