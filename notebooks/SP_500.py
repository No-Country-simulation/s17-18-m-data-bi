import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import ta

# Botón para elegir color de fondo de la página
st.subheader('Visualización de Acciones del S&P 500')
color_pagina = st.color_picker('Selecciona un color para la página')

# Aplicar color de fondo a la página
st.markdown(f"""
    <style>
    .main {{
        background-color: {color_pagina};
    }}
    </style>
""", unsafe_allow_html=True)

# Título de la aplicación
st.title('Selecciona tres Acciones y Grafica, Compara y Descarga')

# Descripción
st.write('Esta aplicación te permite visualizar los datos históricos de las principales acciones del S&P 500.')

# Lista de símbolos del S&P 500 (puedes agregar más)
sp500_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'JPM', 'JNJ', 'V', 'NVDA']

# Crear un selector en Streamlit para elegir una acción del S&P 500
selected_symbol = st.selectbox('Selecciona una acción del S&P 500', sp500_symbols)

# Crear dos selectores más para elegir acciones adicionales
selected_symbol2 = st.selectbox('Selecciona una segunda acción del S&P 500', sp500_symbols)
selected_symbol3 = st.selectbox('Selecciona una tercera acción del S&P 500', sp500_symbols)

# Selección de rango de fechas
start_date = st.date_input('Fecha de inicio', value=pd.to_datetime('2020-01-01'))
end_date = st.date_input('Fecha de fin', value=pd.to_datetime('today'))

# Botón para cargar datos y visualizar
if st.button('Mostrar gráfico'):
    # Descargar datos de Yahoo Finance
    data = yf.download([selected_symbol, selected_symbol2, selected_symbol3], start=start_date, end=end_date)

    if not data.empty:
        # Mostrar gráfico del precio de cierre
        st.subheader(f'Datos históricos de {selected_symbol}, {selected_symbol2} y {selected_symbol3}')
        st.line_chart(data['Close'])

        # Mostrar gráfico de candelas
        st.subheader('Gráfico de candelas')
        fig = go.Figure(data=[go.Candlestick(x=data.index,
                                            open=data['Open'][selected_symbol],
                                            high=data['High'][selected_symbol],
                                            low=data['Low'][selected_symbol],
                                            close=data['Close'][selected_symbol],
                                            name=selected_symbol),
                                    go.Candlestick(x=data.index,
                                                    open=data['Open'][selected_symbol2],
                                                    high=data['High'][selected_symbol2],
                                                    low=data['Low'][selected_symbol2],
                                                    close=data['Close'][selected_symbol2],
                                                    name=selected_symbol2),
                                    go.Candlestick(x=data.index,
                                                    open=data['Open'][selected_symbol3],
                                                    high=data['High'][selected_symbol3],
                                                    low=data['Low'][selected_symbol3],
                                                    close=data['Close'][selected_symbol3],
                                                    name=selected_symbol3)])
        fig.update_layout(title='Gráfico de candelas', xaxis_title='Fecha', yaxis_title='Precio')
        st.plotly_chart(fig)

        # Mostrar recomendaciones de análisis bursátiles financieros
        st.subheader('Recomendaciones de análisis bursátiles financieros')

        # Calcula la media móvil de 50 días
        data['MA50'] = data['Close'][selected_symbol].rolling(window=50).mean()

        # Calcula la media móvil de 200 días
        data['MA200'] = data['Close'][selected_symbol].rolling(window=200).mean()

        # Compara las medias móviles para determinar la tendencia
        if data['MA50'].iloc[-1] > data['MA200'].iloc[-1]:
            st.write('La tendencia es alcista')
        elif data['MA50'].iloc[-1] < data['MA200'].iloc[-1]:
            st.write('La tendencia es bajista')
        else:
            st.write('La tendencia es neutra')

        # Calcula el RSI (Relative Strength Index)
        data['RSI'] = ta.momentum.RSIIndicator(data['Close'][selected_symbol], window=14).rsi()

        # Compara el RSI para determinar si la acción está sobrecomprada o sobre vendida
        if data['RSI'].iloc[-1] > 70:
             st.write('La acción está sobrecomprada')
        elif data['RSI'].iloc[-1] < 30:
            st.write('La acción está sobre vendida')
        else:
            st.write('La acción está en un nivel neutral')

        # Opción para descargar datos
        st.subheader('Descargar datos')
        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')
        csv = convert_df(data)
        st.download_button(
            label="Descargar datos como CSV",
            data=csv,
            file_name='datos.csv',
            mime='text/csv',
        )
    else:
        st.error('No se encontraron datos para este rango de fechas.')