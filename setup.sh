#!/bin/bash

echo "🚀 Setting up Hummingbot AI Chatbot..."
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found Python $python_version"

# Create virtual environment
echo ""
echo "🔧 Creating virtual environment..."
python3 -m venv venv
echo "   ✅ Virtual environment created"

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate
echo "   ✅ Virtual environment activated"

# Install requirements
echo ""
echo "📦 Installing dependencies (this may take a few minutes)..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "   ✅ Dependencies installed"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "📝 Creating .env file..."
    cp env.example .env
    echo "   ✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your OpenAI API key!"
    echo "   Get your API key from: https://platform.openai.com/api-keys"
    echo ""
    echo "   Open .env file and replace 'your_openai_api_key_here' with your actual key"
else
    echo ""
    echo "✅ .env file already exists"
fi

echo ""
echo "=" * 60
echo "🎉 Setup complete!"
echo "=" * 60
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OpenAI API key"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python hummingbot_chatbot.py (first time setup)"
echo "4. Run: python web_interface.py (web UI)"
echo ""
echo "For detailed instructions, see CHATBOT_README.md"
echo ""

