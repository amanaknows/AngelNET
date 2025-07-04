# angelnet_terminal.py

import datetime
from colorama import init, Fore
from core import memory, profile, config, security, handlers

# Init color
init(autoreset=True)

# Load memory + profile
user_memory = memory.load_memory()
angelnet_profile = profile.load_profile()

# Start Terminal
print(Fore.CYAN + "🔐 AngelNET Secure Terminal v3.0")

if not security.verify_user():
    exit()

print(Fore.GREEN + f"Session started at {datetime.datetime.now()}")
print(Fore.YELLOW + "Type 'help' for commands. Type 'exit' to quit.\n")

command_count = 0
log_file = open(config.LOG_PATH, "a")

# Loop
while True:
    user_input = input(Fore.WHITE + ">> Enter command: ")
    command_count += 1
    timestamp = datetime.datetime.now()
    log_file.write(f"[{timestamp}] Command #{command_count}: {user_input}\n")

    if user_input == "status":
        handlers.handle_status()
    elif user_input == "greet":
        handlers.handle_greet()
    elif user_input == "help":
        handlers.handle_help()
    elif user_input in ["disconnect", "exit"]:
        handlers.handle_disconnect(log_file, timestamp)
        break
    elif user_input == "":
        print(Fore.YELLOW + "⚠️ No input detected.")
        continue
    elif user_input == "access-omega":
        confirm = input("🔑 Re-enter password for Omega Access: ")
        if confirm == config.DEFAULT_PASS:
            handlers.handle_secret()
        else:
            print(Fore.RED + "🚫 Access denied. Omega core locked.")
    elif user_input in ["intruder", "breach", "override"]:
        security.self_defense(log_file, reason=user_input)
        break
    elif user_input.startswith("teach "):
        memory.teach(user_input, user_memory)
    elif user_input.startswith("recall "):
        memory.recall(user_input, user_memory)
    elif user_input == "profile":
        profile.show_profile(angelnet_profile)
    elif user_input.startswith("update "):
        parts = user_input.split(maxsplit=2)
        if len(parts) < 3:
            print("✏️ Usage: update [field] [new_value]")
        else:
            field, new_value = parts[1], parts[2]
            angelnet_profile[field] = new_value
            profile.save_profile(angelnet_profile)
            print(f"📝 Updated {field} to '{new_value}'")
    else:
        handlers.handle_unknown()

# Save
memory.save_memory(user_memory)
profile.save_profile(angelnet_profile)
log_file.close()

