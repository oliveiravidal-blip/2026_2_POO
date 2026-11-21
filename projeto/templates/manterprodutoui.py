import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProdutoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado.")
        else:
            list_dic = []
            for obj in produtos:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        categorias = Service.categoria_listar()
        if len(categorias) == 0:
            st.warning("Cadastre ao menos uma categoria antes de inserir produtos.")
        else:
            descricao = st.text_input("Informe a descrição do produto")
            preco = st.number_input("Informe o preço (R$)", min_value=0.01, step=0.50, format="%.2f")
            estoque = st.number_input("Informe a quantidade em estoque", min_value=0, step=1)
            op_categoria = st.selectbox("Selecione a categoria", categorias)

            if st.button("Inserir"):
                id_categoria = op_categoria.get_id()
                Service.produto_inserir(descricao, preco, estoque, id_categoria)
                st.success("Produto inserido com sucesso!")
                time.sleep(2)
                st.rerun()

    def atualizar():
        produtos = Service.produto_listar()
        categorias = Service.categoria_listar()
        
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado.")
        elif len(categorias) == 0:
            st.warning("Nenhuma categoria disponível para vínculo.")
        else:
            op_produto = st.selectbox("Selecione o produto a atualizar", produtos)
            
            descricao = st.text_input("Nova descrição", op_produto.get_descricao())
            preco = st.number_input("Novo preço (R$)", value=float(op_produto.get_preco()), min_value=0.01, step=0.50, format="%.2f")
            estoque = st.number_input("Novo estoque", value=int(op_produto.get_estoque()), min_value=0, step=1)
            
            idx_cat = 0
            for i, cat in enumerate(categorias):
                if cat.get_id() == op_produto.get_id_categoria():
                    idx_cat = i
                    break
                    
            op_categoria = st.selectbox("Nova categoria", categorias, index=idx_cat)

            if st.button("Atualizar"):
                id = op_produto.get_id()
                id_categoria = op_categoria.get_id()
                Service.produto_atualizar(id, descricao, preco, estoque, id_categoria)
                st.success("Produto atualizado com sucesso!")
                time.sleep(2)
                st.rerun()

    def excluir():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado.")
        else:
            op = st.selectbox("Selecione o produto para exclusão", produtos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.produto_excluir(id)
                st.success("Produto excluído com sucesso!")
                time.sleep(2)
                st.rerun()