from langchain_core.prompts import PromptTemplate
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

st.header('reasearch tool')

# Step 1: Define Variables for the prompt

TopicInput=st.selectbox('Select a topic', ['RAG', 'machine learning', 'AI'])
LevelInput=st.selectbox('Select a level', ['10-year-old', 'high school student', 'college student'])

# Step 2: Define the template with {variables}

template=PromptTemplate(
    template="You are a helpful assistant. Explain {topic} in simple terms for a {level}.",
    input_variables=["topic", "level"]
)

#Step 3: Fill in the variables


prompt = template.format(
    topic=TopicInput,
    level=LevelInput
)


# Step 4: Get the response from the model
if st.button('Summarize'):
    result=chat_model.invoke([HumanMessage(content=prompt)])
    st.write(result.content)
    
    
    