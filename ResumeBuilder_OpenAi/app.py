import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_chat_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ensure this is the correct model for your needs
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # The response format for ChatCompletion is different; adjust accordingly
    return response.choices[0].message['content'].strip()


# Streamlit app setup
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Define the buttons here to ensure they're set up before their use in logic
submit1 = st.button("Tell Me About the Resume")
# Uncomment and implement the logic for submit2 if needed
# submit2 = st.button("How Can I Improve my Skills")
submit3 = st.button("Percentage match")

# Assuming you've handled PDF content to text conversion or other preprocessing
pdf_text = "Extracted text from your PDF or a summary that you've generated"

if submit1:
    if uploaded_file is not None:
        # Placeholder for your PDF processing/conversion to text
        input_prompt1 = """
        Based on the detailed analysis of the skills, experiences, and qualifications mentioned in the resume against the specific requirements 
        and preferences outlined in the job description, estimate the alignment percentage. Please provide a justified percentage match, taking 
        into account the presence or absence of critical skills, the level of experience, and the relevance of the candidate's background to the 
        role's needs.

        """
        response = get_openai_chat_response(f"{input_text}\n\n{pdf_text}\n\n{input_prompt1}")
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        input_prompt3 = """
        You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
        your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
        the job description. First, the output should come as a percentage and then keywords missing and last final thoughts.
        """
        response = get_openai_chat_response(f"{input_text}\n\n{pdf_text}\n\n{input_prompt3}")
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
