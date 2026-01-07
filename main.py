import streamlit as st
from query_data import query_rag

st.write("## Ask your question")


query = st.text_input("query")
respons = query_rag(query)
st.write(respons)


