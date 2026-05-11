import streamlit as st
import google.generativeai as genai
import os

# Configura a chave
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

st.title("🤖 IA do Pequeno Engenheiro")

pergunta = st.text_input("O que vamos inventar?")

if pergunta:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(pergunta)
    st.write(response.text)
