# Chatbot using OLLAMA, Mistral, and LangChain

## Overview
This project is a chatbot built using **Ollama**, **Mistral**, and **LangChain**. It leverages **Mistral**, a powerful LLM (Large Language Model), via **Ollama**, integrated with **LangChain** to handle prompt management and LLM interactions. The chatbot is deployed using **Streamlit** for an interactive user interface.

## Features
- Uses **Mistral** LLM via **Ollama**
- Integrated with **LangChain** for prompt management
- Simple and interactive UI built with **Streamlit**
- Accepts user queries and provides AI-generated responses

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/JisnaP/Chatbot-using-OLLAMA-MISTRAL-AND-LANGCHAIN.git
cd Chatbot-using-OLLAMA-MISTRAL-AND-LANGCHAIN
```

### 2. Create a Virtual Environment 
```sh
conda create -p ./venv python=3.10 -y
conda activate ./venv   # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Install and Run Ollama
- Download and install **Ollama** from [Ollama's official website](https://ollama.ai/)
- Pull the **Mistral** model:
  ```sh
  ollama pull mistral
  ```
- Verify that Ollama is running:
  ```sh
  ollama run mistral
  ```

## Running the Chatbot
To start the chatbot, run:
```sh
streamlit run app.py
```
This will launch the chatbot UI in your web browser.

## Usage
1. Enter a query in the input box.
2. The chatbot will process the query using **LangChain** and **Mistral** via **Ollama**.
3. The response will be displayed in the Streamlit interface.

## Example Interaction
**User Input:**
> "What is LangChain?"

**Chatbot Response:**
> "LangChain is a framework for building applications powered by LLMs. It provides tools for managing prompts, memory, and chains of interactions with large language models."

## File Structure
```
Chatbot-using-OLLAMA-MISTRAL-AND-LANGCHAIN/
│── app.py                 # Main application script
│── requirements.txt       # List of dependencies
│── README.md              # Project documentation
│── venv/                  # Virtual environment (optional)
└── ...
```


## Author
**Jisna Patharakkal**

