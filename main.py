import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Resume Critiquer", page_icon="📄",layout="centered")
st.title("Resume Critiquer")
st.markdown("Upload your resume in PDF format and get feedback on how to improve it.")

OpenAI.api_key = os.getenv("OPEN-AI-KEY")
Uploaded_file=st.file_uploader("Choose a PDF file", type="pdf")
Job_description=st.text_area("Enter the job description for the position you are applying for:")
Analyze_button=st.button("Analyze Resume")
