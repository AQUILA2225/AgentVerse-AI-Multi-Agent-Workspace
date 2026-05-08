import PyPDF2

from utils.llm import get_ai_response


def extract_resume_text(uploaded_resume):

    pdf_reader = PyPDF2.PdfReader(uploaded_resume)

    resume_text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:

            resume_text += page_text + "\n"

    return resume_text


def analyze_resume(resume_text, job_description):

    analysis_prompt = f"""
You are an ATS Resume Analyzer Agent.

Analyze the resume against the job description.

Resume Text:
{resume_text}

Job Description:
{job_description}

Give the output in this format:

1. ATS Match Score:
Give percentage out of 100.

2. Matched Skills:
List skills present in both resume and job description.

3. Missing Skills:
List important skills from job description missing in resume.

4. Improvement Suggestions:
Give clear beginner-friendly suggestions to improve the resume.

5. Suggested Resume Bullet Points:
Give 3 improved resume bullet points based on the job description.
"""

    analysis_result = get_ai_response(analysis_prompt)

    return analysis_result