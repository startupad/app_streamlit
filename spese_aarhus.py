import streamlit as st
import pandas as pd

# Impostazione sfondo bianco
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: white;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Titolo dell'app
st.title('Gestione delle spese a Aarhus')

# Inizializza un DataFrame vuoto per memorizzare le spese se non esiste già
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = pd.DataFrame(columns=['Data', 'Categoria', 'Descrizione', 'Importo'])

# Menu per scegliere tra visualizzare le spese o aggiungerne di nuove
scelta = st.radio("Cosa vuoi fare?", ['Visualizza Spese', 'Aggiungi una Spesa'])

if scelta == 'Visualizza Spese':
    # Visualizza la tabella delle spese
    st.write("### Spese registrate:")

    # Mostra la data nel formato europeo (gg/mm/aaaa)
    st.session_state['expenses']['Data'] = pd.to_datetime(st.session_state['expenses']['Data'], errors='coerce').dt.strftime('%d/%m/%Y')

    st.write(st.session_state['expenses'])

    # Bottone per scaricare il file CSV delle spese
    st.download_button(
        label="Scarica le tue spese come CSV",
        data=st.session_state['expenses'].to_csv(index=False),
        file_name='spese_aarhus.csv',
        mime='text/csv'
    )

elif scelta == 'Aggiungi una Spesa':
    # Input dell'utente per le nuove spese
    data = st.date_input('Data della spesa', format='DD/MM/YYYY')  # Imposta il formato della data
    categoria = st.selectbox('Categoria della spesa', ['Cibo', 'Trasporti', 'Alloggio', 'Divertimento', 'Altro'])
    descrizione = st.text_input('Descrizione della spesa')
    importo = st.number_input('Importo', min_value=0.0, format="%.2f")

    # Bottone per aggiungere una nuova spesa
    if st.button('Aggiungi spesa'):
        new_expense = pd.DataFrame([[data, categoria, descrizione, importo]], columns=['Data', 'Categoria', 'Descrizione', 'Importo'])
        st.session_state['expenses'] = pd.concat([st.session_state['expenses'], new_expense], ignore_index=True)
        st.success('Spesa aggiunta con successo!')
