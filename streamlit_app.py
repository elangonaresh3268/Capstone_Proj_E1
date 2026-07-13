import os
import streamlit as st

from memory import memory
from rag import build_vector_store, get_context
from recommendation import generate_recommendation
from llm import ask_llama
from graph import graph

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(
    page_title="Insurance Advisor",
    page_icon="🛡️",
    layout="wide"
)

if "profile" not in st.session_state:
    st.session_state.profile = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "documents" not in st.session_state:
    st.session_state.documents = []

memory.profile = st.session_state.profile
memory.chat_history = st.session_state.chat_history
memory.vector_store = st.session_state.vector_store
memory.documents = st.session_state.documents

st.title("🛡️ Intelligent Insurance Advisor")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Profile",
        "Upload Documents",
        "Chat",
        "Recommendation"
    ]
)

#########################################################
# PROFILE
#########################################################

if menu == "Profile":

    st.header("User Profile")

    with st.form("profile_form"):

        name = st.text_input("Name")

        age = st.number_input(
            "Age",
            18,
            100,
            25
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other"
            ]
        )

        occupation = st.text_input("Occupation")

        income = st.number_input(
            "Annual Income",
            100000,
            50000000,
            500000
        )

        marital = st.selectbox(
            "Marital Status",
            [
                "Single",
                "Married"
            ]
        )

        medical = st.text_area(
            "Medical History"
        )

        existing = st.text_input(
            "Existing Insurance"
        )

        submit = st.form_submit_button(
            "Save Profile"
        )

        if submit:
                profile_data = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "occupation": occupation,
                    "income": income,
                    "marital_status": marital,
                    "medical_history": medical,
                    "existing_policy": existing
                }

                memory.profile = profile_data
                st.session_state.profile = profile_data

                st.success("Profile Saved Successfully")
#########################################################
# DOCUMENT UPLOAD
#########################################################

elif menu == "Upload Documents":

    st.header("Upload Insurance Documents")

    uploaded = st.file_uploader(
        "Upload PDF / DOCX / TXT",
        type=[
            "pdf",
            "docx",
            "txt"
        ]
    )

    if uploaded:
            filepath = os.path.join(
                UPLOAD_FOLDER,
                uploaded.name
            )

            with open(filepath, "wb") as f:
                f.write(uploaded.read())

            with st.spinner("Processing Document..."):
                chunks = build_vector_store(filepath)

            st.session_state.vector_store = memory.vector_store
            st.session_state.documents = memory.documents

            st.success(
                f"Document Indexed Successfully ({chunks} chunks)"
            )
#########################################################
# CHAT
#########################################################

elif menu == "Chat":

    st.header("Insurance Chat")

    question = st.text_input(
        "Ask your insurance question"
    )

    if st.button("Ask AI"):

        if memory.vector_store is None:

            st.warning(
                "Please upload an insurance document first."
            )

        else:

            context = get_context(question)
            answer = ask_llama(context, question)

            memory.chat_history.append(
                (
                    question,
                    answer
                )
            )

            st.markdown("### AI Response")
            st.write(answer)

    if memory.chat_history:

        st.divider()

        st.subheader("Conversation History")

        for q, a in reversed(memory.chat_history):

            st.markdown(f"**You:** {q}")

            st.markdown(f"**AI:** {a}")

#########################################################
# RECOMMENDATION
#########################################################

elif menu == "Recommendation":

    st.header("Insurance Recommendation")

    if memory.vector_store is None:

        st.info(
            "Upload insurance documents first."
        )

    elif not memory.profile:

        st.info(
            "Complete your profile first."
        )

    else:

        if st.button("Generate Recommendation"):
            context = get_context(
                "Recommend the best insurance policy based on the user profile and uploaded documents."
            )
            answer = generate_recommendation(memory.profile, context)

            st.success("Recommendation Ready")
            st.write(answer)
