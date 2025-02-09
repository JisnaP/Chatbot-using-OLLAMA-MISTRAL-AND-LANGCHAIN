from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
LANGSMITH_TRACING= "true"

st.title("CHATBOT USING MISTRAL AND LANGCHAIN")
input=st.text_input("Type your queries here")
user_input=input
prompt=ChatPromptTemplate.from_messages(
    [
    ("system", "You are a helpful AI bot. Please respond to the user queries."),
    ("user", "Question:{question}")
    
    ]

)

llm=Ollama(model="mistral")
outparser=StrOutputParser()
chain=prompt|llm|outparser
if input:
    response=chain.invoke({"question":input})
    st.write(response)
