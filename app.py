import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def main():
    st.title("ERP Financeiro com Streamlit")
    
    menu = ["Clientes", "Contas a Pagar", "Contas a Receber", "Lançamentos", "Relatórios"]
    choice = st.sidebar.selectbox("Selecione uma opção", menu)
    conn = sqlite3.connect("erp_finance.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    
    if choice == "Clientes":
        st.subheader("Cadastro de Clientes")
        df = pd.read_sql_query("SELECT * FROM clientes", conn)
        st.dataframe(df)
        
    elif choice == "Contas a Pagar":
        st.subheader("Contas a Pagar")
        df = pd.read_sql_query("SELECT * FROM contas_pagar", conn)
        st.dataframe(df)
        
    elif choice == "Contas a Receber":
        st.subheader("Contas a Receber")
        df = pd.read_sql_query("SELECT * FROM contas_receber", conn)
        st.dataframe(df)
        
    elif choice == "Lançamentos":
        st.subheader("Lançamentos Financeiros")
        df = pd.read_sql_query("SELECT * FROM lancamentos", conn)
        st.dataframe(df)
        
    elif choice == "Relatórios":
        st.subheader("Relatório de Fluxo de Caixa")
        
        st.subheader("Top 5 Clientes com Maior Receita")
        df_top_clientes = pd.read_sql_query("""
            SELECT c.nome, SUM(l.valor) AS total_receita
            FROM lancamentos l
            JOIN clientes c ON l.tipo = 'Receita' AND l.descricao LIKE '%' || c.nome || '%'
            GROUP BY c.id
            ORDER BY total_receita DESC
            LIMIT 5
        """, conn)
        st.dataframe(df_top_clientes)
        
        st.bar_chart(df_top_clientes.set_index('nome')['total_receita'])

        st.subheader("Comparação Receita vs Despesa")
        df_comparacao = pd.read_sql_query("""
            SELECT tipo, SUM(valor) AS total 
            FROM lancamentos
            WHERE strftime('%Y-%m', data) = strftime('%Y-%m', 'now')
            GROUP BY tipo
        """, conn)
        df_comparacao_pivot = df_comparacao.set_index('tipo')['total']
        st.bar_chart(df_comparacao_pivot)

        st.subheader("Previsão de Fluxo de Caixa (Próximos 30 dias)")
        data_atual = datetime.now()
        data_futura = data_atual + timedelta(days=30)
        
        df_previsao_pagar = pd.read_sql_query("""
            SELECT * FROM contas_pagar 
            WHERE vencimento BETWEEN ? AND ?
        """, conn, params=(data_atual, data_futura))
        
        df_previsao_receber = pd.read_sql_query("""
            SELECT * FROM contas_receber 
            WHERE vencimento BETWEEN ? AND ?
        """, conn, params=(data_atual, data_futura))
        
        st.write("Contas a Pagar nos próximos 30 dias:")
        st.dataframe(df_previsao_pagar)
        
        st.write("Contas a Receber nos próximos 30 dias:")
        st.dataframe(df_previsao_receber)
        
    conn.close()

if __name__ == "__main__":
    main()
