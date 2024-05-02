# Q&A Chatbot
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
import streamlit as st

## Function to load OpenAI model and get responses
def get_openai_response(question, api_key):
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.5, **api_key)
    response = llm(question)
    return response

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("OPEN AI Application")

input_text = st.text_input("Input: ", key="input")
my_api_key = {"api_key": "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"}  # Replace this with your actual API key

submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    st.subheader("The Response is")
    response = get_openai_response(input_text, my_api_key)
    st.write(response)
