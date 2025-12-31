# LangGraph Stateful Chatbot

A basic stateful chatbot using **LangGraph**, **LangChain**, **Streamlit**, and **Groq LLMs**.

---

## How It Works

- **State**: Conversation stored in `messages` via `add_messages` reducer.  
- **Chatbot Node**: Receives messages and returns model responses.  
- **Graph Flow**: `START → chatbot → END`  
- **UI**: Streamlit captures input and streams responses.

---

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py

<img width="1837" height="730" alt="image" src="https://github.com/user-attachments/assets/a82d52a7-9e09-4958-b48f-6507c227a82a" />
