import json
import os


MEMORY_FILE = "memory/memory_store.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as file:
            json.dump([], file)
            
    if os.path.getsize(MEMORY_FILE) == 0:
        with open(MEMORY_FILE, "w") as file:
            json.dump([], file)
            
    with open(MEMORY_FILE, "r") as file:
        memory_data = json.load(file)

    return memory_data


def save_memory(user_message, ai_response):

    memory_data = load_memory()

    conversation = {
        "user": user_message,
        "ai": ai_response
    }

    memory_data.append(conversation)

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory_data, file, indent=4)