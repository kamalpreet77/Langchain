# 🔑 ChatPromptTemplate — For chat models like GPT-4 or Claude. You structure messages with roles: system (AI's persona) + human (user message) + optionally ai (prior response).


from dotenv import load_dotenv
import os

from openai import chat
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Using HuggingFace's OpenAI-compatible router
chat_model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    model="deepseek-ai/DeepSeek-V4-Pro:novita",
)

# maintain chathistory
chat_history = []

while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input.lower() == "exit"):
        break
    
    result=chat_model.invoke(chat_history)
    chat_history.append(result)
    print("AI:", result.content)
    


    
    
    
    
    