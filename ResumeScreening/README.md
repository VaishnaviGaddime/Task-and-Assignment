# Resume Screening System

Streamlit-based Resume Screening System that supports:

- User signup and login with SQLite
- Multiple resume upload (PDF, DOCX, TXT)
- Skill extraction from resumes
- Job role specific required skills input
- Resume score calculation
- Candidate contact detail extraction (email, phone)
- Data analysis with Pandas & NumPy (tables, summary stats, top candidates)
- Simple ML-based shortlist prediction using Logistic Regression

## Project Structure

- `app.py` – main Streamlit application
- `parser.py` – PDF/DOCX text extraction
- `skills.py` – skill extraction from resume text
- `scoring.py` – resume score calculation
- `contact.py` – email and phone extraction
- `database.py` – SQLite user table and helpers
- `auth.py` – signup/login helpers
- `analytics.py` – Pandas/NumPy analytics utilities
- `ml_model.py` – Logistic Regression shortlist model

## Setup

```bash
cd "Resume Screening System/ResumeScreening"
pip install -r requirements.txt
```

This project uses SQLite, which is included with Python (no extra install needed).

## Run

```bash
streamlit run app.py
```

Open the URL shown in the terminal to use the app.

