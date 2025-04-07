# app.py
import streamlit as st
from eda_report import load_data, treat_data, load_continent_data, merge_datasets, select_year
import plotly.express as px

st.set_page_config(page_title="EDA Dashboard", layout="wide")

# Título
st.title("Exploração de Dados Econômicos")

# Carregamento de dados
df = load_data()
df = treat_data(df)
continents = load_continent_data()
df_final = merge_datasets(df, continents)

# Filtros interativos
years = sorted(df_final['time'].unique())
selected_year = st.sidebar.selectbox("Selecione o ano:", years, index=len(years)-1)

variables = ['gdp_growth', 'inflation', 'real_interest_rate', 'reer']
y_var = st.sidebar.selectbox("Variável Y:", variables)
x_var = st.sidebar.selectbox("Variável X (para gráfico de dispersão):", variables)

# Dados filtrados
df_filtered = select_year(df_final, selected_year)

# Gráfico de boxplot por continente
st.subheader(f"Boxplot de {y_var} por Continente ({selected_year})")
box_fig = px.box(df_filtered, x='continent', y=y_var, color='continent')
st.plotly_chart(box_fig, use_container_width=True)

# Gráfico de dispersão
st.subheader(f"Dispersão: {x_var} vs {y_var} ({selected_year})")
scatter_fig = px.scatter(df_filtered, x=x_var, y=y_var, color='continent')
st.plotly_chart(scatter_fig, use_container_width=True)
