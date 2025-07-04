# core/profile.py

import json
from colorama import Fore
from core.config import PROFILE_PATH, DEFAULT_USER, DEFAULT_RANK, DEFAULT_MODE

def load_profile():
    try:
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ No profile found. Starting fresh.")
        return {
            "user": DEFAULT_USER,
            "rank": DEFAULT_RANK,
            "mode": DEFAULT_MODE
        }

def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=4)
    print(Fore.LIGHTGREEN_EX + "💾 Profile saved.")

def show_profile(profile):
    print(Fore.CYAN + "\n📇 AngelNET Operator Profile:")
    for key, value in profile.items():
        print(f"• {key}: {value}")

