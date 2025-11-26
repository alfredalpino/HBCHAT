# 🤖 Hummingbot AI Chat Assistant

<div align="center">

![Hummingbot](https://img.shields.io/badge/Hummingbot-AI%20Assistant-00D4FF?style=for-the-badge&logo=robot)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Enabled-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache%202.0-yellow?style=for-the-badge)

**An intelligent AI chatbot powered by RAG (Retrieval Augmented Generation) that answers questions about Hummingbot using the complete official documentation.**

[Quick Start](#-quick-start) •
[Features](#-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[Documentation](#-documentation)

</div>

---

## 🎯 What is This?

The **Hummingbot AI Chat Assistant** is an advanced conversational AI that provides instant, accurate answers to any questions about Hummingbot - the open-source crypto trading bot platform. Built using state-of-the-art LangChain and OpenRouter technologies, it has deep knowledge of:

- ✅ **346 Documentation Files** - Complete Hummingbot documentation
- ✅ **All Trading Strategies** - PMM, Arbitrage, Cross-Exchange, V2 Strategies
- ✅ **40+ Exchanges** - CEX and DEX connectors
- ✅ **Installation & Setup** - Docker, Linux, Mac, Windows, Raspberry Pi
- ✅ **Configuration Guides** - Every parameter and setting explained
- ✅ **Developer Documentation** - Build custom strategies and connectors
- ✅ **102 Blog Posts** - Tutorials, case studies, and guides

## ✨ Features

### 🧠 **Intelligent Question Answering**
- Natural language understanding
- Context-aware responses
- Conversation memory for follow-up questions
- Source citations for every answer

### 🎨 **Multiple Interfaces**
- **Web UI** - Beautiful Gradio-based chat interface
- **CLI** - Terminal-based interactive chat
- **API Ready** - Easy to integrate into other applications

### 🚀 **Powered by OpenRouter**
- Access to multiple AI models (Claude, GPT-4, Llama, Gemini)
- Flexible model selection
- Cost-effective pricing
- Free models available for testing

### 📚 **Comprehensive Knowledge Base**
- **Strategies**: Pure Market Making, Arbitrage, Avellaneda-Stoikov, and more
- **Exchanges**: Binance, Bybit, Kraken, Gate.io, Uniswap, PancakeSwap, etc.
- **Dashboard**: Deployment, backtesting, portfolio management
- **API**: Hummingbot API documentation
- **Gateway**: DEX connector setup and usage
- **V2 Strategies**: Latest framework and executors

## 🚀 Quick Start

### Prerequisites
- **Conda** (Miniconda or Anaconda) - [Download here](https://docs.conda.io/en/latest/miniconda.html)
- OpenRouter API key ([Get one free](https://openrouter.ai/))

### Installation with Conda (Recommended - 3 Steps!)

#### Step 1: Create Conda Environment

**Mac/Linux:**
```bash
./setup_conda.sh
```

**Windows:**
```bash
setup_conda.bat
```

**Or manually:**
```bash
conda env create -f environment.yml
```

#### Step 2: Activate Environment

```bash
conda activate hbchat
```

#### Step 3: Initialize and Start Chatting

```bash
# First time: Initialize (creates vector embeddings - takes 3-5 minutes)
python hummingbot_chatbot.py

# Or start web interface directly
python web_interface.py
```

That's it! The chatbot will load all documentation, create embeddings, and start an interactive chat session.

### Web Interface

For a better experience, use the web interface:

```bash
conda activate hbchat
python web_interface.py
```

Then open: **http://localhost:7860**

## 📦 Installation

### Option 1: Conda Environment (Recommended) ⭐

Conda ensures all dependencies are properly isolated and compatible. This is the **recommended method**.

#### Automated Setup

**Mac/Linux:**
```bash
./setup_conda.sh
conda activate hbchat
```

**Windows:**
```bash
setup_conda.bat
conda activate hbchat
```

#### Manual Setup

```bash
# 1. Create conda environment from environment.yml
conda env create -f environment.yml

# 2. Activate the environment
conda activate hbchat

# 3. Verify installation
python -c "import langchain_community; print('✅ All packages installed!')"

# 4. Your OpenRouter API key is already configured in .env
# If you need to change it, edit the .env file

# 5. Initialize chatbot (first time only)
python hummingbot_chatbot.py
```

#### Managing the Conda Environment

```bash
# Activate environment (do this every time you work on the project)
conda activate hbchat

# Deactivate when done
conda deactivate

# Remove environment (if needed)
conda env remove -n hbchat

# Update environment
conda env update -f environment.yml --prune
```

### Option 2: Python Virtual Environment (Alternative)

If you prefer not to use Conda:

**Mac/Linux:**
```bash
./setup.sh
source venv/bin/activate
```

**Windows:**
```bash
setup.bat
venv\Scripts\activate
```

**Or manually:**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Your OpenRouter API key is already configured in .env
# If you need to change it, edit the .env file

# Initialize chatbot
python hummingbot_chatbot.py
```

## 💬 Usage

### Example Questions

**Installation & Setup:**
```
How do I install Hummingbot with Docker?
What are the system requirements for Hummingbot?
How to run Hummingbot on Raspberry Pi?
```

**Trading Strategies:**
```
What is the pure market making strategy?
Explain the Avellaneda-Stoikov strategy
How does cross-exchange market making work?
What's the difference between V1 and V2 strategies?
```

**Configuration:**
```
How do I configure inventory skew?
What is the kill switch and how to enable it?
How to set up order refresh tolerance?
Explain hanging orders configuration
```

**Exchange Setup:**
```
How do I connect to Binance?
What exchanges support perpetual futures?
How to set up Gateway for Uniswap?
Does Hummingbot support Kraken?
```

**Troubleshooting:**
```
Why are my orders not getting filled?
How do I check my bot's performance?
What should I do if the bot stops unexpectedly?
How to read log files?
```

**Advanced Topics:**
```
How do I create a custom strategy?
What is the Dashboard and how to use it?
How to backtest a strategy?
Explain the V2 executor framework
```

### CLI Interface

```bash
$ python hummingbot_chatbot.py

🤖 HUMMINGBOT AI CHAT ASSISTANT
============================================================
Ask me anything about Hummingbot!
Type 'quit', 'exit', or 'bye' to end the conversation.
============================================================

You: How do I install Hummingbot with Docker?
🤖 Assistant: To install Hummingbot with Docker, follow these steps...
```

### Web Interface

```bash
$ python web_interface.py

Running on local URL:  http://0.0.0.0:7860
```

Beautiful chat interface with:
- Message history
- Source citations
- Code highlighting
- Easy copy/paste

## ⚙️ Configuration

### OpenRouter Models

Your chatbot is configured to use **Claude 3.5 Sonnet** by default. To change models, edit the `model_name` in:

**hummingbot_chatbot.py** (line ~104):
```python
model_name="anthropic/claude-3.5-sonnet"  # Current
# model_name="openai/gpt-4o-mini"        # Cheaper
# model_name="meta-llama/llama-3.1-8b-instruct"  # Very cheap
```

### Available Models

| Model | Cost | Quality | Best For |
|-------|------|---------|----------|
| Claude 3.5 Sonnet | $$$ | Excellent | Complex questions, best accuracy |
| GPT-4o Mini | $$ | Great | Balanced performance |
| Llama 3.1 70B | $$ | Great | Open source, good quality |
| Llama 3.1 8B | $ | Good | Budget-friendly |
| Llama 3.2 3B | **FREE** | Fair | Testing, development |

See [OPENROUTER_GUIDE.md](OPENROUTER_GUIDE.md) for complete model list and switching instructions.

### Environment Variables

Edit `.env` to configure:

```bash
# OpenRouter API Key (Required)
OPENAI_API_KEY=sk-or-v1-your-key-here

# OpenRouter API Base URL
OPENAI_API_BASE=https://openrouter.ai/api/v1

# App Name (Optional)
OPENROUTER_APP_NAME=Hummingbot-AI-Chat
```

## 📊 Project Structure

```
HBCHAT/
├── MD-Only/                    # 📚 346 Hummingbot markdown docs
│   ├── about/                  # About Hummingbot
│   ├── academy/                # Educational content
│   ├── blog/                   # 102 blog posts
│   ├── strategies/             # Strategy guides
│   ├── exchanges/              # Exchange connectors
│   ├── installation/           # Setup guides
│   ├── dashboard/              # Dashboard docs
│   ├── v2-strategies/          # V2 framework
│   └── ...                     # And much more!
│
├── hummingbot_vectorstore/     # 🧠 Vector embeddings (auto-generated)
│
├── hummingbot_chatbot.py       # 🤖 Main chatbot (CLI)
├── web_interface.py            # 🌐 Web UI (Gradio)
├── loader.py                   # 📄 Document loader
│
├── environment.yml             # 🐍 Conda environment file (RECOMMENDED)
├── requirements.txt            # 📦 Python dependencies (venv alternative)
├── .env                        # 🔑 API configuration
├── env.example                 # 🔑 API key template
│
├── setup_conda.sh              # 🛠️ Conda setup (Mac/Linux) ⭐
├── setup_conda.bat             # 🛠️ Conda setup (Windows) ⭐
├── setup.sh                    # 🛠️ Venv setup (Mac/Linux)
├── setup.bat                   # 🛠️ Venv setup (Windows)
│
├── README.md                   # 📖 This file
├── QUICKSTART.md               # ⚡ Fast setup guide
├── CHATBOT_README.md           # 📚 Complete documentation
├── OPENROUTER_GUIDE.md         # 🌐 OpenRouter usage guide
├── START_HERE.md               # 🎯 Getting started guide
└── CONTRIBUTING.md             # 🤝 Contribution guidelines
```

## 💰 Cost Estimate

Using OpenRouter with Claude 3.5 Sonnet:

| Usage | Estimated Cost |
|-------|---------------|
| Initial Setup (one-time) | $0.10 - $0.30 |
| Per Question | $0.003 - $0.005 |
| 100 Questions | ~$0.50 |
| Monthly (moderate use) | $5 - $15 |

**Want it cheaper?**
- Switch to Llama 3.1 8B: ~$0.001/question
- Use free models: Llama 3.2 3B (FREE!)

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[START_HERE.md](START_HERE.md)** - Simple step-by-step guide
- **[CHATBOT_README.md](CHATBOT_README.md)** - Complete documentation
- **[OPENROUTER_GUIDE.md](OPENROUTER_GUIDE.md)** - Model selection and usage

## 🛠️ Technology Stack

- **LangChain** - LLM application framework
- **OpenRouter** - Multi-model API gateway
- **FAISS** - Vector similarity search
- **OpenAI Embeddings** - Text embeddings
- **Gradio** - Web interface
- **Python 3.8+** - Programming language

## 🎯 Use Cases

### For Traders
- Quick answers while setting up bots
- Strategy explanations and comparisons
- Configuration assistance
- Troubleshooting help

### For Developers
- API documentation reference
- Custom strategy development
- Connector building guides
- Architecture understanding

### For Beginners
- Learn about trading bots
- Understand market making
- Step-by-step setup guides
- Concept explanations

### For Teams
- Onboarding new members
- Internal knowledge base
- 24/7 documentation access
- Consistent answers

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Add More Documents** - Drop markdown files into `MD-Only/`
2. **Improve Prompts** - Enhance system prompts for better answers
3. **Add Features** - Streaming responses, chat history, etc.
4. **Fix Bugs** - Report issues or submit PRs
5. **Improve UI** - Enhance the web interface

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 🐛 Troubleshooting

### "Module not found" errors (langchain_community, etc.)

**If using Conda (Recommended):**
```bash
# Make sure you're in the conda environment
conda activate hbchat

# Verify you're using the right Python
which python  # Should show path with 'hbchat' in it

# Reinstall if needed
conda env update -f environment.yml --prune
```

**If using venv:**
```bash
# Activate virtual environment first
source venv/bin/activate  # Windows: venv\Scripts\activate

# Then install
pip install -r requirements.txt
```

### "OPENAI_API_KEY not found"
```bash
# Check if .env file exists
cat .env  # Mac/Linux
type .env  # Windows

# If not, create it:
cp env.example .env  # Mac/Linux
copy env.example .env  # Windows

# Then add your OpenRouter API key to .env
```

### "Vector store not found"
```bash
# Make sure you're in the conda environment
conda activate hbchat

# Run the chatbot once to create it
python hummingbot_chatbot.py
```

### Conda environment issues

**Environment not activating:**
```bash
# List all environments
conda env list

# If hbchat doesn't exist, create it
conda env create -f environment.yml

# Activate it
conda activate hbchat
```

**Wrong Python version:**
```bash
# Check Python version in environment
conda activate hbchat
python --version  # Should be 3.10

# Recreate with correct version
conda env remove -n hbchat
conda env create -f environment.yml
```

**Packages not installing:**
```bash
# Update conda first
conda update conda

# Then recreate environment
conda env remove -n hbchat
conda env create -f environment.yml
```

### Slow responses
- Switch to a faster model (Llama 3.1 8B)
- Check your internet connection
- Reduce the number of retrieved documents (edit code: `k=3`)

### Wrong or incomplete answers
- Try Claude 3.5 Sonnet for best accuracy
- Be more specific in your questions
- Ask follow-up questions for clarification

## 🚀 Roadmap

- [ ] Add streaming responses for real-time output
- [ ] Implement persistent conversation history
- [ ] Add multi-language support
- [ ] Create Discord/Slack/Telegram bots
- [ ] Add voice input/output
- [ ] Implement user feedback system
- [ ] Add analytics dashboard
- [ ] Docker containerization
- [ ] API endpoint for integration

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hummingbot Foundation** - For the amazing trading bot platform and documentation
- **OpenRouter** - For providing access to multiple AI models
- **LangChain** - For the powerful LLM framework
- **Anthropic, OpenAI, Meta** - For their incredible AI models

## 📞 Support

- **Hummingbot Discord**: [https://discord.gg/hummingbot](https://discord.gg/hummingbot)
- **OpenRouter Discord**: [https://discord.gg/openrouter](https://discord.gg/openrouter)
- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)

## ⭐ Show Your Support

If you find this project helpful, please consider:
- Starring this repository ⭐
- Sharing it with others 📢
- Contributing improvements 🛠️
- Reporting bugs 🐛

---

<div align="center">

**Built with ❤️ for the Hummingbot Community**

[Hummingbot Website](https://hummingbot.org) • [Documentation](https://docs.hummingbot.org) • [Discord](https://discord.gg/hummingbot)

</div>
