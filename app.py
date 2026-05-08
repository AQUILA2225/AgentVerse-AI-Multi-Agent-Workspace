# import streamlit as st 
# from utils.llm import get_ai_response 
# from utils.memory import load_memory, save_memory
# from utils.rag import search_knowledge_base
# from utils.agent import generate_learning_roadmap, generate_daily_tasks

# st.set_page_config(
#     page_title="AI Thought Partner",
#     page_icon="🧠",
#     layout="wide"
# )

# st.title("🧠 AI Thought Partner")
# st.write("Your AI Companion for ideas, goals, learning, and planning.")

# user_input = st.text_area("What would you like help with?")
# if st.button("Ask AI"):
#     if user_input:
#         with st.spinner("Thinking..."):
#             memory_data = load_memory()
#             knowledge_text = search_knowledge_base(user_input)
#             ai_response = get_ai_response(user_input, memory_data, knowledge_text)
            
#             save_memory(user_input, ai_response)
            
#         st.success("AI Response")
#         st.write("ai_response")
#     else:
#         st.warning("Please enter a question.")
        
# st.divider()

# st.subheader("Agent Tools")

# career_goal = st.text_input("Enter your career or learning goal")
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("Generate Learning Roadmap"):
#         if career_goal:
#             memory_data = load_memory()
#             knowledge_text = search_knowledge_base(career_goal)
            
#             roadmap = generate_learning_roadmap(
#                 career_goal,
#                 memory_data,
#                 knowledge_text
#             )
            
#             st.subheader("Learning Roadmap")
#             st.write(roadmap)
        
#         else:
#             st.warning("Please enter your goal first.")
    
# with col2:
#     if st.button("Generate Daily Tasks"):
#         if career_goal:
#             memory_data = load_memory()
#             knowledge_text = search_knowledge_base(career_goal)
            
#             tasks = generate_daily_tasks(
#                 career_goal,
#                 memory_data,
#                 knowledge_text
#             )
            
#             st.subheader("Daily Tasks")
#             st.write(tasks)
            
#         else:
#             st.warning("Please enter your goal first.")

# st.subheader("Conversation Memory") 

# memory_data = load_memory()

# if memory_data:
#     for conversation in memory_data[-5:]:
#         st.write("**You:**", conversation["user"])
#         st.write("**AI:**", conversation["ai"])
#         st.divider()
    
#     else:
#         st.info("No conversation memory yet.")
            
# import streamlit as st

# from utils.llm import get_ai_response
# from utils.memory import save_memory, load_memory
# from utils.rag import search_knowledge_base
# from utils.agent import generate_learning_roadmap, generate_daily_tasks


# st.set_page_config(
#     page_title="AI Thought Partner",
#     page_icon="🧠",
#     layout="wide"
# )


# st.title("🧠 AI Thought Partner")
# st.caption("Your personal AI companion for ideas, goals, learning, and planning.")


# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# with st.sidebar:
#     st.header("Agent Tools")

#     career_goal = st.text_input("Enter your career or learning goal")

#     if st.button("Generate Learning Roadmap"):
#         if career_goal:
#             with st.spinner("Generating roadmap..."):
#                 memory_data = load_memory()
#                 knowledge_text = search_knowledge_base(career_goal)

#                 roadmap = generate_learning_roadmap(
#                     career_goal,
#                     memory_data,
#                     knowledge_text
#                 )

#             st.session_state.chat_history.append(
#                 {
#                     "role": "assistant",
#                     "content": roadmap
#                 }
#             )

#         else:
#             st.warning("Please enter your goal first.")

#     if st.button("Generate Daily Tasks"):
#         if career_goal:
#             with st.spinner("Generating daily tasks..."):
#                 memory_data = load_memory()
#                 knowledge_text = search_knowledge_base(career_goal)

#                 tasks = generate_daily_tasks(
#                     career_goal,
#                     memory_data,
#                     knowledge_text
#                 )

#             st.session_state.chat_history.append(
#                 {
#                     "role": "assistant",
#                     "content": tasks
#                 }
#             )

#         else:
#             st.warning("Please enter your goal first.")

#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []


# for message in st.session_state.chat_history:

#     with st.chat_message(message["role"]):
#         st.write(message["content"])


# user_input = st.chat_input("Message AI Thought Partner...")


# if user_input:

#     st.session_state.chat_history.append(
#         {
#             "role": "user",
#             "content": user_input
#         }
#     )

#     with st.chat_message("user"):
#         st.write(user_input)

#     with st.chat_message("assistant"):

#         with st.spinner("Thinking..."):

#             memory_data = load_memory()

#             knowledge_text = search_knowledge_base(user_input)

#             ai_response = get_ai_response(
#                 user_input,
#                 memory_data,
#                 knowledge_text
#             )

#             st.write(ai_response)

#     st.session_state.chat_history.append(
#         {
#             "role": "assistant",
#             "content": ai_response
#         }
#     )

#     save_memory(user_input, ai_response)
        



import streamlit as st

from utils.llm import get_ai_response
from utils.memory import save_memory, load_memory
from utils.rag import search_knowledge_base
from utils.resume_analyzer import extract_resume_text, analyze_resume


st.set_page_config(
    page_title="AI Thought Partner",
    page_icon="🧠",
    layout="wide"
)


AGENTS = {
    "Idea Discussion Agent": {
        "greeting": "Hello! I am your Idea Discussion Agent. Share your idea, and I will help you improve it, expand it, and make it project-ready.",
        "instruction": "You are an Idea Discussion Agent. Help the user brainstorm, improve ideas, compare options, and convert raw ideas into clear project plans."
    },
    "Career Mentor Agent": {
        "greeting": "Hello! I am your Career Mentor Agent. Tell me your career goal, and I will guide you with a practical roadmap.",
        "instruction": "You are a Career Mentor Agent. Give career guidance, skill roadmaps, project suggestions, and fresher-friendly advice."
    },
    "Daily Task Agent": {
        "greeting": "Hello! I am your Daily Task Agent. Tell me your goal, and I will give you simple daily tasks.",
        "instruction": "You are a Daily Task Agent. Give practical, beginner-friendly daily tasks that help the user make consistent progress."
    },
    "Resume Analyzer Agent": {
    "greeting": "Hello! I am your Resume Analyzer Agent. Upload your resume PDF and paste a job description. I will analyze your resume and suggest improvements.",
    "instruction": "You are a Resume Analyzer Agent. Analyze resumes against job descriptions, identify matching skills, missing skills, give ATS-style feedback, and suggest improved resume bullet points."
    },
    "Interview Preparation Agent": {
    "greeting": "Hello! I am your Interview Preparation Agent. Tell me the topic or role, and I will prepare questions and answers.",
    "instruction": "You are an Interview Preparation Agent. Ask and answer interview questions in a simple beginner-friendly way."
    }
}


st.title("🧠 AgentVerse AI")
st.caption("Multi-agent AI companion for ideas, career, tasks, resume, and interview preparation.")


with st.sidebar:
    st.header("Choose AI Agent")

    selected_agent = st.selectbox(
        "Select an agent",
        list(AGENTS.keys())
    )

    if st.button("Start New Chat"):
        st.session_state.active_agent = selected_agent
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": AGENTS[selected_agent]["greeting"]
            }
        ]

    if st.button("Clear Current Chat"):
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": AGENTS[selected_agent]["greeting"]
            }
        ]


if "active_agent" not in st.session_state:
    st.session_state.active_agent = selected_agent

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": AGENTS[selected_agent]["greeting"]
        }
    ]


if st.session_state.active_agent != selected_agent:
    st.session_state.active_agent = selected_agent
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": AGENTS[selected_agent]["greeting"]
        }
    ]


st.subheader(st.session_state.active_agent)

if st.session_state.active_agent == "Resume Analyzer Agent":
    st.info("Upload your resume PDF and paste the job description to analyze your resume.")
    uploaded_resume = st.file_uploader(
        "Upload your resume PDF",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Paste the job description here"
    )

    if st.button("Analyze Resume"):
        if uploaded_resume and job_description:
            resume_text = extract_resume_text(uploaded_resume)
            if resume_text:
                st.success("Resume text extracted successfully.")
                with st.spinner("Analyzing resume against job description..."):
                    analysis_result = analyze_resume(
                    resume_text,
                    job_description
        )

            st.subheader("Resume Analysis Result")
            st.write(analysis_result)
        else:
            st.error("Could not extract text from this PDF. Please upload a text-based resume PDF.")
    else:
        st.warning("Please upload your resume and paste the job description.")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Message your selected agent...")

if user_input:
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            memory_data = load_memory()

            knowledge_text = search_knowledge_base(user_input)

            agent_instruction = AGENTS[st.session_state.active_agent]["instruction"]

            final_prompt = f"""
{agent_instruction}

User question:
{user_input}
"""

            ai_response = get_ai_response(
                final_prompt,
                memory_data,
                knowledge_text
            )

            st.write(ai_response)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )

    save_memory(user_input, ai_response)