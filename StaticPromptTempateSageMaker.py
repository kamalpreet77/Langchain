from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import streamlit as st

# Using HuggingFace's OpenAI-compatible router
chat_model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    model="deepseek-ai/DeepSeek-V4-Pro:novita",
)

# response = chat_model.invoke([HumanMessage(content="Explain RAG in simple terms")])
# print(response.content)


# make a simple streamlit app to show the response
st.header('reasearch tool')
user_input=st.text_input('Enter your question')

if st.button('summarize'):
    result=chat_model.invoke([HumanMessage(content=user_input)])
    st.write(result.content)
    
