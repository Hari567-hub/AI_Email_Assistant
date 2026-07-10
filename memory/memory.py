"""
Manage processed email IDs.

This module stores the IDs of emails that have already
been processed so they are not analyzed again.
"""        
import json
import os

MEMORY_FILE = "processed.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_memory(memory):
    try:
        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file, indent=4)
    except OSError:
        pass


def is_processed(message_id):
    memory = load_memory()
    return message_id in memory


def mark_processed(message_id):
    memory = load_memory()

    if message_id not in memory:
        memory.append(message_id)
        save_memory(memory)