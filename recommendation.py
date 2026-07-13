from llm import ask_llama


def _get_condition_focus(profile: dict) -> str:
    medical_history = (profile.get("medical_history") or "").lower()

    respiratory_terms = ["respiratory", "asthma", "copd", "bronchitis", "emphysema", "lung disease", "pneumonia", "oxygen", "tb"]
    heart_terms = ["heart", "cardiac", "heart disease", "hypertension", "bp", "high blood pressure", "stroke", "arrhythmia"]
    cancer_terms = ["cancer", "tumor", "malignancy"]
    diabetes_terms = ["diabetes", "sugar"]

    if any(term in medical_history for term in respiratory_terms):
        return f"""
        IMPORTANT: The user has a medical history that includes severe respiratory disease: {profile.get('medical_history')}
        Make this the main reason for the recommendation.
        Prioritize policies that cover hospitalization, ICU care, oxygen therapy, emergency admission, respiratory treatment, medicines, chronic disease support, and day-care procedures.
        Explain clearly why these features are valuable for someone with this condition.
        """

    if any(term in medical_history for term in heart_terms):
        return f"""
        IMPORTANT: The user has a medical history that includes heart-related disease: {profile.get('medical_history')}
        Make this the main reason for the recommendation.
        Prioritize policies that cover hospitalization, ICU care, emergency cardiac treatment, surgery, medicines, follow-up care, and chronic disease support.
        Explain clearly why these features are valuable for someone with this condition.
        """

    if any(term in medical_history for term in cancer_terms):
        return f"""
        IMPORTANT: The user has a medical history that includes cancer-related disease: {profile.get('medical_history')}
        Make this the main reason for the recommendation.
        Prioritize policies that cover hospitalization, chemotherapy, surgery, specialist treatment, medicines, and critical illness support.
        Explain clearly why these features are valuable for someone with this condition.
        """

    if any(term in medical_history for term in diabetes_terms):
        return f"""
        IMPORTANT: The user has a medical history that includes diabetes: {profile.get('medical_history')}
        Make this the main reason for the recommendation.
        Prioritize policies that cover hospitalization, regular treatment, medicines, diabetic care, and chronic disease support.
        Explain clearly why these features are valuable for someone with this condition.
        """

    return """
    If the profile includes a serious health condition, make it central to the recommendation and explain why the chosen policy is suitable.
    """


def build_recommendation_prompt(profile: dict, context: str) -> str:
    condition_focus = _get_condition_focus(profile)

    return f"""
    You are an expert Insurance Advisor.
    User Profile
    Name : {profile.get("name")}
    Age : {profile.get("age")}
    Gender : {profile.get("gender")}
    Occupation : {profile.get("occupation")}
    Income : {profile.get("income")}
    Marital Status : {profile.get("marital_status")}
    Medical History : {profile.get("medical_history")}
    Existing Insurance : {profile.get("existing_policy")}

    Insurance Documents
    {context}

    Based ONLY on the provided user profile and insurance documents,

    {condition_focus}

    Recommend:
    1. Best insurance policy
    2. Why it suits the customer
    3. Coverage details
    4. Premium (if available)
    5. Most useful parts of the policy
    6. Why this premium is valuable for the customer
    7. Advantages
    8. Important exclusions
    9. Confidence score (0-100%)

    Present the answer in a clear bullet-point format. Highlight the most useful parts of the policy and explain why the premium is valuable.
    Do not give a generic answer. Tie every recommendation to the user's profile and medical history.

    If the document does not contain the requested information, clearly say "not available"
    """


def generate_recommendation(profile: dict, context: str):
    prompt = build_recommendation_prompt(profile, context)
    return ask_llama(context, prompt)