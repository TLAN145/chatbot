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

## Examples
llama3.2:1b :
You: Can you help me with programming?
Bot: I'd be happy to help you with programming. What kind of programming are you working on, or what problem do you need help with? Are you a beginner looking for explanations and resources, or are you an experienced programmer trying to solve something specific? Let me know how I can assist you.

llama3.1:8b :
You: Can you help me with programming?
Bot: I'd be happy to help with your programming-related questions or problems. What type of programming are you working on (e.g., web development, mobile app development, machine learning, etc.) and what specific issue or task do you need assistance with?

Please provide more details such as:

* Programming language(s) involved
* Platform or framework being used (if applicable)
* A clear description of the problem or task you're trying to accomplish

This will help me better understand your needs and provide a more accurate and helpful response.


Clone the repository:
[https://github.com/your-repo/ollama-chatbot.git](https://github.com/TLAN145/chatbot.git)
