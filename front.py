import streamlit as st
import pandas as pd

st.title("Gerenciador de Usuários")
st.write("Usuários")

usuarios = [{"Nome": 'Bárbara', "Sobrenome": 'Lopes', "Idade": 22, "Localidade":'Rio de Janeiro',},
            {"Nome": 'Júlia', "Sobrenome": 'Mendes', "Idade": 43, "Localidade":'Minas Gerais',},
            {"Nome": 'Bianca', "Sobrenome": 'Santos', "Idade": 30, "Localidade":'São Paulo',},
            {"Nome": 'Luiz', "Sobrenome": 'Ronaldo', "Idade": 34, "Localidade":'São Paulo',},
            {"Nome": 'Juan', "Sobrenome": 'Fernandes', "Idade": 25, "Localidade":'Rio de Janeiro',},
            {"Nome": 'Marisa', "Sobrenome": 'Orleans', "Idade": 46, "Localidade":'Minas Gerais',},
]



dt = st.dataframe(usuarios)