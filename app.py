import streamlit as st
from PyPDF2 import PdfReader

st.title("AI Resume Skill Gap Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text.lower()   # ← MUST be inside this block

    aiml_skills = [
        "python", "machine learning", "deep learning",
        "nlp", "computer vision", "pandas", "numpy",
        "scikit-learn", "tensorflow", "pytorch",
        "sql", "statistics"
    ]

    matched_skills = []
    missing_skills = []

    for skill in aiml_skills:
        if skill in text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = (len(matched_skills) / len(aiml_skills)) * 100

    st.subheader("Resume Score")
    st.progress(int(score))
    st.write(f"Match Score: {score:.2f}%")

    st.subheader("Matched Skills")
    st.write(matched_skills)

    st.subheader("Missing Skills")
    st.write(missing_skills)