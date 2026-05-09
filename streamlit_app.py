import streamlit as st
import pandas as pd
from datetime import datetime
import base64
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="KaDe Pie Susu Bandung",
    page_icon="🥧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Custom untuk desain menarik
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .product-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 100%;
        cursor: pointer;
    }
    
    .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2) !important;
    }
    
    .price-tag {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .order-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem;
        border-radius: 20px;
        color: white;
        text-align: center;
    }
    
    .whatsapp-btn {
        background: linear-gradient(45deg, #25D366, #128C7E) !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        padding: 1rem 2rem !important;
        box-shadow: 0 8px 25px rgba(37,211,102,0.4) !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: #333;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
    }
    
    .footer {
        background: #333;
        color: white;
        padding: 2rem;
        text-align: center;
        border-radius: 20px;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Data Produk
PRODUCTS = {
    "🥧 Classic Pie Susu": {
        "price": 25000,
        "desc": "Pie susu original rasa susu kental manis khas Bandung"
    },
    "🍋 Lemon Pie Susu": {
        "price": 28000,
        "desc": "Sensasi segar lemon dengan tekstur lembut creamy"
    },
    "🍓 Strawberry Pie Susu": {
        "price": 30000,
        "desc": "Stroberi segar bertemu sus
