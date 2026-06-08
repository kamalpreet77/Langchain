from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Using HuggingFace's OpenAI-compatible router
chat_model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    model="deepseek-ai/DeepSeek-V4-Pro:novita",
)

response = chat_model.invoke([HumanMessage(content="Explain RAG in simple terms")])
print(response.content)