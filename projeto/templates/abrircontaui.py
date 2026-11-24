import streamlit as st
from service import Service
import time

class AbrirContaUI:
    def main():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha")
        if st.button("Inserir"):
            Service.cliente_inserir(nome, email, fone)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()