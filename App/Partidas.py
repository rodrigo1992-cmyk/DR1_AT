
import pandas as pd
import streamlit as st
from utils import *

######################################  INICIA O APLICATIVO ######################################

#Carrego as variáveis de sessão em variáveis locais para facilitar na hora de passar como parâmetro das funções
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
    resumo_selecao(df_partidas_filtrado, df_eventos, filtro_camp, filtro_ano, filtro_partida)
    
    if filtro_partida != 'Selecione':
        tab_graf, tab_tabelas = st.tabs(['GRÁFICOS', 'TABELAS'])

        with tab_graf:
            col_a, col_b = st.columns(2)
            with col_a:
                graficos_partida(df_partidas_filtrado, df_eventos, home_team)
            with col_b:
                graficos_partida(df_partidas_filtrado, df_eventos, away_team)

            with st.container(height=920):
                tipo_label, tipo, team = filtro_pass_plot(home_team,away_team)
                df_pass, mak_complete = data_pass_plot(df_eventos,tipo,team)
                with st.spinner('Processando o Mapa...'):
                    time.sleep(3)
                    graf_pass_plot(df_pass, mak_complete, tipo_label, team)

            with st.container(height=820):
                team_heatmap = filtro_heat_plot(df_eventos,home_team,away_team)
                df_pressure = dados_heat_plot(df_eventos,team_heatmap)
                with st.spinner('Processando o Mapa...'):
                    time.sleep(3)
                    graf_heat_plot(df_pressure,team_heatmap)

        with tab_tabelas:
            tabelas_pg_partida(df_partidas_filtrado,df_eventos)
