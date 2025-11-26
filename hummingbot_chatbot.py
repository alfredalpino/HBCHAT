"""
Hummingbot AI Chat Wrapper
A RAG-based chatbot for Hummingbot documentation
"""

import os
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class HummingbotChatbot:
    def __init__(self, docs_path="/Users/ubaid/HBCHAT/MD-Only", use_openai=True):
        """
        Initialize the Hummingbot Chatbot
        
        Args:
            docs_path: Path to the markdown documentation folder
            use_openai: If True, uses OpenAI embeddings. If False, uses local embeddings
        """
        self.docs_path = docs_path
        self.use_openai = use_openai
        self.vectorstore = None
        self.qa_chain = None
        
        # Initialize the chatbot
        self._load_documents()
        self._create_vectorstore()
        self._setup_qa_chain()
    
    def _load_documents(self):
        """Load all markdown documentation files"""
        print("📚 Loading Hummingbot documentation...")
        
        loader = DirectoryLoader(
            self.docs_path,
            glob="**/*.md",
            loader_cls=UnstructuredMarkdownLoader,
            show_progress=True,
        )
        
        documents = loader.load()
        print(f"✅ Loaded {len(documents)} documentation files")
        
        # Split documents into chunks
        print("✂️  Splitting documents into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        self.texts = text_splitter.split_documents(documents)
        print(f"✅ Created {len(self.texts)} text chunks")
    
    def _create_vectorstore(self):
        """Create vector store from documents"""
        print("🔍 Creating vector embeddings...")
        
        if self.use_openai:
            # Check for OpenAI API key
            if not os.getenv("OPENAI_API_KEY"):
                raise ValueError(
                    "❌ OPENAI_API_KEY not found in environment variables. "
                    "Please create a .env file with your OpenAI API key or set use_openai=False"
                )
            # Configure for OpenRouter if base URL is set
            api_base = os.getenv("OPENAI_API_BASE")
            if api_base:
                embeddings = OpenAIEmbeddings(
                    openai_api_base=api_base,
                    model="openai/text-embedding-3-small"
                )
            else:
                embeddings = OpenAIEmbeddings()
        else:
            # Use local embeddings (free, but slower)
            from langchain_community.embeddings import HuggingFaceEmbeddings
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
        
        # Create FAISS vector store
        self.vectorstore = FAISS.from_documents(self.texts, embeddings)
        print("✅ Vector store created successfully!")
        
        # Save vectorstore for future use
        self.vectorstore.save_local("hummingbot_vectorstore")
        print("💾 Vector store saved to 'hummingbot_vectorstore'")
    
    def _setup_qa_chain(self):
        """Set up the conversational QA chain"""
        print("🤖 Setting up QA chain...")
        
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError(
                "❌ OPENAI_API_KEY not found. Please set it in your .env file"
            )
        
        # Initialize the LLM with OpenRouter support
        api_base = os.getenv("OPENAI_API_BASE")
        if api_base:
            # Using OpenRouter - you can choose from many models!
            # Set headers via environment or default_headers
            import os
            os.environ.setdefault("HTTP_REFERER", "https://hummingbot.io")
            os.environ.setdefault("X_TITLE", "Hummingbot AI Chat")
            
            llm = ChatOpenAI(
                model="anthropic/claude-3.5-sonnet",  # or "openai/gpt-4o-mini", "meta-llama/llama-3.1-70b-instruct"
                temperature=0.7,
                base_url=api_base,
                default_headers={
                    "HTTP-Referer": "https://hummingbot.io",
                    "X-Title": "Hummingbot AI Chat"
                }
            )
        else:
            # Direct OpenAI
            llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0.7,
            )
        
        # Create memory for conversation history
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        # Create the conversational retrieval chain
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5}),
            memory=memory,
            return_source_documents=True,
            verbose=False
        )
        
        print("✅ Chatbot ready!\n")
    
    def chat(self, question):
        """
        Ask a question to the chatbot
        
        Args:
            question: User's question about Hummingbot
            
        Returns:
            dict with 'answer' and 'source_documents'
        """
        if not self.qa_chain:
            raise ValueError("QA chain not initialized. Please run setup first.")
        
        result = self.qa_chain.invoke({"question": question})
        return result
    
    def interactive_chat(self):
        """Start an interactive chat session"""
        print("=" * 60)
        print("🤖 HUMMINGBOT AI CHAT ASSISTANT")
        print("=" * 60)
        print("Ask me anything about Hummingbot!")
        print("Type 'quit', 'exit', or 'bye' to end the conversation.")
        print("Type 'sources' after any answer to see source documents.")
        print("=" * 60 + "\n")
        
        last_sources = []
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n👋 Thanks for using Hummingbot AI Chat! Happy trading!\n")
                    break
                
                if user_input.lower() == 'sources' and last_sources:
                    print("\n📚 Source Documents:")
                    for i, doc in enumerate(last_sources, 1):
                        source = doc.metadata.get('source', 'Unknown')
                        print(f"  {i}. {source}")
                    print()
                    continue
                
                # Get response from chatbot
                result = self.chat(user_input)
                answer = result['answer']
                last_sources = result.get('source_documents', [])
                
                print(f"\n🤖 Assistant: {answer}\n")
                
                if last_sources:
                    print(f"📄 (Based on {len(last_sources)} documentation sources - type 'sources' to view)\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Chat interrupted. Goodbye!\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")


def load_existing_vectorstore(vectorstore_path="hummingbot_vectorstore"):
    """
    Load an existing vector store (faster startup if already created)
    """
    print("📂 Loading existing vector store...")
    
    if not os.path.exists(vectorstore_path):
        raise ValueError(f"Vector store not found at {vectorstore_path}")
    
    if os.getenv("OPENAI_API_KEY"):
        api_base = os.getenv("OPENAI_API_BASE")
        if api_base:
            embeddings = OpenAIEmbeddings(
                openai_api_base=api_base,
                model="openai/text-embedding-3-small"
            )
        else:
            embeddings = OpenAIEmbeddings()
    else:
        from langchain_community.embeddings import HuggingFaceEmbeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    
    vectorstore = FAISS.load_local(vectorstore_path, embeddings, allow_dangerous_deserialization=True)
    print("✅ Vector store loaded!")
    return vectorstore


if __name__ == "__main__":
    # Initialize and start the chatbot
    print("\n🚀 Initializing Hummingbot AI Chatbot...\n")
    
    try:
        chatbot = HummingbotChatbot()
        chatbot.interactive_chat()
    except Exception as e:
        print(f"\n❌ Failed to initialize chatbot: {e}")
        print("\nMake sure you:")
        print("1. Created a .env file with your OPENAI_API_KEY")
        print("2. Installed all requirements: pip install -r requirements.txt")
        print("3. Have the MD-Only folder with markdown files\n")

