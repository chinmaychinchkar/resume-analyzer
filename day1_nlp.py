import spacy

nlp = spacy.load("en_core_web_sm")

text = "Skilled in Java, C++, Python and Data Science."


doc = nlp(text)

clean_words = []

for token in doc:
    # remove punctuation & spaces
    if not token.is_punct and not token.is_space:
        clean_words.append(token.text.lower())

print(clean_words)