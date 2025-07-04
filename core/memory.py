# core/memory.py

import json
from colorama import Fore
from core.config import MEMORY_PATH

def load_memory():
    try:
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ No memory file found. Starting fresh.")
        return {}

def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=4)
    print(Fore.LIGHTGREEN_EX + "💾 Memory saved.")

def teach(command, memory):
    parts = command.split(maxsplit=2)
    if len(parts) < 3:
        print("🧠 Usage: teach [key] [value]")
    else:
        key, value = parts[1], parts[2]
        memory[key] = value
        print(f"🧠 Learned: {key} = {value}")
        save_memory(memory)

def recall(command, memory):
    parts = command.split(maxsplit=1)
    if len(parts) < 2:
        print("👁️ Usage: recall [key]")
    else:
        key = parts[1]
        if key in memory:
            print(f"👁️ {key} = {memory[key]}")
        else:
            print(f"🧠 I don’t know anything about “{key}”.")

