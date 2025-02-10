import os
from dotenv import load_dotenv
import streamlit as st
from langsmith import Client
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")  
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "Chatbot-Session"  


client = Client()


st.title("CHATBOT USING MISTRAL AND LANGCHAIN")
user_input = st.text_input("Type your queries here")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI bot. Please respond to the user queries."),
    ("user", "Question: {question}")
])


llm = Ollama(model="mistral")
outparser = StrOutputParser()
chain = prompt | llm | outparser


if user_input:
    try:
        response = chain.invoke({"question": user_input})  
        st.write(response)  
    except Exception as e:
        st.error(f"Error: {str(e)}")
