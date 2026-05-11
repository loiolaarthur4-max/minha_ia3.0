import streamlit as st
import google.generativeai as genai
import os

# Configuração da IA
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Esse é o segredo: Criar uma função principal
def main():
    st.title("🤖 Minha IA Inventor")
    
    pergunta = st.text_input("O que vamos inventar hoje?")
    
    if pergunta:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(pergunta)
        st.write(response.text)

# A Vercel precisa disso para saber por onde começar
if __name__ == "__main__":
    main()
