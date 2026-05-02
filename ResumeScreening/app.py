import streamlit as st
from parser import extract_text_from_pdf, extract_text_from_docx
from skills import extract_skills
from scoring import calculate_resume_score
from contact import extract_email, extract_phone
from auth import signup_user, login_user
from database import create_users_table
from analytics import (
    create_candidate_dataframe,
    calculate_score_statistics,
    get_top_candidates,
)
from ml_model import train_shortlist_model, predict_candidate_status


st.set_page_config(page_title="Resume Screening System", layout="wide")

create_users_table()
model = train_shortlist_model()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = ""


def login_page() -> None:
    st.title("Resume Screening System")
    st.subheader("Login Page")

    username = st.text_input("Enter Username", key="login_username")
    password = st.text_input(
        "Enter Password", type="password", key="login_password"
    )

    if st.button("Login"):
        if login_user(username, password):
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.rerun()
        else:
            st.error("Invalid Username or Password")


def signup_page() -> None:
    st.title("Resume Screening System")
    st.subheader("Signup Page")

    username = st.text_input("Create Username", key="signup_username")
    password = st.text_input(
        "Create Password", type="password", key="signup_password"
    )

    if st.button("Signup"):
        success, message = signup_user(username, password)
        if success:
            st.success(message)
        else:
            st.error(message)


def main_app() -> None:
    st.title("Resume Screening System")
    st.header("AI Powered Resume Screening")
    st.write(f"Welcome, {st.session_state.current_user}")

    st.sidebar.title("Navigation")

    option = st.sidebar.selectbox(
        "Select Option",
        ["Upload Resume", "Screen Candidates", "View Results"],
    )

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = ""
        st.rerun()

    job_skills_input = st.text_input(
        "Enter Required Skills",
        "Python, SQL, Machine Learning, NLP",
    )

    required_skills = [
        skill.strip()
        for skill in job_skills_input.split(",")
        if skill.strip()
    ]

    uploaded_files = st.file_uploader(
        "Upload Resumes",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True,
    )

    candidate_data: list[dict] = []

    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.markdown("---")
            st.subheader(f"Processing Resume: {uploaded_file.name}")

            file_name = uploaded_file.name.lower()

            if file_name.endswith(".pdf"):
                resume_text = extract_text_from_pdf(uploaded_file)
            elif file_name.endswith(".docx"):
                resume_text = extract_text_from_docx(uploaded_file)
            else:
                resume_text = uploaded_file.read().decode("utf-8")

            email = extract_email(resume_text)
            phone = extract_phone(resume_text)
            skills = extract_skills(resume_text)
            score, matched = calculate_resume_score(
                skills, required_skills
            )
            prediction, probability = predict_candidate_status(
                model, skills, matched, score
            )

            candidate_record = {
                "File Name": uploaded_file.name,
                "Email": email,
                "Phone": phone,
                "Skills Found": ", ".join(skills)
                if skills
                else "No skills found",
                "Resume Score": score,
                "Matched Skills": ", ".join(matched)
                if matched
                else "No matched skills",
                "ML Prediction": prediction,
                "Prediction Confidence": round(probability * 100, 2),
            }

            candidate_data.append(candidate_record)

            st.subheader("Candidate Details")
            st.write("Email:", email)
            st.write("Phone:", phone)

            st.subheader("Skills Found")
            if skills:
                for skill in skills:
                    st.write("-", skill)
            else:
                st.write("No matching skills found")

            st.subheader("Resume Match Score")
            st.write("Score:", round(score, 2), "%")

            st.subheader("Matched Skills")
            if matched:
                for skill in matched:
                    st.write("-", skill)
            else:
                st.write("No matched skills found")

            st.subheader("ML Prediction")
            st.write("Status:", prediction)
            st.write("Confidence:", round(probability * 100, 2), "%")

        st.markdown("---")
        st.subheader("Candidate Data Table")

        df = create_candidate_dataframe(candidate_data)
        st.dataframe(df, use_container_width=True)

        stats = calculate_score_statistics(df)

        st.subheader("Score Summary")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Average Score", round(stats["average_score"], 2))

        with col2:
            st.metric("Highest Score", round(stats["highest_score"], 2))

        with col3:
            st.metric("Lowest Score", round(stats["lowest_score"], 2))

        with col4:
            st.metric("Total Candidates", stats["total_candidates"])

        st.subheader("Top Candidates")
        top_df = get_top_candidates(df, top_n=3)
        st.dataframe(top_df, use_container_width=True)

    st.markdown("---")
    st.write("AI Resume Screening System")


menu = st.sidebar.radio("Select Page", ["Login", "Signup"])

if st.session_state.logged_in:
    main_app()
else:
    if menu == "Login":
        login_page()
    else:
        signup_page()

