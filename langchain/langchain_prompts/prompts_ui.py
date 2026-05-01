# NOTE: ## in code indicated the static prompts that was used earlier. Current working code is for dynamic prompt generation.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv  
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

paper_input = st.selectbox("Select a research paper:", ["Attention is all you need", 
"BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners",
"Diffusion Models Beat GANs on Image Synthesis", "AlphaFold: Protein Structure Prediction with Deep Learning"])

style_input = st.selectbox("Select explanation style:", ["Summary", "Beginner-friendly", "Technical", 
"Code Oriented", "Mathematical"])

length_input = st.selectbox("Select explanation length:", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", 
"Long (6+ paragraphs)"])

# # template
# template=PromptTemplate(input_variables=["paper_input", "style_input", "length_input"], template="\nPlease summarize the research paper titled \"{paper_input}\" with the following specifications:\nExplanation Style: {style_input}  \nExplanation Length: {length_input}  \n1. Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper.  \n   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  \n2. Analogies:  \n   - Use relatable analogies to simplify complex ideas.  \nIf certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  \nEnsure the summary is clear, accurate, and aligned with the provided style and length.\n")

template = load_prompt("template.json")

# fill the placeholders in the template
prompt = template.invoke({"paper_input": paper_input, 
                 "style_input": style_input, 
                 "length_input": length_input})


## user_input = st.text_input("Enter your query:")

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
    ## result = model.invoke(user_input)
    ## st.write(result.content)
