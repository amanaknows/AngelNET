# AngelNET Secure Terminal v3.0

### 🧬 Built by Angelica | Core Security + Memory + Profile Access

---

## Overview

AngelNET is a secure terminal chatbot interface designed to:

* Run commands interactively
* Store and recall user-defined knowledge (memory)
* Manage user profiles with rank and mode
* Protect with multi-step verification and defensive lockdown protocols
* Modular, easy-to-extend Python codebase

---

## Features

* Secure login with 3 attempts limit
* Command handling with help, status, greet, and custom commands
* Persistent user memory saved to JSON files
* Profile viewing and updating commands
* Defensive self-defense mode for security threats
* Colorized terminal output with `colorama`
* Modular code organized in `core/` for easy maintenance

---

## Setup & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/angelnet.git
   cd angelnet
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   .\venv\Scripts\activate     # Windows PowerShell
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the terminal:

   ```bash
   python angelnet_terminal.py
   ```

---

## Usage

* Use `help` command to see available commands
* `teach [key] [value]` to add memory
* `recall [key]` to retrieve stored memory
* `profile` to view your profile
* `update [field] [new_value]` to change profile fields
* `access-omega` for restricted secure access (password required)
* `disconnect` or `exit` to safely exit AngelNET

---

## Project Structure

```
angelnet/
├── core/               # Modular Python code for memory, profile, security, handlers, and config
├── data/               # Persistent JSON files for memory and profile, plus logs
├── angelnet_terminal.py  # Main program entry point
├── README.md
└── venv/               # Python virtual environment (excluded from Git)
```

---

## Contributing

Feel free to open issues or submit pull requests to improve AngelNET! Suggestions for AI integration, front-end UI, or expanded security features are very welcome.

---

## License

MULTI-VERSAL LICENSE

