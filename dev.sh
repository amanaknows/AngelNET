#!/bin/bash

#!/bin/bash

echo ""
echo "🔐 Welcome to AngelNET Development Shell"
echo "🔄 Checking environment..."

# Step 1: Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment activated."
else
    echo "❌ No virtual environment found. Please run:"
    echo "   python3 -m venv venv"
    exit 1
fi

# Step 2: Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing Python dependencies..."
    pip install -r requirements.txt
else
    echo "⚠️  requirements.txt not found."
    echo "📝 Creating one now from current environment..."
    pip freeze > requirements.txt
    echo "✅ Created requirements.txt"
fi

# Step 3: Prepare log folder and file
LOG_DIR="logs"
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date +"%Y-%m-%d--%H-%M-%S")
LOG_FILE="$LOG_DIR/session-$TIMESTAMP.log"

echo ""
echo "🗂️  Saving session log to: $LOG_FILE"

# Step 4: Run AngelNET with logging
echo ""
echo "🚀 Launching AngelNET Terminal..."
python angelnet_terminal.py 2>&1 | tee "$LOG_FILE"

# Step 5: Wrap up
echo ""
echo "🛑 AngelNET session closed. Deactivating virtual environment..."
deactivate
