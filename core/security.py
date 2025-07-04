# core/security.py

from colorama import Fore
from core.config import DEFAULT_USER, DEFAULT_PASS
import datetime

def verify_user():
    """Ask for name and password. Only allows 3 attempts."""
    for attempt in range(3):
        name = input("🧾 Enter your name: ")
        pwd = input("🔑 Enter your password: ")

        if name == DEFAULT_USER and pwd == DEFAULT_PASS:
            print(Fore.GREEN + f"✅ Identity verified. Welcome, {name}.")
            return True
        else:
            print(Fore.RED + "❌ Access denied. Try again.")

    print(Fore.RED + "🚫 Too many failed attempts. Locking system.")
    return False

def self_defense(log_file, rea

