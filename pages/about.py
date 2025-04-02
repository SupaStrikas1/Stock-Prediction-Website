import streamlit as st

def about_page():
    st.title("📚 About Stock Market Predictor")

    # 🔍 How It Works - Two Column Layout
    st.markdown("## 🔍 **How It Works**")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ##### 🛠️ **Step 1: Data Collection**
        - 📜 Retrieves historical stock prices using **Yahoo Finance (yfinance)**  
        - Covers multiple timeframes (days, weeks, months)  
        - Fetches real-time updates to keep predictions current  

        ##### 🔄 **Step 2: Data Preprocessing**
        - Cleans and **normalizes stock data** for consistency  
        - Converts raw prices into a format suitable for AI analysis  
        - Creates **time-series sequences** for better trend detection  
        
        ##### 🤖 **Step 3: LSTM Model Processing**
        - Uses **Long Short-Term Memory (LSTM)**, a deep learning model  
        - Learns patterns from past stock movements  
        - Identifies trends and market fluctuations  
        """)

    with col2:
        st.markdown("""
        ##### 📈 **Step 4: Price Prediction**
        - AI generates **short-term forecasts** based on learned data  
        - Provides insights into potential market movements  
        - Predicts **multi-day stock trends** with reasonable accuracy  

        ##### 📊 **Step 5: Visualization & Insights**
        - Displays **interactive stock charts** with historical & predicted prices  
        - Allows users to track stock trends with real-time updates  
        - Enables better decision-making with AI-powered insights  
        """)

    # 📌 Two-column layout for Tech Stack & Key Features
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## 🛠️ **Technology Stack**")
        st.markdown("""
        - 🐍 **Python** – Backend Processing  
        - 🌐 **Streamlit** – Web Application Framework  
        - 🤖 **TensorFlow/Keras** – Deep Learning  
        - 📈 **LSTM Neural Network** – Stock Trend Prediction  
        - 📊 **YFinance** – Real-Time Stock Data Fetching  
        - 📉 **Matplotlib & Plotly** – Data Visualization  
        """)

    with col2:
        st.markdown("## 🌟 **Key Features**")
        st.success("""
        ✅ Live stock price updates  
        ✅ AI-driven trend analysis 🤖  
        ✅ Interactive & user-friendly charts 📊  
        ✅ Multi-day stock price predictions 📈  
        ✅ Easy-to-use interface 🎨  
        ✅ No coding knowledge required! 🛠️  
        """)

    # 📌 Disclaimer Section at Bottom
    st.markdown("---")
    st.warning("""
    ⚠️ **Disclaimer:**  
    This application provides **probabilistic predictions** and should **not** be considered **financial advice**.  
    Always conduct **your own research** before making investment decisions.
    """)
