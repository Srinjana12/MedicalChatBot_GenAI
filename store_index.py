from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore


load_dotenv()
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)
embeddings= download_hugging_face_embeddings()


# Load your .env
load_dotenv()

# Initialize Pinecone client
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
)

# Now you can create the index using `pc`
index_name = "medicalbot"

if index_name not in pc.list_indexes():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=os.getenv("PINECONE_ENVIRONMENT") 
        )
    )

    # Embed each chunks and upsert the embeddings into the Pinecone index
docsearch=PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
    
    
)