def extract_skills(text: str) -> list[str]:
    skills_list = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "NLP",
        "Data Analysis",
        "Pandas",
        "NumPy",
        "Flask",
        "Django",
        "TensorFlow",
        "PyTorch",
        "Power BI",
        "Excel",
        "Java",
    ]
    found_skills: list[str] = []
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills

