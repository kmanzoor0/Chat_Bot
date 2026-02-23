# Chat_Bot
A conversational AI chatbot built using LangChain and Groq LLM with manual chat history memory using ChatPromptTemplate and LCEL chaining.


# 🤖 LangChain Chatbot with Conversation History

This project is a simple conversational AI chatbot built using **LangChain** and **Groq LLM (LLaMA 3.1 8B Instant)**.

The chatbot maintains conversation history manually using `ChatPromptTemplate` and `MessagesPlaceholder`, allowing it to remember previous user interactions.

---

## 🚀 Features

- Uses Groq LLaMA 3.1 model
- Implements LCEL chaining (`|` operator)
- Maintains chat history manually
- Uses `ChatPromptTemplate`
- Uses `MessagesPlaceholder`
- Interactive CLI chatbot
- Temperature control for natural responses

---

## 🛠️ Tech Stack

- Python
- LangChain Core
- Groq LLM
- dotenv
- LCEL (LangChain Expression Language)

---

## 📂 How It Works

1. Stores conversation in a Python list.
2. Injects history into the prompt using `MessagesPlaceholder`.
3. Sends structured conversation to LLM.
4. Appends new messages back into history.
5. Repeats in a loop until user types `exit`.

---

## ▶️ Installation
```bash
pip install langchain langchain-groq python-dotenv

##Create a .env file:

GROQ_API_KEY=your_api_key_here

##Run:

python chatbot.py


```bash
pip install langchain langchain-groq python-dotenv
