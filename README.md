# Moroccan Public Finance Laws Chatbot (2020-2025)

## Project Overview

This is a **Retrieval-Augmented Generation (RAG)** chatbot designed to provide fast and accurate answers to questions about Moroccan public finance laws passed between **2020 and 2025**. It uses a powerful combination of open-source and proprietary tools to process and understand legal documents, allowing users to ask complex questions in natural language.

## Key Features

- **Intelligent Q&A**: Get precise answers to your questions based on specific laws and documents.
- **Intuitive UI**: An easy-to-use interface built with Streamlit for a seamless user experience.
- **Rapid Response**: Leveraging the speed of the Groq API for near-instantaneous answer generation (note: it may take 2 minutes to download the data initially).
- **Comprehensive Knowledge Base**: The chatbot is grounded in official public finance documents, ensuring factual and reliable information.

## Technologies Used

This project is built using a modern **RAG** stack to create a robust and efficient chatbot. The key tools include:

- **Streamlit**: Used for creating the interactive and user-friendly web interface.
- **LangChain**: The core framework that orchestrates the entire RAG pipeline, from document loading to model invocation.
- **Chroma**: A powerful open-source vector database that stores the embedded document chunks for efficient retrieval.
- **OpenAI Embeddings**: Utilized to convert the text documents into high-dimensional numerical vectors, allowing the system to understand the semantic meaning of the text.
- **Groq**: A fast and scalable language model (LLM) that powers the final answer generation, ensuring quick and accurate responses.

## Setup and Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10
- Git

### Step-by-Step Guide

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ILIASB1212/RAG-CHAT-WITH-MOROCCO-LOIS-DE-FINANCE-2020-2025.git
