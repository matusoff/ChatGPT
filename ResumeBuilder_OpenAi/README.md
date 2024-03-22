# ATS Tracking System

This  application leverages the power of Streamlit and OpenAI's GPT models to provide an interactive interface for matching your resume with Job Description. 
ATS Resume Expert is a Streamlit application designed to help users evaluate their resumes against job descriptions using OpenAI's powerful AI models.
It provides insights on how well a resume matches a job description, identifies missing keywords, suggests skills improvements, and estimates a percentage match.


## Features

- **Powered by OpenAI**: Utilize the cutting-edge capabilities of GPT models for suggestions and content creation.
- **Customizable Templates**: Choose from a variety of templates to find the one that best suits your professional profile.
- **Export Functionality**: Easily upload your resume in PDF format for matching your resume with Job Description.

## Getting Started

To get started with the Resume Builder app, follow these steps:

### Prerequisites

- requirements.txt
- An OpenAI API key
- Poppler for PDF processing (Windows users)

### Setup Instructions

1. Obtain an OpenAI API Key
   
To use this application, you'll need an API key from OpenAI.

Follow these steps to obtain one:

Visit OpenAI and sign up or log in.

Navigate to the API section and follow the instructions to generate a new API key.

3. Install Required Python Packages
   
```bash
pip install -r requirements.txt
```
3. Setup Poppler for PDF Processing (Windows Users)
To process PDF files, Windows users need to set up Poppler. Follow these steps:

Download Poppler for Windows from the Poppler Windows releases page.

Extract the downloaded Poppler zip file.

Create a new folder named poppler in C:\Program Files (x86).

Copy and paste the extracted Poppler folder into the C:\Program Files (x86)\poppler.

Add Poppler to your PATH environment variable:

Search for "Environment Variables" in Windows search and select "Edit the system environment variables."

In the System Properties window, click on the "Environment Variables" button.

In the Environment Variables window, under "System variables," find the PATH variable and select it. Click "Edit."

In the Edit Environment Variable window:

click "New" and add the path to the Poppler bin directory, which should be something like C:\Program Files (x86)\poppler\[Poppler-Version]\Library\bin.

### Running the Application
To run the Resume Builder application, execute the following command:

```bash
streamlit run app.py
```

After running the command, Streamlit will start the web server, and you should see a URL in your terminal, which you can visit with your web browser to access 
the application.
