import streamlit as st

def model_info_page():
    st.title("🚀 LSTM Model Overview")
    
    st.markdown("""
    ## 🤖 Understanding LSTM: Powering Stock Predictions
    The **Long Short-Term Memory (LSTM)** network is a specialized type of **Recurrent Neural Network (RNN)**
    designed to **learn from past data** and make accurate **time-series predictions**. 
    
    ---
    
    ## 🔍 **Why LSTM for Stock Market Prediction?**
    ✅ Captures **long-term dependencies** in stock price patterns  
    ✅ Overcomes **vanishing gradient issues** common in RNNs  
    ✅ Maintains a **memory state**, enabling precise forecasting  
    
    ---
    
    ## 🏗 **Model Architecture**
    ```
    Input → LSTM Layers → Dense Layer → Output (Stock Price Prediction)
    ```
    - **Input Layer** 📥: Receives normalized historical stock prices
    - **LSTM Layers** 🔄: Learn sequential patterns and trends
    - **Dense Layer** 🎯: Produces final stock price prediction
    - **Activation Function** ⚡: Uses **Sigmoid** or **Tanh** for stability
    
    ---""")

    # Create a two-column layout
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## 🔬 **Training Process**")
        st.markdown("##### **1️⃣ Data Preprocessing**")
        st.markdown("- Normalization with **MinMaxScaler** (0 to 1 range)  \n- Creating sequences from past stock data")
        
        st.markdown("##### **2️⃣ Model Training**")
        st.markdown("- **Loss Function** 🎯: Mean Squared Error (MSE)  \n- **Optimizer** ⚡: Adam for fast convergence  \n- **Epochs** ⏳: Typically **50-100** for accuracy")

    with col2:
        st.markdown("##### **3️⃣ Prediction Workflow**")
        st.markdown(
            "- Accepts historical price data 📊  \n"
            "- Normalizes input for better accuracy ⚖️  \n"
            "- LSTM layers learn the patterns 🔄  \n"
            "- Outputs future stock price predictions 📈  \n"
            "- Converts predicted value back to real price scale 🔄"
        )
    
    st.markdown("""
    ---
    
    ## 🎯 **Why Use This Model?**
    - 📉 **Detects Trends & Patterns**: Learns from past stock data
    - 📊 **Minimizes Errors**: Uses robust optimization techniques
    - 🔥 **Real-World Applications**: Applied in financial forecasting, cryptocurrency, and demand prediction
    
    ---
    
    💡 *LSTM is at the heart of modern AI-driven stock market predictions, providing deep insights into financial trends.*
    
    **🚀 Start analyzing your stocks with the power of LSTM today!**
    """)
    
    st.info("LSTM models are widely used for time-series forecasting, making them a powerful tool for stock market prediction.")