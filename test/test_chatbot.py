import pytest
from src.chatbot import generate_response, retrieve_from_chromadb, save_to_chromadb
from unittest.mock import Mock

def test_generate_response():
    mock_llm = Mock(return_value="Hello, how can I help you?")
    response = generate_response("llama3.2:1b", "Hello!")
    assert response == "Hello, how can I help you?"

def test_retrieve_from_chromadb():
    # Assuming `retrieve_from_chromadb` returns mock data
    mock_collection = Mock()
    mock_collection.query.return_value = {'documents': ['Hello, how can I help you?']}
    context = retrieve_from_chromadb(mock_collection, "Hello!")
    assert context == "Hello, how can I help you?"

def test_save_to_chromadb():
    # Mocking ChromaDB collection's `add` method
    mock_collection = Mock()
    save_to_chromadb(mock_collection, "Hello!", "Hello, how can I help you?")
    mock_collection.add.assert_called_with(
        documents=["Hello!", "Hello, how can I help you?"],
        metadatas=[{"role": "user"}, {"role": "bot"}],
        ids=["user-0", "bot-0"]
    )
