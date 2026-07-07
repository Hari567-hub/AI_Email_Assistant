import json
import os

MEMORY_FILE = "processed.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def is_processed(message_id):
    memory = load_memory()
    return message_id in memory


def mark_processed(message_id):
    memory = load_memory()

    if message_id not in memory:
        memory.append(message_id)
        save_memory(memory)