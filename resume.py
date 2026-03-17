import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def show():
    st.title("Resume Critiquer")
    st.markdown("Upload your resume in PDF format and get feedback on how to improve it.")

    api_key = os.getenv("OPEN-AI-KEY")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    job_description = st.text_area("Enter the job description for the position you are applying for:")
    analyze_button = st.button("Analyze Resume")

    def extract_text_from_pdf(file):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    def extract_text_from_file(uf):
        if uf.type == "application/pdf":
            return extract_text_from_pdf(io.BytesIO(uf.read()))
        return uf.read().decode("utf-8")

    if analyze_button and uploaded_file:
        try:
            file_content = extract_text_from_file(uploaded_file)
            if not file_content:
                st.error("Could not extract text from the uploaded file. Please ensure it is a valid PDF or text file.")
                st.stop()

            prompt = f"""Please analyze this resume and provide constructive feedback.
            Focus on the following areas:
            1. Content clarity and impact
            2. Skills presentation
            3. Experience Descriptions
            4. Specific improvements for {job_description}
            Resume Content:
            {file_content}

            Please provide your analysis in a clear, structured format with specific recommendations.
            """

            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            st.subheader("Resume Analysis")
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
