#!/bin/bash

echo "🚀 Setting up Hummingbot AI Chatbot with Conda..."
echo ""

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ Conda is not installed!"
    echo "Please install Miniconda or Anaconda first:"
    echo "  - Miniconda: https://docs.conda.io/en/latest/miniconda.html"
    echo "  - Anaconda: https://www.anaconda.com/download"
    exit 1
fi

echo "✅ Conda found: $(conda --version)"
echo ""

# Create conda environment
echo "🔧 Creating conda environment 'hbchat'..."
conda env create -f environment.yml

if [ $? -ne 0 ]; then
    echo "❌ Failed to create conda environment"
    exit 1
fi

echo "✅ Conda environment 'hbchat' created successfully!"
echo ""

# Activate environment
echo "🔌 Activating conda environment..."
echo ""
echo "⚠️  IMPORTANT: Run the following command to activate the environment:"
echo ""
echo "   conda activate hbchat"
echo ""
echo "Then verify your .env file has the OpenRouter API key:"
echo "   cat .env"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    if [ -f env.example ]; then
        cp env.example .env
        echo "✅ .env file created"
        echo ""
        echo "⚠️  Don't forget to add your OpenRouter API key to .env!"
    fi
else
    echo "✅ .env file already exists"
fi

echo ""
echo "=" * 60
echo "🎉 Setup complete!"
echo "=" * 60
echo ""
echo "Next steps:"
echo "1. Activate the environment:"
echo "   conda activate hbchat"
echo ""
echo "2. Verify your API key in .env file:"
echo "   cat .env"
echo ""
echo "3. Initialize the chatbot (first time only):"
echo "   python hummingbot_chatbot.py"
echo ""
echo "4. Start the web interface:"
echo "   python web_interface.py"
echo ""
echo "For detailed instructions, see README.md"
echo ""

