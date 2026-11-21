import streamlit as st
import time
from service import Service

class ReajustarProdutoUI:
    def main():
        st.header("Reajuste de Preço dos Produtos")
        ReajustarProdutoUI.reajustar()

    def reajustar():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado para reajuste.")
        else:
            st.write("Aplica um reajuste percentual no preço de **todos** os produtos cadastrados no sistema.")
            percentual = st.number_input("Informe o percentual de reajuste (%)", value=0.0, step=1.0)
            
            if st.button("Reajustar"):
                Service.produto_reajustar(percentual)
                st.success(f"Preços reajustados em {percentual}% com sucesso!")
                time.sleep(2)
                st.rerun()