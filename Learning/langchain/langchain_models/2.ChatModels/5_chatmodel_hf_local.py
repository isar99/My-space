# Do not run, will consume lot of data
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100}
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of France?")
print(result.content)
