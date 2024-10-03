
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

        with st.form(key='my_form'):
            st.write("Selecione os jogadores a comparar:")
            col_a, col_b = st.columns(2)

            with col_a:
                jogadorA = st.selectbox("Selecione o Jogador A", df_eventos['player'].unique())

            with col_b:
                jogadorB = st.selectbox("Selecione o Jogador B", df_eventos['player'].unique())
            
            submit_button = st.form_submit_button(label='Enviar')
            
        if submit_button:
            dados_jogador(df_eventos, jogadorA, jogadorB)
