
import pandas as pd
import streamlit as st
from statsbombpy import sb

def barra_lateral():
    st.sidebar.header('Filtros')


def carga_dados():
    df_camp = sb.competitions()
    #df_partidas = sb.matches(competition_id=9, season_id=42)

    #Crio a lista de campeonatos
    list_camp = df_camp['competition_name'].drop_duplicates().tolist()
    list_camp.insert(0, 'Todos')

    #Crio o Seletor
    select_camp = st.sidebar.selectbox('Filtrar Campeonato', list_camp)

    #Aplico a condição para só filtrar se houver seleção
    if select_camp != 'Todos':
        df_camp = df_camp.loc[df_camp['competition_name'] == select_camp]


    st.dataframe(df_camp)
    #st.dataframe(df_partidas)


carga_dados()
