from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Configure the Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(input_text):
    """Get response from the Gemini model based on input text."""
    response = model.generate_content(input_text)
    return response

def input_pdf_text(uploaded_file):
    """Extract text from the uploaded PDF file."""
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())  # Extract text from each page
    
    return text

input_prompt = """As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the job description and meticulously identify any missing keywords with utmost accuracy.

Resume: {text}
Description: {jd}

I want the response in the following structure:
1. The first line indicates the percentage match with the job description.
2. The second line presents a list of missing keywords.
3. The third section provides a profile summary.

Please mention the title for all three sections and ensure there is some space to separate each section in the response.
"""

# Set the Streamlit page configuration
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

# Set background color and add some custom CSS
st.markdown("""
    <style>
    .main {
        background-color:white;  /* Light background color */
        padding: 2rem;              /* Padding for the content */
    }
    img {
        opacity: 0.9;               /* Make images slightly transparent */
        border-radius: 10px;       /* Rounded corners for images */
    }
    </style>
    """, unsafe_allow_html=True)

# Add vertical space
avs.add_vertical_space(4)

# Create columns for the introduction
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<h1 style='color: blue;'>CareerCraft</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: blue;'>Navigate the Job Market with Confidence!</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style="text-align: justify;">
        Introducing CareerCraft, an ATS Optimized Resume Analyzer your ultimate solution for optimizing job applications and accelerating career growth. 
        Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes compatibility with job descriptions. 
        From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market. 
        Streamline your job application process, enhance your skills, and navigate your career path with confidence. 
        Join CareerCraft today and unlock new opportunities for professional success!
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<div style='margin-right: 20px;'></div>", unsafe_allow_html=True)
    st.image('images/icon (2).jpg', use_column_width=True)

# Add more vertical space if needed
avs.add_vertical_space(10)

# Create columns for offerings
col1, col2 = st.columns([3, 2])

with col2:
    st.markdown("<h2 style='color: blue;'>Wide Range of Offerings</h2>", unsafe_allow_html=True)
    st.write('ATS-Optimized Resume Analysis')
    st.write('Resume Optimization')
    st.write('Skill Enhancement')
    st.write('Career Progression Guidance')
    st.write('Tailored Profile Summaries')
    st.write('Streamlined Application Process')
    st.write('Personalized Recommendations')
    st.write('Efficient Career Navigation')

with col1:
    img1 = Image.open("images/icon1.jpg")
    st.image(img1, use_column_width=True)

avs.add_vertical_space(10)

# Create columns for user input
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<h1 style='color: blue; text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    
    # Text area for job description input
    jd = st.text_area("Paste the Job Description")
    
    # File uploader for resume upload
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

    # Submit button
    submit = st.button("Submit")
    if submit:
        if uploaded_file is not None:
            # Extract text from the uploaded PDF
            text = input_pdf_text(uploaded_file)
            # Get response from the Gemini model
            response = get_gemini_response(input_prompt.format(text=text, jd=jd))
         
            # Access the result
            candidates = response._result.candidates if response._result else []

            if candidates:
                # Access the first candidate's content
                content = candidates[0].content

                # Extract the text from the parts
                if content.parts:
                    display_text = content.parts[0].text  # Get the text of the first part

                    # Display the response in Streamlit
                    st.subheader(display_text)
                else:
                    st.warning("No content parts found.")
            else:
                st.warning("No candidates found.")
        else:
            st.warning("Please upload a resume.")

with col2:
    img2 = Image.open("images/icon2.jpg")
    st.image(img2, use_column_width=True)

# Add vertical space at the end if needed
avs.add_vertical_space(10)

# Create columns for FAQs
col1, col2 = st.columns([3, 2])

with col2:
    st.markdown("<h1 style='color: blue; text-align: center;'>FAQ</h1>", unsafe_allow_html=True)
    
    st.write("Question: How does CareerCraft analyze resumes and job descriptions?")
    st.write("""Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.""")
    avs.add_vertical_space(3)
    
    st.write("Question: Can CareerCraft suggest improvements for my resume?")
    st.write("Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.")
    avs.add_vertical_space(3)
    
    st.write("Question: Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.""")

with col1:
    st.markdown("<div style='margin-left: 10px;'></div>", unsafe_allow_html=True)  # Adjust the margin as needed
    img3 = Image.open("images/icon4.jpg")
    st.image(img3, use_column_width=True)
