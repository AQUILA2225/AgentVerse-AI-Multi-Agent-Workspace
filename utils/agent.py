from utils.llm import get_ai_response

def generate_learning_roadmap(career_goal, memory_data=None, knowledge_text=""):
    roadmap_prompt = f"""
    Create a detailed beginner-friendly roadmap for this goal:
    {career_goal}
    
    The roadmap should include:
    - learning stages
    - important technologies
    - project ideas
    - practice suggestions
    - interview preparation tips

    Give the roadmap step-by-step.
    """

    roadmap = get_ai_response(
        roadmap_prompt,
        memory_data,
        knowledge_text
        )
    return roadmap

def generate_daily_tasks(goal, memory_data=None, knowledge_text = ""):
    task_prompt = f""" 
    Genertae practical dailt tasks for this goal:
    {goal}
    
    Rules:
    - tasks should be beginner-friendly
    - tasks should be practical
    - tasks should help consistency
    - tasks should improve AI/GenAI skills

    Give only 5 tasks.
    """
    
    tasks = get_ai_response(
        task_prompt,
        memory_data,
        knowledge_text
    )
    return tasks 
