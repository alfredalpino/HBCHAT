@echo off
echo 🚀 Setting up Hummingbot AI Chatbot...
echo.

REM Check Python
echo 📋 Checking Python version...
python --version
echo.

REM Create virtual environment
echo 🔧 Creating virtual environment...
python -m venv venv
echo    ✅ Virtual environment created
echo.

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate
echo    ✅ Virtual environment activated
echo.

REM Install requirements
echo 📦 Installing dependencies (this may take a few minutes)...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo    ✅ Dependencies installed
echo.

REM Create .env file
if not exist .env (
    echo 📝 Creating .env file...
    copy env.example .env
    echo    ✅ .env file created
    echo.
    echo ⚠️  IMPORTANT: Edit .env file and add your OpenAI API key!
    echo    Get your API key from: https://platform.openai.com/api-keys
    echo.
) else (
    echo ✅ .env file already exists
    echo.
)

echo ============================================================
echo 🎉 Setup complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Edit .env file and add your OpenAI API key
echo 2. Run: venv\Scripts\activate
echo 3. Run: python hummingbot_chatbot.py (first time setup)
echo 4. Run: python web_interface.py (web UI)
echo.
echo For detailed instructions, see CHATBOT_README.md
echo.
pause

