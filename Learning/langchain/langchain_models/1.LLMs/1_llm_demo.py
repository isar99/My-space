# from langchain_openai import OpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# llm = OpenAI(model="gpt-3.5-turbo-instruct")

# result = llm.invoke("What is the capital of France?")

# print(result)

model = ChatGroq(model="llama-3.1-8b-instant",
    temperature=0.0,
    max_retries=2,
)

result = model.invoke("What is the capital of France?")

print(result.content)
