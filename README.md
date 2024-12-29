## Ollama Chatbot with ChromaDB Memory

This project demonstrates how to build a chatbot using Ollama's LLM (Language Model) and ChromaDB for maintaining contextual memory. The chatbot remembers previous interactions and leverages past conversation data to provide relevant and accurate responses. The app is built using Streamlit for the frontend interface.

## Features

- **Memory**: Uses ChromaDB to store conversation history and context for the chatbot, allowing it to generate responses based on past interactions.
- **Ollama Model**: The app integrates with Ollama's language model to generate responses.
- **Model Selection**: You can choose between different Ollama models from the sidebar.
- **Chat History**: The chatbot remembers previous exchanges, allowing for more meaningful conversations.
- **Clear Chat History**: Clears both the session's chat history and ChromaDB's stored data.

## Requirements

- Python 3.7 or higher
- Streamlit
- Langchain (Ollama integration)
- ChromaDB
- OpenAI API Key (for embeddings in ChromaDB)


