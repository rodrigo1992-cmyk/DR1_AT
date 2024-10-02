
import pandas as pd
import streamlit as st
from utils import *


######################################  INICIA O APLICATIVO ######################################
def exibir():
    filtro_partida = st.session_state.filtro_partida
    
    loading_bar(filtro_partida)
    if st.session_state.filtro_partida != 'Selecione':
        aba_jogadores(st.session_state.df_eventos)
