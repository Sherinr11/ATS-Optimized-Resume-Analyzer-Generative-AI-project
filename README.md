# CareerCraft: ATS Optimized Resume Analyzer

## Overview
CareerCraft is an innovative platform designed to help job seekers optimize their resumes to stand out in a competitive job market. By leveraging advanced ATS (Applicant Tracking System) technology, CareerCraft provides valuable insights into resume compatibility with job descriptions, enhancing the chances of landing interviews.

## Features
- **ATS-Optimized Resume Analysis:** Get detailed feedback on how well your resume matches a job description.
- **Resume Optimization:** Suggestions for enhancing your resume to meet job requirements.
- **Skill Enhancement:** Identify key skills needed for specific roles and improve your profile.
- **Career Progression Guidance:** Insights on advancing your career based on current trends.
- **Tailored Profile Summaries:** Customized summaries based on your resume and the job description.
- **Streamlined Application Process:** Simplify your job application with optimized documents.
- **Personalized Recommendations:** Get specific advice to improve your resume.
- **Efficient Career Navigation:** Tools and insights to help you navigate your career path.

## Technologies Used
- **Python:** For backend processing and logic.
- **Streamlit:** For creating the interactive web application.
- **PyPDF2:** To extract text from PDF resumes.
- **Google Generative AI:** For generating insights and recommendations.
- **PIL (Pillow):** For handling image processing.

## Getting Started

### Prerequisites
- Python 3.x
- Streamlit
- PyPDF2
- Pillow
- Google Generative AI library
- An API key for Google Generative AI (stored in a `.env` file)

### Installation
1. Clone the repository:
      ```bash
    git clone https://github.com/yourusername/careercraft.git
    cd careercraft
2.  Create a virtual environment (optional but recommended):

    ```bash 
    python -m venv venv 
    source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Install the required packages:
   ```bash

   pip install -r requirements.txt
4. Create a .env file in the project root and add your Google API key:

    ```bash

    echo "GOOGLE_API_KEY=your_api_key_here" > .env
5. Running the Application:

To run the application, use the following command:

  ```bash

   streamlit run app.py

