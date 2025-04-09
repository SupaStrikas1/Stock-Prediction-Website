import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import plotly.graph_objects as go
import openai
from google import genai


def stock_prediction_page():
    st.title("📈 Stock Market Prediction with LSTM")
    
    # Sidebar inputs
    st.sidebar.header("Stock Selection")
    stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL):", "GOOG")
    prediction_days = 7
    
    # Load Model
    try:
        model = load_model("stock_lstm_model.h5")  
        st.success("✅ Model Loaded Successfully!")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # Fetch Stock Data
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=3650)).strftime('%Y-%m-%d')
    
    with st.spinner('Fetching Stock Data...'):
        try:
            data = yf.download(stock_symbol, start=start_date, end=end_date)
        except Exception as e:
            st.error(f"Error fetching stock data: {e}")
            return

    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Historical Data", "📉 Price Chart", "🔮 Predictions", "🤖 AI Trend Analysis"])

    with tab1:
        st.subheader(f"Historical Stock Data for {stock_symbol}")
        st.dataframe(data.tail(50).iloc[::-1], use_container_width=True)

    with tab2:
        # Interactive Plotly Chart

        st.subheader("📉 Historical Stock Prices")

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(data['Close'], label='Closing Price', color='blue')
        ax.set_xlabel("Date")
        ax.set_ylabel("Stock Price")
        ax.legend()
        st.pyplot(fig)

        x=data.index.values[1500:]
        y=data['Close'].values.ravel()

        hover_text=[f'Date: {pd.to_datetime(date).strftime('%Y-%m-%d')}<br>Stock Price: ${price:.2f}' for date, price in zip(x,y)]

        graph=go.Figure(data=go.Scatter(x=x,y=y,mode='lines', hovertext=hover_text))
        graph.update_layout(
            title={
                'text':f'Stock Prices of {stock_symbol} of last 5 yers',
                'x':0.5,
                'y':0.9,
                'xanchor':'center',
                'yanchor':'top'
            },
            xaxis=dict(
                title="Year"
            ),
            yaxis=dict(
                title="Stock Price (in USD)"
            )
        )
        st.plotly_chart(graph, use_container_width=True)

    with tab3:

        st.subheader("🔮 Future Stock Price Predictions (Next Week)")

        # Data Preparation for Prediction
        scaler = MinMaxScaler(feature_range=(0,1))
        data_scaled = scaler.fit_transform(data['Close'].values.reshape(-1,1))

        # Create Input Sequence
        x_input = np.array(data_scaled[-100:]).reshape(1, 100, 1)

        # Predict Next Days' Stock Prices
        future_predictions = []
        last_100_days = x_input.copy()

        for _ in range(prediction_days):
            next_pred = model.predict(last_100_days)[0][0]
            future_predictions.append(next_pred)
            last_100_days = np.append(last_100_days[:, 1:, :], [[[next_pred]]], axis=1)

        # Convert Predictions Back to Original Scale
        future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))
        future_dates = [datetime.today() + timedelta(days=i+1) for i in range(prediction_days)]

        # Prediction Table
        future_df = pd.DataFrame({
            'Date': future_dates, 
            'Predicted Price': future_predictions.flatten()
        })
        st.dataframe(future_df, use_container_width=True)

        # Key Statistics
        st.subheader("Prediction Insights")
        col1, col2, col3 = st.columns(3)
        col1.metric("Next Day Prediction", f"${future_predictions[0][0]:.2f}")

        st.subheader(f"📰 Latest News for {stock_symbol}")

        st.spinner('Fetching latest news...')

        stock = yf.Ticker(stock_symbol)
        news = stock.news

        for i, article in enumerate(news[:5]):
            with st.container():
                st.markdown(f"{article['content']['title']}")
                st.markdown(f"**Summary:** {article['content']['summary']}")
                st.markdown(f"[Read full article]({article['content']['canonicalUrl']['url']})")
                st.divider()

    # Modified version of the AI Trend Analysis tab
    with tab4:
        st.subheader(f"🤖 AI Trend Analysis for {stock_symbol}")
        
        # Button to generate analysis
        if st.button("Generate AI Trend Analysis"):
            client = genai.Client(api_key="AIzaSyBv1LaEVK6hhvgrAOfzeRuFFTwuI1qLtlk")

            prompt=f'''You are a stock market analyst expert. Analyze the current trend for {stock_symbol} stock based on the current affairs: 

                    Please provide:
                    1. A brief analysis of the current trend
                    2. Key factors that might be affecting the stock price
                    3. A short-term outlook (1-7 days)
                    
                    Keep your response concise and actionable.'''

            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )
                        
                        # Display in a nice format
            st.markdown(response.text)
            
            # Add timestamp
            st.caption(f"Analysis generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Information about the AI analysis
        with st.expander("About AI Trend Analysis"):
            st.markdown("""
            The AI Trend Analysis uses machine learning to evaluate:
            - Historical stock price data
            - Recent news and events
            - Technical indicators
            - Market sentiment
            
            This analysis is for informational purposes only and should not be considered financial advice.
            Always do your own research before making investment decisions.
            """)

    st.success("✅ Stock Prediction Analysis Complete!")