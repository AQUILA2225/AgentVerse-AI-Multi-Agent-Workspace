from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("groq_api_key")

llm=ChatOpenAI(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
    
)

def get_ai_response(user_message, memory_data=None, knowledge_text=""):

    memory_text = ""

    if memory_data:
        for conversation in memory_data[-5:]:
            memory_text += f"User: {conversation['user']}\n"
            memory_text += f"AI: {conversation['ai']}\n\n"

    idea_keywords = [
        "idea",
        "startup",
        "project idea",
        "thinking",
        "confused",
        "plan",
        "career",
        "brainstorm",
        "should i",
        "what do you think"
    ]

    is_idea_discussion = any(
        keyword in user_message.lower()
        for keyword in idea_keywords
    )

    if is_idea_discussion:

        style_instruction = """
        You are in friendly idea-discussion mode.
        Rules:
        - Reply like a close friend or thinking partner.
        - Do NOT give lists.
        - Do NOT give numbered points.
        - Do NOT explain everything at once.
        - Reply in only 2 to 4 short sentences.
        - Ask only ONE simple follow-up question.
        - Sound natural, warm, and curious.
        - First understand the idea before giving suggestions.
        - Do not use formal phrases like "Can you share more details such as".
        - Do not mention validation, MVP, market, roadmap, or strategy unless the user asks.

        Example style:
"That sounds interesting! What kind of AI startup are you thinking about — something for students, businesses, healthcare, or daily life?"

"""

    else:

        style_instruction = """
Give clear, structured, beginner-friendly responses.
Explain in detail when needed.
Provide practical guidance and examples.
"""

    prompt = f"""
You are an AI Thought Partner.

Your role is to:
- remember the user's goals
- help the user think clearly
- suggest practical next steps
- give career, learning, and project guidance

Previous conversation memory:
{memory_text}

Relevant knowledge from user's notes:
{knowledge_text}

Current user question:
{user_message}

Response Style:
{style_instruction}
"""

    response = llm.invoke(prompt)

    return response.content