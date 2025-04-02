import streamlit as st
from pages.stock_prediction import stock_prediction_page
from pages.about import about_page
from pages.model_info import model_info_page

def main():
    st.set_page_config(
        page_title="Stock Market Predictor",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #f0f2f6, #e6e9ef);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to bottom, #ffffff, #f0f2f6);
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar navigation
    pages = {
        "Stock Prediction": stock_prediction_page,
        "Model Information": model_info_page,
        "About": about_page
    }

    st.sidebar.title("🧠 Stock Predictor Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Run the selected page
    pages[selection]()

if __name__ == "__main__":
    main()