import streamlit as st
from data.mock_policy_data import MOCK_INSURANCE_DATA
from core.llm_handler import generate_policy_answer

st.set_page_config(page_title="Insurance Policy Q&A Demonstrator")
st.title("Insurance Policy Q&A Demonstrator")

company_list = ["Select a Company..."] + list(MOCK_INSURANCE_DATA.keys())
selected_company = st.selectbox("Select an Insurance Company:", company_list)

policy_list = ["Select a Policy..."]
if selected_company and selected_company != "Select a Company...":
    policy_list += list(MOCK_INSURANCE_DATA[selected_company].keys())
selected_policy = st.selectbox("Select a Policy Type:", policy_list)

policy_text = ""
if selected_company != "Select a Company..." and selected_policy != "Select a Policy...":
    policy_text = MOCK_INSURANCE_DATA[selected_company][selected_policy]
    st.markdown("**Mock Policy Document:**")
    st.text_area("", policy_text, height=120, disabled=True)

st.markdown("**Ask your question about the policy:**")
user_question = st.text_input("", "")

if st.button("Get AI Answer"):
    if selected_company == "Select a Company..." or selected_policy == "Select a Policy...":
        st.warning("Please select both a company and a policy type before asking a question.")
    elif not user_question.strip():
        st.warning("Please enter a question about the policy.")
    else:
        with st.spinner("AI is generating an answer..."):
            try:
                answer = generate_policy_answer(policy_text, user_question)
                st.markdown("**AI's Answer:**")
                st.success(answer)
            except Exception:
                st.error("Sorry, I encountered an error trying to generate an answer.")
