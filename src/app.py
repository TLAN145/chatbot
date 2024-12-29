import streamlit as st
from src.chatbot import initialize_chromadb, save_to_chromadb, retrieve_from_chromadb, generate_response

# Initialize global variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def main():
    st.title("Ollama Chatbot with ChromaDB Memory")
    
    # Initialize ChromaDB
    collection = initialize_chromadb()
    if isinstance(collection, str):  # Check if initialization failed
        st.error(collection)
        return

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
        context = retrieve_from_chromadb(collection, user_input)
        prompt = f"Context: {context}\nUser: {user_input}" if context else user_input

        # Generate and append response
        response = generate_response(model_choice, prompt)
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")

        # Save to ChromaDB
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
