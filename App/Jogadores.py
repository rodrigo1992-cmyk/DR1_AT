
import pandas as pd
import streamlit as st
from utils import *


######################################  INICIA O APLICATIVO ######################################
def exibir():

    df_partidas_filtrado = st.session_state.df_partidas_filtrado
    df_eventos = st.session_state.df_eventos
    filtro_camp = st.session_state.filtro_camp
    filtro_ano = st.session_state.filtro_ano
    filtro_partida = st.session_state.filtro_partida

    if df_partidas_filtrado.empty:
        pass
    else:
        home_team = df_partidas_filtrado.home_team.values[0]
        away_team  = df_partidas_filtrado.away_team.values[0]
    
    loading_bar(filtro_partida)
    
    if st.session_state.filtro_partida != 'Selecione':

        jogadores = df_eventos['player'].unique()
    
        col_a, col_b = st.columns(2)
        with col_a:
            jogadorA = st.selectbox("Selecione o Jogador", jogadores,key='jogadorA')
            dados_jogador(df_eventos, jogadorA, 'csv_jogadorA')
        with col_b:
            jogadorB = st.selectbox("Selecione o Jogador", jogadores,key='jogadorB')
            dados_jogador(df_eventos, jogadorB, 'csv_jogadorB')
 
