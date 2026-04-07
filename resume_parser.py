from skills import extract_skills
from jobs import match_jobs
import PyPDF2
import re

def extract_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

# --- MAIN EXECUTION ---
resume_text = extract_text("resume.pdf")
cleaned_text = clean_text(resume_text)

skills = extract_skills(cleaned_text)

job_matches = match_jobs(skills)

print("Skills:", skills)
print("Job Matches:", job_matches)


best_job = max(job_matches, key=job_matches.get)
print("Best Match:", best_job)