def match_jobs_ml(resume_text, skills):
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    df = pd.read_csv("jobs.csv")

    job_names = df["job_role"].tolist()
    job_descriptions = df["description"].tolist()

    # 🔥 BOOST SKILLS IMPORTANCE
    boosted_resume = resume_text + " " + " ".join(skills) * 3

    documents = [boosted_resume] + job_descriptions

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    resume_vector = tfidf_matrix[0]
    job_vectors = tfidf_matrix[1:]

    similarity_scores = cosine_similarity(resume_vector, job_vectors)[0]

    results = {}
    for i, score in enumerate(similarity_scores):
        results[job_names[i]] = int(score * 100)

    return results