# 🚀 Quick Start Guide - Hummingbot AI Chatbot

Get your Hummingbot AI assistant running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- ~500MB disk space

## Step-by-Step Setup

### 1️⃣ Install Dependencies

**Mac/Linux:**
```bash
./setup.sh
```

**Windows:**
```bash
setup.bat
```

**Or manually:**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 2️⃣ Configure OpenAI API Key

```bash
# Copy the example file
cp env.example .env

# Edit .env and add your key
nano .env  # or use any text editor
```

Add your OpenAI API key:
```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
```

### 3️⃣ Initialize the Chatbot

First run (creates vector embeddings - takes 2-5 minutes):

```bash
python hummingbot_chatbot.py
```

You'll see:
```
📚 Loading Hummingbot documentation...
✅ Loaded 346 documentation files
✂️  Splitting documents into chunks...
✅ Created XXXX text chunks
🔍 Creating vector embeddings...
✅ Vector store created successfully!
💾 Vector store saved to 'hummingbot_vectorstore'
🤖 Setting up QA chain...
✅ Chatbot ready!
```

### 4️⃣ Start Chatting!

**Option A - Web Interface (Recommended):**
```bash
python web_interface.py
```
Then open: http://localhost:7860

**Option B - Command Line:**
```bash
python hummingbot_chatbot.py
```

## 💬 Try These Questions

```
You: How do I install Hummingbot with Docker?
🤖: To install Hummingbot with Docker...

You: What is pure market making strategy?
🤖: Pure market making is a strategy that...

You: How do I connect to Binance?
🤖: To connect to Binance exchange...
```

## 🎯 What Can You Ask?

- **Installation & Setup**
  - "How do I install Hummingbot on Ubuntu?"
  - "What are the system requirements?"
  
- **Strategies**
  - "Explain the Avellaneda-Stoikov strategy"
  - "How does cross-exchange market making work?"
  
- **Configuration**
  - "How do I set up inventory skew?"
  - "What is kill switch and how to configure it?"
  
- **Exchanges**
  - "How to connect to Kraken?"
  - "What exchanges support perpetual trading?"
  
- **Troubleshooting**
  - "Why are my orders not getting filled?"
  - "How do I check my bot's status?"
  
- **Advanced**
  - "What's the difference between V1 and V2 strategies?"
  - "How do I use the Dashboard to backtest?"

## 📁 Project Structure

```
HBCHAT/
├── MD-Only/              # 📚 346 Hummingbot docs
├── hummingbot_vectorstore/ # 🧠 Vector embeddings (auto-generated)
│
├── hummingbot_chatbot.py # 🤖 Main chatbot (CLI)
├── web_interface.py      # 🌐 Web UI (Gradio)
├── loader.py            # 📄 Simple doc loader
│
├── requirements.txt     # 📦 Python packages
├── env.example          # 🔑 API key template
├── .env                 # 🔐 Your API key (create this)
│
├── setup.sh            # 🛠️ Auto setup (Mac/Linux)
├── setup.bat           # 🛠️ Auto setup (Windows)
│
├── CHATBOT_README.md   # 📖 Full documentation
└── QUICKSTART.md       # ⚡ This file
```

## 🐛 Common Issues

### "OPENAI_API_KEY not found"
- Make sure `.env` file exists in the project root
- Check that your API key is correctly formatted
- Verify the key starts with `sk-`

### "Vector store not found"
- Run `python hummingbot_chatbot.py` first to create it
- This only needs to be done once

### "Module not found"
- Activate virtual environment: `source venv/bin/activate`
- Reinstall: `pip install -r requirements.txt`

### Slow response times
- Switch to gpt-3.5-turbo (edit the model_name in the code)
- Check your internet connection
- OpenAI API might be slow during peak hours

## 💰 Cost Estimate

Using OpenAI API with gpt-4o-mini:
- **Setup**: $0.10-0.50 (one-time)
- **Per chat session**: $0.01-0.05 (10-20 questions)
- **Monthly** (moderate use): $5-15

Tips to reduce costs:
- Use `gpt-3.5-turbo` (cheaper)
- Use local embeddings (`use_openai=False`)
- Batch your questions

## 🚀 Next Steps

1. **Customize the prompt** - Edit system prompts in the code
2. **Deploy to web** - Use Gradio Spaces or Streamlit Cloud
3. **Add more docs** - Drop more markdown files into MD-Only/
4. **Integrate** - Add to Discord, Slack, or your app
5. **Go local** - Use Ollama for fully local LLM

## 📚 Full Documentation

For advanced features, troubleshooting, and customization:
- See `CHATBOT_README.md`

## 🤝 Need Help?

- Hummingbot Discord: https://discord.gg/hummingbot
- OpenAI Help: https://help.openai.com

---

**Happy chatting! 🎉**

