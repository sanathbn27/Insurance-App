"""
Handles loading the LLM, prompt construction, and answer generation using LangChain.
"""
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from functools import lru_cache

MODEL_NAME = "google/flan-t5-small"

@lru_cache(maxsize=1)
def get_langchain_llm():
    # Load model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=128,
        min_length=10,
        num_beams=4,
        early_stopping=True,
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    return llm

def generate_policy_answer(policy_text: str, user_question: str) -> str:
    """
    Constructs the prompt and generates an answer using LangChain LLM.
    """
    llm = get_langchain_llm()
    prompt_template = PromptTemplate(
        input_variables=["policy_text", "user_question"],
        template=(
            "You are an expert insurance assistant. Answer the user's question based only on the following policy document. "
            "If the answer is not found in the document, say 'The information is not found in the policy document.'\n\n"
            "Policy Document: {policy_text}\n\n"
            "Question: {user_question}\n"
            "Answer:"
        ),
    )
    prompt = prompt_template.format(policy_text=policy_text, user_question=user_question)
    answer = llm(prompt)
    return answer.strip()
