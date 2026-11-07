from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-70B-Instruct",
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiments: Annotated[str, "Return sentiment of the review either negative, neutral, or positive"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("What did the customer think of the product?")
print(result)
