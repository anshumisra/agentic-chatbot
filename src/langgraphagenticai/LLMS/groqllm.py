import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input

    def get_llm_models(self):
        try:
            groq_api_key=self.user_controls_input.get('GROQ_API_KEY')
            selected_groq_model=self.user_controls_input.get('groq_model_selection')

            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
                st.error("Error: GROQ API Key is missing. Please provide a valid API Key.")
                
            llm=ChatGroq(api_key=groq_api_key,model_name=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")
        return llm