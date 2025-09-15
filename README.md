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

- **Python 3.10**
- **Git**

### Step-by-Step Guide

1. **Clone the Repository, Create a Virtual Environment, Install Dependencies, and Set Up API Keys**:

   - Clone the repository:

     ```bash
     git clone https://github.com/ILIASB1212/RAG-CHAT-WITH-MOROCCO-LOIS-DE-FINANCE-2020-2025.git
     ```

   - Create a virtual environment:

     ```bash
     conda create -p env python==3.10 -y
     ```

   - Install the required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Create a `.env` file in the project root directory and add your API keys:

     ```bash
     OPENAI_API_KEY="your_openai_api_key_here"
     GROQ_API_KEY="your_groq_api_key_here"
     LANGCHAIN_API_KEY="your_langchain_api_key_here"
     ```

   - Add your documents: Place all the public finance PDF files from **2020 to 2025** into a new directory named `data` in the project root.

2. **Running the Application**:

   Once everything is set up, run the Streamlit application from your terminal:

   ```bash
   streamlit run app.py
This will open the application in your web browser, where you can start asking questions.
