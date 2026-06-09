from dotenv import load_dotenv
import os

from openai import chat
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Using HuggingFace's OpenAI-compatible router
chat_model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    model="deepseek-ai/DeepSeek-V4-Pro:novita",
)

#chat template 

chat_history = [
    HumanMessage(content="Hello"),
    AIMessage(content="Hi! How can I help?")
]

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains concepts in simple terms."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])
# maintain chathistory

with open("chat_history.txt", "r") as f:
    for line in f:
        chat_history.append(
            HumanMessage(content=line.strip())
        )
    
print("Chat History:")

#create Prompt

prompt = chat_template.invoke({
    "chat_history": chat_history,
    "question": "What is the capital of France?"
})

print("Prompt:", prompt)