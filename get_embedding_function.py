import openai 
from langchain_openai import OpenAIEmbeddings

import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]



def get_embedding_function():
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    embeddings = OpenAIEmbeddings()
    return embeddings
