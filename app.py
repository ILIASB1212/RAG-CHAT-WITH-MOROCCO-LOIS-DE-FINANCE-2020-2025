from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
import streamlit as st
from logger.log import logging
from exeption.exeption_hundle import AppException
import sys
import os
import time

# LOAD THE API KEYS 
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LOIS DE FINANCE RAG"

#setup document loader and vector store

def embeding_vectorstore():
    if "vectors" not in st.session_state:
        try:
            st.session_state.documents=PyPDFDirectoryLoader("./data").load()

            st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,  
            chunk_overlap=100,
            length_function=len,
            add_start_index=True,
        )
            st.session_state.splited_document=st.session_state.text_splitter.split_documents(st.session_state.documents)
            st.session_state.embeddings=OpenAIEmbeddings()
            st.session_state.vectors=Chroma.from_documents(st.session_state.splited_document,st.session_state.embeddings,persist_directory="db")
            logging.info(f"the vectorestore created suscsesfuly")
        except Exception as e:
            logging.info(f"error in embeding_vectore function {e}")
            raise AppException(e, sys) from e

# load the document with adding text input first
user_propt=st.text_input("write your question query")
if st.button("load the documents"):
    start=time.process_time()
    try:
        time.sleep(1)
        st.write('loading documents may take time')
        embeding_vectorstore()
        end=time.process_time()
        st.write(f'document loaded sussesfully in {end - start} s')
        logging.info(f"document loaded sussesfully in {end - start} s")
    except Exception as e:
            logging.info(f"error in loading document {e}")
            raise AppException(e, sys) from e


# PROMPTE TEMPLATE

system_prompt = (
        "You are an expert assisstant for question-answering tasks of public finance. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, just say that you don't know. "
        "if the user ask you question you need to get the information from thcontext then add your knowledge "
        "\n\n"
        "<context>"
        "{context}"
         "<context>"
    )

prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

# create llm with groq

llm=ChatGroq(model="openai/gpt-oss-20b")


if user_propt:
    try:
        stuff_chain=create_stuff_documents_chain(llm,prompt)
        retriver=st.session_state.vectors.as_retriever()
        chain=create_retrieval_chain(retriver,stuff_chain)
        start=time.process_time()
        responce=chain.invoke({"input":user_propt})
        end=time.process_time()
        st.write(f"the prosses time is : {end-start} S")
        st.write(responce["answer"])
        logging.info(f"the user get answers succsesfuly")
        # st expender to add the resourse
        with st.expander("ressourse documents"):
            for i,doc in enumerate(responce['context']):
                st.write(doc.page_content)
                st.write('------------------------')

    except Exception as e:
            logging.info(f"error in prompt answering {e}")
            raise AppException(e, sys) from e











###############################################################

