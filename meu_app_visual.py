import streamlit as st
import google.generativeai as genai

# Configuração
genai.configure(api_key="AIzaSyAAmvLafTLVTZYES5Rd926mPRlXD3Khc2U")

# FUNÇÃO PARA NÃO DAR MAIS 404
@st.cache_resource
def conectar():
    # Isso lista todos os modelos que funcionam na sua conta agora
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            # Retorna o primeiro que encontrar (geralmente o Flash ou Pro)
            return genai.GenerativeModel(m.name)
    return None

model = conectar()

st.set_page_config(page_title="Minha IA", page_icon="🤖")
st.title("🤖 Minha IA")

if model is None:
    st.error("Não foi possível encontrar um motor funcionando. Verifique sua conexão.")
else:
    if "chat" not in st.session_state:
        st.session_state.chat = []

    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if p := st.chat_input("Diga algo..."):
        st.session_state.chat.append({"role": "user", "content": p})
        with st.chat_message("user"): st.markdown(p)
        with st.chat_message("assistant"):
            try:
                r = model.generate_content(p)
                st.markdown(r.text)
                st.session_state.chat.append({"role": "assistant", "content": r.text})
            except Exception as e:
                st.error(f"Erro: {e}")
