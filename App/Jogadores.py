
import pandas as pd
import streamlit as st
from utils import *

filtro_partida = st.session_state.filtro_partida


######################################  INICIA O APLICATIVO ######################################
def exibir():
    loading_bar(filtro_partida)
    if st.session_state.filtro_partida != 'Selecione':
        aba_jogadores(st.session_state.df_eventos)
