from templates.manterclienteui import ManterClienteUI
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterprodutoui import ManterProdutoUI
from templates.reajustarprodutoui import ReajustarProdutoUI
import streamlit as st

class IndexUI:

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Categorias", "Produtos", "Reajuste"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Categorias": ManterCategoriaUI.main()
        if op == "Produtos": ManterProdutoUI.main()
        if op == "Reajuste": ReajustarProdutoUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()