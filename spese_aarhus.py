import streamlit as st
import pandas as pd
import sqlite3

# Connetti al database SQLite (o creane uno se non esiste)
conn = sqlite3.connect('spese_aarhus.db')
c = conn.cursor()

# Crea una tabella nel database se non esiste già
c.execute('''CREATE TABLE IF NOT EXISTS spese (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                categoria TEXT,
                descrizione TEXT,
                importo REAL)''')

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

# Menu per scegliere tra visualizzare le spese o aggiungerne di nuove
scelta = st.radio("Cosa vuoi fare?", ['Visualizza Spese', 'Aggiungi una Spesa'])

if scelta == 'Visualizza Spese':
    # Recupera le spese dal database
    query = "SELECT * FROM spese"
    spese_db = pd.read_sql(query, conn)

    # Mostra la data nel formato europeo (gg/mm/aaaa)
    spese_db['data'] = pd.to_datetime(spese_db['data'], errors='coerce').dt.strftime('%d/%m/%Y')

    st.write("### Spese registrate:")
    st.write(spese_db)

    # Bottone per scaricare il file CSV delle spese
    st.download_button(
        label="Scarica le tue spese come CSV",
        data=spese_db.to_csv(index=False),
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
        # Inserisci la spesa nel database
        c.execute("INSERT INTO spese (data, categoria, descrizione, importo) VALUES (?, ?, ?, ?)",
                  (data.strftime('%d/%m/%Y'), categoria, descrizione, importo))
        conn.commit()
        st.success('Spesa aggiunta con successo!')

# Chiudi la connessione al database quando l'app finisce
conn.close()
