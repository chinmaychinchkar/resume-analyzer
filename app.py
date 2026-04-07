import streamlit as st
from skills import extract_skills
from jobs import match_jobs_ml
import PyPDF2
import re

# -------- TEXT EXTRACTION --------
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# -------- CLEAN TEXT --------
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

# ---------------- UI ----------------
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🚀")

st.title("🚀 AI Resume Analyzer (ML Powered)")
st.write("Upload your resume and get intelligent job role predictions.")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    # -------- PROCESS RESUME --------
    text = extract_text(uploaded_file)
    cleaned_text = clean_text(text)

    # -------- SKILL EXTRACTION --------
    skills = extract_skills(cleaned_text)

    # -------- ML MATCHING (WITH SKILL BOOST) --------
    job_matches = match_jobs_ml(cleaned_text, skills)

    best_job = max(job_matches, key=job_matches.get)
    max_score = max(job_matches.values())

    # -------- SKILLS DISPLAY --------
    st.subheader("🔍 Extracted Skills")

    if skills:
        col1, col2 = st.columns(2)

        for i, skill in enumerate(skills):
            if i % 2 == 0:
                col1.write(f"✔ {skill}")
            else:
                col2.write(f"✔ {skill}")
    else:
        st.warning("No relevant skills detected.")

    # -------- SCORES DISPLAY --------
    st.subheader("📊 Job Match Scores (ML Based)")

    for job, score in job_matches.items():
        if score == max_score and score != 0:
            st.success(f"{job}: {score}%")
        else:
            st.write(f"{job}: {score}%")

    # -------- BEST MATCH --------
    st.subheader("🏆 Best Match")

    if max_score == 0:
        st.error("No matching job role found.")
    else:
        st.success(best_job)

    # -------- CONFIDENCE --------
    st.subheader("📈 Confidence Level")
    st.progress(max_score / 100)

    # -------- EXPLANATION (VERY IMPORTANT 🔥) --------
    st.subheader("🧠 Why this match?")

    if max_score > 0:
        st.write(
            f"This resume is best suited for the role of **{best_job}** "
            f"because it contains relevant skills such as: "
            f"**{', '.join(skills[:5])}** which align with job requirements."
        )
    else:
        st.write("No strong alignment found with available job roles.")
