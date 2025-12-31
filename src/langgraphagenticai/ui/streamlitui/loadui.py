import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="👩🏻‍💻 " + self.config.get_page_title(),layout="wide")
        st.header("👩🏻‍💻 " + self.config.get_page_title())
    
        with st.sidebar:
            st.subheader("🛠️ User Controls")
            llm_options=self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()
            groq_model_options=self.config.get_groq_model_options()

            self.user_controls['llm_selection']=st.selectbox("Select Model",llm_options)
            

            if self.user_controls['llm_selection']=='Groq':
                self.user_controls['groq_model_selection']=st.selectbox("Select Groq Model",groq_model_options)
                self.user_controls['GROQ_API_KEY']=st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")

                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your GROQ API Key to proceed.")

            self.user_controls['usecase_selection']=st.selectbox("Select Use Case",usecase_options)
        return self.user_controls