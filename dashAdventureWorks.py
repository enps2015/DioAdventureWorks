# Importando as bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# Criando o Data Frame
df = pd.read_excel("AdventureWorks.xlsx")

# Convertendo a coluna "Data Venda" para formato datetime
df["Data Venda"] = pd.to_datetime(df["Data Venda"])
df["Ano Venda"] = df["Data Venda"].dt.year
df["Mes Venda"] = df["Data Venda"].dt.month

# Criando o Dashboard Interativo
st.title("Análise de Vendas da Adventure Works 🚲")
st.write("Explore os dados de vendas, lucratividade e desempenho por produto, loja e cliente.")

# Barra Lateral: Filtros Interativos
st.sidebar.header("Filtros")
ano_selecionado = st.sidebar.selectbox("Selecione o Ano: ", df["Ano Venda"].unique())

produto_selecionado = st.sidebar.multiselect(
    "Selecione o(s) Produto(s): ", df["Produto"].unique(), default=df["Produto"].unique()
)

# Aplicando os Filtros
df_filtrado = df[(df["Ano Venda"] == ano_selecionado) & (df["Produto"].isin(produto_selecionado))]

# 1.Vendas e Lucratividade
st.header("1. Vendas e Lucratividade")

# Receita Total por Mês
receita_mensal = df_filtrado.groupby("Mes Venda")["Valor Venda"].sum()
fig_receita_mensal = px.line(receita_mensal, x=receita_mensal.index, y="Valor Venda", title="Receita Mensal",
                             labels={"Valor Venda": "Receita total", "Mes Venda": "Mês"})
st.plotly_chart(fig_receita_mensal)

# Lucro Total por mês
df_filtrado["Lucro"] = df_filtrado["Valor Venda"] - df_filtrado["Custo Unitário"] * df_filtrado["Quantidade"]
lucro_mensal = df_filtrado.groupby("Mes Venda")["Lucro"].sum()
fig_lucro_mensal = px.line(lucro_mensal, x=lucro_mensal.index, y="Lucro", title="Lucro Mensal",
                           labels={"Lucro": "Lucro Total", "Mes venda": "Mês"})
st.plotly_chart(fig_lucro_mensal)

# Top 10 Produtos por Receita
top_produtos_receita = df_filtrado.groupby("Produto")["Valor Venda"].sum().sort_values(ascending=False).head(10)
fig_top_produtos_receita = px.bar(top_produtos_receita, x="Valor Venda", y=top_produtos_receita.index,
                                  title="Top 10 Produtos por Receita", orientation='h', labels={"Valor venda": "Receita total"})
st.plotly_chart(fig_top_produtos_receita)

# 2.Desempenho por Produto
st.header("2. Desempenho por Produto")

# Tabela Interativa com Dados dos Produtos
st.subheader("Detalhes do produto")
st.dataframe(df_filtrado.groupby("Produto")[["Valor Venda", "Lucro", "Quantidade"]].sum().sort_values("Valor Venda",
            ascending=False))

# Boxplot do Valor Venda por Produto
st.header("Distribuição do Valor de Venda por Produto")
fig_boxplot = px.box(df_filtrado, x="Produto", y="Valor Venda", title="Boxplot do Valor de Venda por Produto",
                     labels={"Valor Venda": "Valor da Venda"})
st.plotly_chart(fig_boxplot)

st.header("Valor Total de Venda por Produto e Ano")

# Agrupando por Produto e Ano, somando o Valor Venda (já feito no código anterior)
df_agrupado = df_filtrado.groupby(["Produto", "Ano Venda"])["Valor Venda"].sum().reset_index()

# Criando o Gráfico de Barras Agrupadas
fig_barras_agrupadas = px.bar(df_agrupado, x="Ano Venda", y="Valor Venda", color="Produto",
                              barmode='group',  # Define o modo de barras agrupadas
                              title="Valor Total de Venda por Produto e Ano",
                              labels={"Ano Venda": "Ano da Venda", "Valor Venda": "Valor Total da Venda"})
st.plotly_chart(fig_barras_agrupadas)

# 3.Análise por Loja
st.header("3. Análise por Loja")

# Receita por Loja
receita_loja = df_filtrado.groupby("ID Loja")["Valor Venda"].sum()

# Criando o gráfico de pizza
fig_receita_loja = px.pie(
    receita_loja, 
    values="Valor Venda", 
    names=receita_loja.index, 
    title="Receita por Loja",
    labels={"Valor Venda": "Receita Total", "ID Loja": "ID da Loja"},
    hole=0.3  # Cria um "donut chart" com um buraco no centro (opcional)
)
st.plotly_chart(fig_receita_loja)

# 4. Análise por Cliente
st.header("4. Análise por Cliente")

# Top 10 Clientes por Receita
top_clientes_receita = df_filtrado.groupby("ID Cliente")["Valor Venda"].sum().sort_values(ascending=False).head(10)

# Criando o gráfico de barras verticais
fig_top_clientes_receita = px.bar(
    top_clientes_receita, 
    x=top_clientes_receita.index, 
    y="Valor Venda",
    title="Top 10 Clientes por Receita",
    labels={"ID Cliente": "ID do Cliente", "Valor Venda": "Receita Total"}
)

fig_top_clientes_receita.update_layout(xaxis_tickangle=-45) 
st.plotly_chart(fig_top_clientes_receita)