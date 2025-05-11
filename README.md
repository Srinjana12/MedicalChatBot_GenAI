# MedicalChatBot_GenAI

An intelligent, interactive chatbot designed to answer healthcare-related questions using retrieved context from medical documents. Built with Flask, LangChain, Pinecone, OpenAI, and Bootstrap, this project simulates a medical assistant that responds only based on indexed knowledge, ensuring reliable, context-specific answers.

# Features
1) Chatbot UI with modern Bootstrap 5 styling

2) Uses HuggingFace sentence embeddings for semantic search

3) Stores and retrieves vector data via Pinecone

4) Context-aware answers using LangChain + OpenAI

5) Real-time interaction via Flask backend

6) Secure API key handling via .env


![image alt](https://github.com/Srinjana12/MedicalChatBot_GenAI/blob/8caedfe814eb587d754724cc5a3dcea894fcf1d3/MedicalChatBotScreenshot.png)




# Tech Stack
# Component    	      Technology
 Backend	            Python, Flask
 Embeddings	          HuggingFace Transformers
 Vector DB	          Pinecone
 LLM	                OpenAI GPT-4 via LangChain
 UI	                Bootstrap 5, Font Awesome, HTML/CSS



# MedicalChatBot_GenAI/
│
├── app.py                    # Main Flask app
├── store_index.py           # Script to index documents into Pinecone
├── .env                     # API keys (excluded in .gitignore)
│
├── src/
│   ├── helper.py            # PDF loader, text splitter, embedding
│   └── prompt.py            # Custom system prompt for the chatbot
│
├── templates/
│   └── chat.html            # Bootstrap chat interface
│
├── static/
│   └── style.css            # Chat bubble and layout styles
│
└── Data/                    # PDF documents to be indexed



# How to Run

### Steps:

Clone the repository

```bash
Projects repo: https://github.com/Srinjana12/MedicalChatBot_GenAI
```

### Step 01: Create a Conda envirement after opening the repository

```bash
conda create -n  python=3.13 -y
```

```bash
conda activate llmmap
```

### Step 02- install the requirements
```bash
pip install -r requirements.txt
```
