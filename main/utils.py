import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def afficher_graphique_action(ticker, date_debut, date_fin, type_graphique='line', date_achat=None):
    # Récupérer les données de l'action
    data = yf.download(ticker, start=date_debut, end=date_fin)

    # Vérifier que des données ont été récupérées
    if data.empty:
        print("Aucune donnée trouvée pour cette période.")
        return

    # Convertir l'index en datetime si nécessaire
    if not pd.api.types.is_datetime64_any_dtype(data.index):
        data.index = pd.to_datetime(data.index)

    # Créer le graphique en fonction du type demandé
    fig = make_subplots(specs=[[{"secondary_y": False}]])

    hover_texts = []

    if type_graphique == 'line':
        for date, value in data.iterrows():
            if date_achat in data.index:
                prix_achat = data.loc[date_achat, 'Close']
                pl = value['Close'] - prix_achat
                pl_pct = (pl / prix_achat) * 100
                hover_texts.append(
                    f'Date: {date}<br>Prix: {value["Close"]:.2f}<br>Achat: {prix_achat:.2f}<br>P/L: {pl:.2f}<br>P/L (%): {pl_pct:.2f}%')
            else:
                hover_texts.append(f'Date: {date}<br>Prix: {value["Close"]:.2f}')
        fig.add_trace(
            go.Scatter(x=data.index, y=data['Close'], mode='lines', name=ticker, text=hover_texts, hoverinfo='text'),
            secondary_y=False,
        )
    elif type_graphique == 'candlestick':
        for date, value in data.iterrows():
            if date_achat in data.index:
                prix_achat = data.loc[date_achat, 'Close']
                pl = value['Close'] - prix_achat
                pl_pct = (pl / prix_achat) * 100
                hover_texts.append(
                    f'Date: {date}<br>Open: {value["Open"]:.2f}<br>High: {value["High"]:.2f}<br>Low: {value["Low"]:.2f}<br>Close: {value["Close"]:.2f}<br>Achat: {prix_achat:.2f}<br>P/L: {pl:.2f}<br>P/L (%): {pl_pct:.2f}%')
            else:
                hover_texts.append(
                    f'Date: {date}<br>Open: {value["Open"]:.2f}<br>High: {value["High"]:.2f}<br>Low: {value["Low"]:.2f}<br>Close: {value["Close"]:.2f}')
        fig.add_trace(
            go.Candlestick(x=data.index,
                           open=data['Open'],
                           high=data['High'],
                           low=data['Low'],
                           close=data['Close'],
                           name=ticker,
                           text=hover_texts,
                           hoverinfo='text'),
            secondary_y=False,
        )
    else:
        print("Type de graphique non supporté.")
        return

    # Ajouter une ligne pointillée pour la date d'achat si elle est spécifiée
    if date_achat:
        date_achat = pd.to_datetime(date_achat)
        if date_achat in data.index:
            prix_achat = data.loc[date_achat, 'Close']
            #fig.add_trace(
                #go.Scatter(x=[date_achat, date_achat], y=[data['Low'].min(), data['High'].max()],
                           #mode='lines', line=dict(dash='dot', color='red'), name='Date Achat'),
                #secondary_y=False,
            #)
            fig.add_trace(
                go.Scatter(x=data.index, y=[prix_achat] * len(data), mode='lines',
                           line=dict(dash='dot', color='cyan'), name='Prix Achat'),
                secondary_y=False,
            )
        else:
            print("La date d'achat n'est pas dans l'intervalle des dates fournies.")

    # Ajouter des titres et des labels
    fig.update_layout(
        title=f"{ticker} de {date_debut} à {date_fin}",
        xaxis_title='Date',
        yaxis_title='Prix',
        xaxis_rangeslider_visible=False,
        hovermode='x',
    )

    # Afficher le graphique
    fig.show()
