import spacy

nlp = spacy.load("en_core_web_sm")

# predefined skills list
skills_list = [
    "python", "java", "sql", "machine learning",
    "data science", "deep learning",
    "excel", "power bi",
    "adobe premiere pro", "davinci resolve",
    "video editing", "audio editing",
    "avid", "scriptwriting", "video production",
    "html", "css", "javascript", "react"
]

def extract_skills(text):
    doc = nlp(text)

    found_skills = set()

    # match predefined skills
    for skill in skills_list:
        if skill in text:
            found_skills.add(skill)

    # also extract noun chunks (extra intelligence)
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.lower()
        if chunk_text in skills_list:
            found_skills.add(chunk_text)

    return list(found_skills)