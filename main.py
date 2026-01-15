import streamlit as st
from query_data import query_rag
from pathlib import Path
from populate_database import populate_database, clear_database


    

if "did_run_once" not in st.session_state:
    clear_database()
    st.session_state["did_run_once"] = True

UPLOAD_DIR = Path("data")
UPLOAD_DIR.mkdir(exist_ok=True)
f = st.file_uploader("Upload a PDF", type="pdf")
if f is not None:
    save_path = UPLOAD_DIR / f.name
    with open(save_path, "wb") as out:
        out.write(f.getvalue())  # bytes
    st.success(f"Saved to {save_path}")
    populate_database()




st.write("## Ask your question")


query = st.text_input("query")
respons = query_rag(query)
st.write(respons)


