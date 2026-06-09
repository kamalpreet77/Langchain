# 🔑 FewShotPromptTemplate — Teach the model by example. Instead of explaining what you want in words, you show input → output pairs and the model learns the pattern.


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

