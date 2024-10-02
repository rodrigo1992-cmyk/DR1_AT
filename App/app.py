import streamlit as st
from utils import *

st.set_page_config(layout="wide")

st.sidebar.header('Navegação')
page = st.sidebar.selectbox("",["Análise de Partidas", "Análise de Jogadores"])

st.sidebar.header('Filtros')
filtros_barra_lateral()

if page == "Análise de Partidas":
    import Partidas
    Partidas.exibir()
elif page == "Análise de Jogadores":
    import Jogadores
    Jogadores.exibir()
