import streamlit as st
import google.generativeai as genai
import os

# Pega a chave que você colocou na Vercel
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

st.title("🤖 IA do Pequeno Engenheiro")

prompt = st.text_input("Em que posso te ajudar hoje?")

if prompt:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    st.write(response.text)
