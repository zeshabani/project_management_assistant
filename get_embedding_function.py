import openai 
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key 
openai.api_key = os.environ['OPENAI_API_KEY']


def get_embedding_function():
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    embeddings = OpenAIEmbeddings()
    return embeddings
