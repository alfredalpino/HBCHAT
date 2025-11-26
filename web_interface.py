"""
Web Interface for Hummingbot AI Chatbot using Gradio
"""

import gradio as gr
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class HummingbotWebChat:
    def __init__(self):
        self.vectorstore = None
        self.qa_chain = None
        self.memory = None
        self._initialize()
    
    def _initialize(self):
        """Initialize the chatbot components"""
        print("🚀 Initializing Hummingbot AI Chatbot...")
        
        # Check for API key
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        # Load vector store
        print("📂 Loading vector store...")
        api_base = os.getenv("OPENAI_API_BASE")
        if api_base:
            embeddings = OpenAIEmbeddings(
                openai_api_base=api_base,
                model="openai/text-embedding-3-small"
            )
        else:
            embeddings = OpenAIEmbeddings()
        
        if os.path.exists("hummingbot_vectorstore"):
            self.vectorstore = FAISS.load_local("hummingbot_vectorstore", embeddings, allow_dangerous_deserialization=True)
            print("✅ Vector store loaded!")
        else:
            raise ValueError(
                "Vector store not found. Please run hummingbot_chatbot.py first to create it."
            )
        
        # Initialize LLM with OpenRouter support
        if api_base:
            llm = ChatOpenAI(
                model_name="anthropic/claude-3.5-sonnet",  # or "openai/gpt-4o-mini"
                temperature=0.7,
                openai_api_base=api_base,
                model_kwargs={
                    "headers": {
                        "HTTP-Referer": "https://hummingbot.io",
                        "X-Title": "Hummingbot AI Chat"
                    }
                }
            )
        else:
            llm = ChatOpenAI(
                model_name="gpt-4o-mini",
                temperature=0.7,
            )
        
        # Create memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        # Create QA chain
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5}),
            memory=self.memory,
            return_source_documents=True,
            verbose=False
        )
        
        print("✅ Chatbot ready!\n")
    
    def chat(self, message, history):
        """
        Process chat message and return response
        
        Args:
            message: User's message
            history: Chat history from Gradio
            
        Returns:
            Response string
        """
        try:
            result = self.qa_chain({"question": message})
            answer = result['answer']
            sources = result.get('source_documents', [])
            
            # Add source information
            if sources:
                source_files = list(set([
                    doc.metadata.get('source', 'Unknown').replace('/Users/ubaid/HBCHAT/MD-Only/', '')
                    for doc in sources
                ]))
                answer += f"\n\n📚 **Sources**: {', '.join(source_files[:3])}"
                if len(source_files) > 3:
                    answer += f" and {len(source_files) - 3} more..."
            
            return answer
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def reset_conversation(self):
        """Reset the conversation memory"""
        self.memory.clear()
        return None


def create_interface():
    """Create and configure the Gradio interface"""
    
    # Initialize chatbot
    chatbot = HummingbotWebChat()
    
    # Create custom CSS
    custom_css = """
    .gradio-container {
        font-family: 'Arial', sans-serif;
    }
    .chat-message {
        padding: 10px;
        border-radius: 10px;
    }
    """
    
    # Create Gradio interface
    with gr.Blocks(
        title="Hummingbot AI Assistant",
        theme=gr.themes.Soft(),
        css=custom_css
    ) as interface:
        
        gr.Markdown(
            """
            # 🤖 Hummingbot AI Chat Assistant
            
            Ask me anything about Hummingbot - strategies, configurations, exchanges, installation, and more!
            
            **Examples:**
            - "How do I install Hummingbot on Docker?"
            - "What is the pure market making strategy?"
            - "How do I connect to Binance?"
            - "Explain the Avellaneda-Stoikov strategy"
            """
        )
        
        chatbot_ui = gr.Chatbot(
            label="Chat with Hummingbot AI",
            height=500,
            show_label=True,
            avatar_images=(None, "🤖")
        )
        
        with gr.Row():
            msg = gr.Textbox(
                label="Your Question",
                placeholder="Type your question here...",
                show_label=False,
                scale=9
            )
            submit = gr.Button("Send", scale=1, variant="primary")
        
        with gr.Row():
            clear = gr.Button("🗑️ Clear Chat")
            
        gr.Markdown(
            """
            ---
            ### 💡 Tips:
            - Be specific with your questions for better answers
            - The AI uses the official Hummingbot documentation
            - Source documents are shown at the bottom of each response
            
            ### 📚 Documentation Categories:
            Strategies • Exchanges • Installation • Configuration • Dashboard • API • Gateway • V2 Strategies
            """
        )
        
        # Event handlers
        msg.submit(chatbot.chat, [msg, chatbot_ui], [chatbot_ui])
        msg.submit(lambda: "", None, [msg])
        
        submit.click(chatbot.chat, [msg, chatbot_ui], [chatbot_ui])
        submit.click(lambda: "", None, [msg])
        
        clear.click(lambda: None, None, [chatbot_ui])
        clear.click(chatbot.reset_conversation, None, None)
    
    return interface


if __name__ == "__main__":
    try:
        interface = create_interface()
        interface.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False,  # Set to True to create a public link
            show_error=True
        )
    except Exception as e:
        print(f"\n❌ Failed to start web interface: {e}")
        print("\nMake sure you:")
        print("1. Run hummingbot_chatbot.py first to create the vector store")
        print("2. Have OPENAI_API_KEY in your .env file")
        print("3. Installed all requirements: pip install -r requirements.txt\n")

