import chromadb
from chromadb.utils import embedding_functions
from langchain.llms import Ollama

# Initialize ChromaDB Client and Collection
def initialize_chromadb():
    try:
        client = chromadb.Client()
        ef = embedding_functions.OpenAIEmbeddingFunction(api_key="your-openai-api-key")  # Replace with your OpenAI API key
        collection = client.get_or_create_collection(name="chatbot_memory", embedding_function=ef)
        return collection
    except Exception as e:
        return f"Error initializing ChromaDB: {e}"

# Save conversation history to ChromaDB
def save_to_chromadb(collection, user_input, response):
    try:
        collection.add(
            documents=[user_input, response],
            metadatas=[{"role": "user"}, {"role": "bot"}],
            ids=[f"user-{len(st.session_state.chat_history)}", f"bot-{len(st.session_state.chat_history)}"]
        )
    except Exception as e:
        return f"Error saving to ChromaDB: {e}"

# Retrieve past context from ChromaDB
def retrieve_from_chromadb(collection, query):
    try:
        results = collection.query(query_texts=[query], n_results=1)
        if results and results.get('documents'):
            return results['documents'][0]  # Return the most relevant document
        return None
    except Exception as e:
        return f"Error retrieving context from ChromaDB: {e}"

# Generate response using the Ollama language model
def generate_response(model_name, prompt):
    try:
        llm = Ollama(model=model_name)
        response = llm(prompt)
        return response
    except Exception as e:
        return f"Error: {e}"
