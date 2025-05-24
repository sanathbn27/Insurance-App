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
policy_preview = ""
if selected_company != "Select a Company..." and selected_policy != "Select a Policy...":
    policy_data = MOCK_INSURANCE_DATA[selected_company][selected_policy]
    policy_preview = policy_data["preview"]
    # Fetch the document by calling the lambda
    policy_text = policy_data["document"]()
    st.markdown("**Mock Policy Preview:**")
    st.text_area("", policy_preview, height=80, disabled=True)

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
