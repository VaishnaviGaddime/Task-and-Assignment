def calculate_resume_score(candidate_skills: list[str], required_skills: list[str]) -> tuple[float, list[str]]:
    matched_skills: list[str] = []

    for skill in candidate_skills:
        if skill in required_skills:
            matched_skills.append(skill)

    score = 0.0
    if len(required_skills) > 0:
        score = (len(matched_skills) / len(required_skills)) * 100

    return score, matched_skills

