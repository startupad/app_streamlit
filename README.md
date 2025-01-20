# Spese Aarhus 🇩🇰 | Marcos Trainsheep

Questa applicazione è stata creata per gestire le **spese** quotidiane e le **entrate** a Aarhus, in Danimarca. L'applicazione consente di tenere traccia delle transazioni, visualizzare il totale delle spese, aggiungere nuove voci, e scaricare i dati in formato CSV.

L'app è progettata per essere semplice, ma potente, con un'interfaccia user-friendly sviluppata utilizzando **Streamlit** e un backend **SQLite** per la gestione dei dati.

## Funzionalità

L'applicazione permette agli utenti di:

1. **Visualizzare le transazioni**: Una lista completa di tutte le spese e entrate registrate, con la possibilità di scaricare il file CSV delle transazioni.
2. **Aggiungere nuove transazioni**: Gli utenti possono inserire una spesa o un'entrata con la data, la categoria, una breve descrizione e l'importo.
3. **Gestire categorie predefinite**: Le transazioni possono essere categorizzate come "Cibo", "Trasporti", "Alloggio", "Divertimento" o "Altro".
4. **Interfaccia moderna e pulita**: L'app è progettata per offrire un'esperienza utente semplice e gradevole, con una chiara divisione tra spese ed entrate.

## Tecnologie Utilizzate

- **Streamlit**: per la creazione dell'interfaccia utente.
- **SQLite**: per la gestione dei dati in un database locale.
- **Python**: per la logica dell'applicazione.
- **Pandas**: per la manipolazione dei dati.
- **Matplotlib** (opzionale, se il grafico è implementato): per la visualizzazione grafica delle spese ed entrate.

## Installazione

1. **Clona il repository**:

   ```bash
   git clone https://github.com/tuo-utente/spese-aarhus.git
   cd spese-aarhus
   ```

2. **Installa le dipendenze**:

   Assicurati di avere **Python 3.x** installato, quindi installa le dipendenze necessarie utilizzando **pip**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Esegui l'applicazione**:

   Per avviare l'applicazione, esegui il comando seguente:

   ```bash
   streamlit run app.py
   ```

4. **Accedi all'app**:

   Una volta avviato il server, apri il browser e visita l'URL locale generato (di solito **http://localhost:8501**).

## Struttura del Database

L'applicazione utilizza un database SQLite per memorizzare le transazioni. La struttura del database è la seguente:

- **Tabella `spese`**:
  - `id`: Identificativo univoco della transazione (chiave primaria).
  - `data`: Data della transazione (formato: gg/mm/aaaa).
  - `categoria`: Categoria della transazione (Cibo, Trasporti, Alloggio, Divertimento, Altro).
  - `descrizione`: Una breve descrizione della transazione.
  - `importo`: L'importo della transazione (positivo per le entrate, negativo per le spese).

## Utilizzo

### Visualizzare le Transazioni

1. **Visualizza le spese e le entrate** registrate nel sistema.
2. Le transazioni sono presentate in un formato tabellare con la data, categoria, descrizione e importo.
3. È possibile scaricare i dati in formato CSV per ulteriori elaborazioni.

### Aggiungere una Nuova Transazione

1. **Aggiungi una spesa o entrata** inserendo la data, la categoria, una descrizione e l'importo.
2. L'applicazione distingue automaticamente tra spese (importo negativo) e entrate (importo positivo).

## Personalizzazione

Se desideri personalizzare le categorie o altre impostazioni dell'app, puoi modificare direttamente il codice nel file **`app.py`**. Puoi anche aggiungere altre funzionalità o miglioramenti come desideri.

## Contribuire

Se vuoi contribuire al progetto, sei il benvenuto! Puoi aprire una **pull request** con nuove funzionalità, correzioni di bug o miglioramenti.

## Licenza

Questo progetto è distribuito con la licenza **MIT**. Vedi il file `LICENSE` per i dettagli.

## Contatti

Se hai domande o vuoi maggiori informazioni, puoi contattarmi via email o visitare il mio profilo su GitHub.

---

**Autore:** Marco Melloni
**Data di Creazione:** Gennaio 2025
