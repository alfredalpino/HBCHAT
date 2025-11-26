from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader

docs_path = "/Users/ubaid/HBCHAT/MD-Only"  # Updated to MD-Only folder

loader = DirectoryLoader(
    docs_path,
    glob="**/*.md",
    loader_cls=UnstructuredMarkdownLoader,
)

documents = loader.load()
print(f"✅ Loaded {len(documents)} Hummingbot documentation files")
for i, doc in enumerate(documents[:3]):
    print(f"Sample {i+1}: {doc.metadata.get('source', 'Unknown')}")
