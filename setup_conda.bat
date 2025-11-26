@echo off
echo 🚀 Setting up Hummingbot AI Chatbot with Conda...
echo.

REM Check if conda is installed
where conda >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Conda is not installed!
    echo Please install Miniconda or Anaconda first:
    echo   - Miniconda: https://docs.conda.io/en/latest/miniconda.html
    echo   - Anaconda: https://www.anaconda.com/download
    pause
    exit /b 1
)

echo ✅ Conda found
conda --version
echo.

REM Create conda environment
echo 🔧 Creating conda environment 'hbchat'...
conda env create -f environment.yml

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to create conda environment
    pause
    exit /b 1
)

echo ✅ Conda environment 'hbchat' created successfully!
echo.

REM Check if .env exists
if not exist .env (
    echo 📝 Creating .env file from template...
    if exist env.example (
        copy env.example .env
        echo ✅ .env file created
        echo.
        echo ⚠️  Don't forget to add your OpenRouter API key to .env!
    )
) else (
    echo ✅ .env file already exists
)

echo.
echo ============================================================
echo 🎉 Setup complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Activate the environment:
echo    conda activate hbchat
echo.
echo 2. Verify your API key in .env file:
echo    type .env
echo.
echo 3. Initialize the chatbot (first time only):
echo    python hummingbot_chatbot.py
echo.
echo 4. Start the web interface:
echo    python web_interface.py
echo.
echo For detailed instructions, see README.md
echo.
pause

