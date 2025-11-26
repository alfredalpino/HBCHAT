# 🤖 Hummingbot AI Chat Assistant

An intelligent chatbot powered by RAG (Retrieval Augmented Generation) that answers questions about Hummingbot using the official documentation.

## ✨ Features

- 💬 **Conversational AI** - Natural language Q&A about Hummingbot
- 📚 **Documentation-Grounded** - Answers based on 346 official markdown docs
- 🌐 **Web Interface** - Beautiful Gradio-based chat UI
- 💻 **CLI Interface** - Command-line chat for terminal lovers
- 🔍 **Source Citations** - Shows which docs were used for each answer
- 🧠 **Context Memory** - Remembers conversation history

## 📋 What's Inside

```
HBCHAT/
├── MD-Only/              # 346 Hummingbot markdown docs (organized by topic)
├── hummingbot_chatbot.py # Main chatbot with CLI interface
├── web_interface.py      # Web-based chat interface (Gradio)
├── loader.py            # Simple document loader script
├── requirements.txt     # Python dependencies
├── env.example          # Environment variables template
└── CHATBOT_README.md    # This file
```

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Step 2: Set Up OpenAI API Key

```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your OpenAI API key
# Get your API key from: https://platform.openai.com/api-keys
```

Your `.env` file should look like:
```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
```

### Step 3: Initialize the Chatbot (First Time Only)

This creates the vector embeddings from the documentation:

```bash
python hummingbot_chatbot.py
```

**Note:** This will:
- Load all 346 markdown files from `MD-Only/`
- Split them into chunks
- Create vector embeddings (using OpenAI)
- Save the vector store to `hummingbot_vectorstore/`
- Start an interactive CLI chat

⏱️ **First run takes ~2-5 minutes** depending on your internet speed and OpenAI API response time.

### Step 4: Use the Chatbot

#### Option A: Web Interface (Recommended)

```bash
python web_interface.py
```

Then open your browser to: **http://localhost:7860**

#### Option B: Command-Line Interface

```bash
python hummingbot_chatbot.py
```

Type your questions and get instant answers!

## 💡 Example Questions

Try asking:

- **Installation**: "How do I install Hummingbot with Docker?"
- **Strategies**: "Explain the pure market making strategy"
- **Configuration**: "How do I set up inventory skew?"
- **Exchanges**: "How do I connect to Binance?"
- **Advanced**: "What's the difference between V1 and V2 strategies?"
- **Troubleshooting**: "Why is my bot not placing orders?"
- **API**: "How do I use the Hummingbot API?"
- **Gateway**: "How do I connect to Uniswap via Gateway?"

## 🔧 Configuration Options

### Use Local Embeddings (Free, No OpenAI Required)

If you want to avoid OpenAI API costs for embeddings:

```python
# In hummingbot_chatbot.py, initialize with:
chatbot = HummingbotChatbot(use_openai=False)
```

This uses HuggingFace's free `sentence-transformers` model.

**Note:** You still need OpenAI API key for the chat LLM, or you can modify the code to use local LLMs like Ollama.

### Change the Model

Edit `hummingbot_chatbot.py` or `web_interface.py`:

```python
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",  # Cheaper option
    # model_name="gpt-4o-mini",  # Better quality
    # model_name="gpt-4",        # Best quality (expensive)
    temperature=0.7,
)
```

### Adjust Retrieval

Modify the number of source documents:

```python
retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5})  # k=5 is default
```

## 📊 Documentation Coverage

The chatbot has knowledge of:

| Category | Files | Topics |
|----------|-------|--------|
| **Strategies** | 25 | PMM, Arbitrage, V2 Strategies, Executors |
| **Exchanges** | 42 | Binance, Bybit, Kraken, Gate.io, + Gateway DEXs |
| **Installation** | 11 | Docker, Linux, Mac, Windows, Raspberry Pi |
| **Configuration** | 27 | Global configs, Strategy configs, Override |
| **Dashboard** | 7 | Deploy, Portfolio, Backtest, Credentials |
| **API** | 4 | Installation, Routers, Quickstart |
| **Blog** | 102 | Tutorials, Case Studies, Announcements |
| **Release Notes** | 44 | Version 1.0.0 to 2.10.0 |
| **Developer** | 24 | Architecture, Building Connectors/Strategies |
| **Other** | 60 | Gateway, Governance, Community, Guides |

**Total: 346 documentation files**

## 🛠️ Advanced Usage

### Load Existing Vector Store (Faster Startup)

After the first run, you can load the pre-built vector store:

```python
from hummingbot_chatbot import load_existing_vectorstore

vectorstore = load_existing_vectorstore()
```

### Programmatic Usage

```python
from hummingbot_chatbot import HummingbotChatbot

# Initialize
bot = HummingbotChatbot()

# Ask questions
result = bot.chat("How do I configure a trading pair?")
print(result['answer'])

# View sources
for doc in result['source_documents']:
    print(doc.metadata['source'])
```

### Web Interface on Public URL

To share your chatbot publicly:

```python
# In web_interface.py, change:
interface.launch(share=True)  # Creates a public gradio.live link
```

## 🐛 Troubleshooting

### "OPENAI_API_KEY not found"

Make sure you:
1. Created a `.env` file in the project root
2. Added your OpenAI API key: `OPENAI_API_KEY=sk-...`
3. The `.env` file is in the same directory as your Python scripts

### "Vector store not found"

Run `python hummingbot_chatbot.py` first to create the vector store before using the web interface.

### Out of Memory

If you get memory errors:
1. Reduce chunk size in text splitter: `chunk_size=500`
2. Use smaller embedding model
3. Process docs in batches

### Slow Responses

- Use `gpt-3.5-turbo` instead of `gpt-4o-mini`
- Reduce the number of retrieved documents: `search_kwargs={"k": 3}`
- Use local embeddings to avoid API latency

## 💰 Costs

**OpenAI API Costs** (approximate):

- **Initial Setup**: ~$0.10-0.50 (creating embeddings)
- **Per Question**: ~$0.001-0.01 (depending on model)
  - GPT-3.5-turbo: ~$0.001/question
  - GPT-4o-mini: ~$0.003-0.005/question
  - GPT-4: ~$0.01-0.03/question

**Tips to Reduce Costs:**
- Use local embeddings (`use_openai=False`)
- Use `gpt-3.5-turbo` for the chat model
- Cache the vector store (already done)
- Reduce number of retrieved docs (`k=3` instead of `k=5`)

## 🎯 Next Steps

### Enhance the Chatbot

1. **Add Streaming Responses**
   ```python
   from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
   ```

2. **Add Web Search** for latest info
   ```python
   from langchain.agents import create_openai_tools_agent
   ```

3. **Add Memory Persistence**
   ```python
   from langchain.memory import ConversationBufferWindowMemory
   ```

4. **Use Local LLM** (Ollama, LM Studio)
   ```python
   from langchain_community.llms import Ollama
   llm = Ollama(model="llama2")
   ```

5. **Add Authentication** to web interface
   ```python
   interface.launch(auth=("username", "password"))
   ```

### Deploy to Production

- **Streamlit Cloud**: Free hosting for Streamlit apps
- **Hugging Face Spaces**: Free hosting for Gradio apps
- **Railway/Render**: Easy deployment platforms
- **Docker**: Containerize the application

## 📝 License

This chatbot uses the Hummingbot documentation which is open source. Make sure to comply with Hummingbot's license terms.

## 🤝 Contributing

Feel free to enhance this chatbot:
- Add more features
- Improve prompts
- Add new interfaces (Slack, Discord, Telegram)
- Optimize performance

## 📞 Support

For Hummingbot questions: Visit the [Hummingbot Discord](https://discord.gg/hummingbot)

---

**Built with ❤️ using LangChain, OpenAI, and Gradio**

