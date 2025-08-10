import asyncio
import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma  # use the updated import if you switched from deprecated one

# Make sure there's an event loop for async gRPC
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Set Google API Key
os.environ["GOOGLE_API_KEY"] = "YAIzaSyBnS4nnKJtgB7oyhDJ17SOCyMlxWrGHsCQ"

# Create embeddings
embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Example vector DB creation (replace with your logic)
vectordb = Chroma(embedding_function=embedding_function)

st.title("Job Recommender")
st.write("Your app is running without event loop errors now!")
import os
import streamlit as st
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# ✅ Set API key directly instead of using st.secrets
os.environ["GOOGLE_API_KEY"] = "AIzaSyBnS4nnKJtgB7oyhDJ17SOCyMlxWrGHsCQ"  # <-- Replace with your real API key

# Load Chroma DB
vectordb = Chroma(
    persist_directory="jobs_chroma_db",
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
)
retriever = vectordb.as_retriever(search_kwargs={"k": 5})

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Prompt
prompt_template = """
You are an AI job recommendation assistant.
Given the user's skills and preferences, recommend the most relevant job openings from the retrieved postings.

User profile:
{query}

Relevant jobs:
{context}

Provide recommendations in bullet points with job title, company, and location.
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["query", "context"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt, "input_key": "query"},
    return_source_documents=True
)

# Streamlit UI
st.title("💼 AI Job Recommendation System")
st.write("Discover jobs that fit your skills & preferences.")

user_input = st.text_area("Enter your skills, experience, and job preferences:")

if st.button("Get Recommendations"):
    if user_input.strip():
        with st.spinner("Finding best matches..."):
            response = qa_chain({"query": user_input})
        st.subheader("Recommended Jobs")
        st.write(response["result"])

        with st.expander("See Source Job Descriptions"):
            for i, doc in enumerate(response["source_documents"], start=1):
                st.markdown(f"**Source {i}:** {doc.page_content}")
    else:
        st.warning("Please enter your profile information.")