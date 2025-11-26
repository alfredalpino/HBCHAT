# 🌐 Using OpenRouter with Hummingbot AI Chatbot

Your chatbot is now configured to use **OpenRouter**, which gives you access to multiple AI models through a single API!

## ✅ Configuration Complete

Your `.env` file has been set up with:
- ✅ OpenRouter API Key
- ✅ OpenRouter API Base URL
- ✅ App identification

## 🎯 Available Models

OpenRouter gives you access to many models. Your chatbot is currently configured to use **Claude 3.5 Sonnet** (Anthropic), but you can easily change it!

### Recommended Models:

| Model | Code | Cost | Best For |
|-------|------|------|----------|
| **Claude 3.5 Sonnet** | `anthropic/claude-3.5-sonnet` | $$$ | Best quality, great reasoning |
| **GPT-4o Mini** | `openai/gpt-4o-mini` | $$ | Good balance of cost/quality |
| **GPT-3.5 Turbo** | `openai/gpt-3.5-turbo` | $ | Cheapest, fast responses |
| **Llama 3.1 70B** | `meta-llama/llama-3.1-70b-instruct` | $$ | Open source, good quality |
| **Llama 3.1 8B** | `meta-llama/llama-3.1-8b-instruct` | $ | Very cheap, decent quality |
| **Gemini Pro** | `google/gemini-pro` | $$ | Google's model |

View all models: https://openrouter.ai/models

## 🔧 How to Change Models

### Option 1: Edit the Python files

**In `hummingbot_chatbot.py` (line ~104):**
```python
llm = ChatOpenAI(
    model_name="anthropic/claude-3.5-sonnet",  # Change this line
    temperature=0.7,
    openai_api_base=api_base,
    ...
)
```

**In `web_interface.py` (line ~52):**
```python
llm = ChatOpenAI(
    model_name="anthropic/claude-3.5-sonnet",  # Change this line
    temperature=0.7,
    openai_api_base=api_base,
    ...
)
```

### Option 2: Quick Model Switch Examples

**For cheaper operation (Llama 3.1 8B):**
```python
model_name="meta-llama/llama-3.1-8b-instruct"
```

**For OpenAI GPT-4o-mini:**
```python
model_name="openai/gpt-4o-mini"
```

**For free models:**
```python
model_name="meta-llama/llama-3.2-3b-instruct:free"
```

## 💰 Cost Comparison

Approximate costs per 1000 questions:

| Model | Cost per 1K questions | Quality |
|-------|----------------------|---------|
| Llama 3.1 8B | ~$0.50 | Good |
| GPT-3.5 Turbo | ~$1.00 | Good |
| GPT-4o Mini | ~$3.00 | Great |
| Llama 3.1 70B | ~$5.00 | Great |
| Claude 3.5 Sonnet | ~$10.00 | Excellent |

## 🚀 Quick Start (OpenRouter Edition)

### 1. Check Your Configuration
```bash
cat .env
```

Should show:
```
OPENAI_API_KEY=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
OPENAI_API_BASE=https://openrouter.ai/api/v1
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Chatbot (First Time)
```bash
python hummingbot_chatbot.py
```

This will:
- Load 346 documentation files
- Create embeddings using OpenRouter
- Save the vector store
- Start interactive chat

### 4. Use Web Interface
```bash
python web_interface.py
```

Open: http://localhost:7860

## 🎯 OpenRouter Benefits

✅ **Access to Multiple Models** - Switch between OpenAI, Anthropic, Meta, Google  
✅ **Single API Key** - One key for all models  
✅ **Pay As You Go** - No subscriptions needed  
✅ **Free Tier Available** - Some models are free  
✅ **Better Rate Limits** - Often more generous than direct API  
✅ **Automatic Failover** - Falls back if a model is down  

## 📊 Monitor Your Usage

Check your usage at: https://openrouter.ai/activity

## 🔐 Security Note

Your API key is stored in `.env` which is:
- ✅ Ignored by git (won't be committed)
- ✅ Local to your machine
- ✅ Never shared in the code

**Never share your API key publicly!**

## 🐛 Troubleshooting

### "Invalid API key"
- Check your key is correct in `.env`
- Make sure it starts with `sk-or-v1-`
- Verify at: https://openrouter.ai/keys

### "Model not found"
- Check the model name at: https://openrouter.ai/models
- Ensure you're using the full path (e.g., `anthropic/claude-3.5-sonnet`)

### "Rate limit exceeded"
- You've hit OpenRouter's rate limit
- Wait a few seconds and try again
- Consider upgrading your OpenRouter credits

### Slow responses
- Try a smaller/faster model (Llama 3.1 8B)
- Check your internet connection
- OpenRouter might be experiencing high load

## 💡 Pro Tips

1. **Start with a cheap model** (Llama 8B) to test, then upgrade
2. **Use free models** for development: `meta-llama/llama-3.2-3b-instruct:free`
3. **Monitor costs** on OpenRouter dashboard
4. **Set spending limits** in OpenRouter settings
5. **Cache vector store** (already done) to save on embedding costs

## 📝 Model Selection Guide

**Choose Claude 3.5 Sonnet if:**
- You want the best quality answers
- Cost is not a primary concern
- You need complex reasoning

**Choose GPT-4o Mini if:**
- You want good quality at reasonable cost
- You're familiar with OpenAI models
- You want fast responses

**Choose Llama 3.1 70B if:**
- You want open-source models
- You want good quality at lower cost
- You prefer Meta's models

**Choose Llama 3.1 8B if:**
- You want very cheap operation
- Speed is important
- Answers don't need to be perfect

## 🔄 Switching Between OpenRouter and OpenAI

To switch back to direct OpenAI:

1. Get an OpenAI API key from: https://platform.openai.com/api-keys

2. Edit `.env`:
```bash
OPENAI_API_KEY=sk-proj-your-openai-key-here
# OPENAI_API_BASE=https://openrouter.ai/api/v1  # Comment this out
```

3. The code will automatically use direct OpenAI when no base URL is set

## 📚 Additional Resources

- OpenRouter Dashboard: https://openrouter.ai/
- Model Pricing: https://openrouter.ai/models
- API Documentation: https://openrouter.ai/docs
- Discord Community: https://discord.gg/openrouter

---

**You're all set! Start chatting with your Hummingbot AI assistant! 🚀**

