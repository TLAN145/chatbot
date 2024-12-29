import streamlit as st
from langchain.llms import Ollama  # Ensure this works in your environment
import chromadb
from chromadb.utils import embedding_functions

# Initialize global variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize ChromaDB Client and Collection
def initialize_chromadb():
    try:
        client = chromadb.Client()
        ef = embedding_functions.OpenAIEmbeddingFunction(api_key="your-openai-api-key")  # Replace with your OpenAI API key
        collection = client.get_or_create_collection(name="chatbot_memory", embedding_function=ef)
        return collection
    except Exception as e:
        st.error(f"Error initializing ChromaDB: {e}")
        return None

# Save conversation history to ChromaDB
def save_to_chromadb(collection, user_input, response):
    try:
        collection.add(
            documents=[user_input, response],
            metadatas=[{"role": "user"}, {"role": "bot"}],
            ids=[f"user-{len(st.session_state.chat_history)}", f"bot-{len(st.session_state.chat_history)}"]
        )
    except Exception as e:
        st.error(f"Error saving to ChromaDB: {e}")

# Retrieve past context from ChromaDB
def retrieve_from_chromadb(collection, query):
    try:
        results = collection.query(query_texts=[query], n_results=1)
        if results and results.get('documents'):
            return results['documents'][0]  # Return the most relevant document
        return None
    except Exception as e:
        st.error(f"Error retrieving context from ChromaDB: {e}")
        return None

# Function to generate a response
def generate_response(model_name, prompt):
    try:
        llm = Ollama(model=model_name)
        response = llm(prompt)
        return response
    except Exception as e:
        return f"Error: {e}"

# Main function for Streamlit app
def main():
    st.title("Ollama Chatbot with ChromaDB Memory")
    
    # Initialize ChromaDB
    collection = initialize_chromadb()
    if collection is None:
        st.warning("ChromaDB could not be initialized. Contextual memory is disabled.")

    # Sidebar for model selection
    st.sidebar.header("Settings")
    model_choice = st.sidebar.selectbox(
        "Choose a model:",
        ("llama3.2:1b", "llama3.1:8b")
    )
    
    # Clear chat history button
    if st.sidebar.button("Clear Chat History"):
        st.session_state.chat_history = []
        if collection:
            try:
                collection.delete(where={})  # Clear ChromaDB collection
            except Exception as e:
                st.error(f"Error clearing ChromaDB: {e}")

    # Input box for user prompt
    user_input = st.text_input("Enter your message:", key="user_input")

    if user_input:
        # Retrieve context from ChromaDB
        context = retrieve_from_chromadb(collection, user_input) if collection else None
        if context:
            prompt = f"Context: {context}\nUser: {user_input}"
        else:
            prompt = user_input

        # Generate and append response
        response = generate_response(model_choice, prompt)
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")

        # Save to ChromaDB
        if collection:
            save_to_chromadb(collection, user_input, response)
    
    # Display chat history
    st.write("### Chat History")
    if st.session_state.chat_history:
        st.text_area(
            "Conversation:",
            value="\n".join(st.session_state.chat_history),
            height=300,
            key="chat_history_display"
        )

# Run the app
if __name__ == "__main__":
    main()
