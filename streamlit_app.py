import streamlit as st
import pandas as pd
from datetime import datetime
import base64
import time
import urllib.parse

# Konfigurasi halaman
st.set_page_config(
    page_title="KaDe Pie Susu Lembang",
    page_icon="🥧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Custom
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
    }

    .product-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    .price-tag {
        font-size: 2rem;
        font-weight: 700;
        color: #ff6b6b;
    }

    .metric-card {
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
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

# PRODUK
PRODUCTS = {
    "Pie Susu Original": {"emoji": "🥧", "price": 20000, "desc": "Pie susu original khas"},
    "Pie Susu Coklat": {"emoji": "🍫", "price": 20000, "desc": "Coklat creamy lembut"},
    "Pie Susu Keju": {"emoji": "🧀", "price": 20000, "desc": "Keju premium lembut"},
    "Pie Susu Matcha": {"emoji": "🍃", "price": 20000, "desc": "Matcha creamy segar"},
    "Pie Talas Susu": {"emoji": "🍠", "price": 20000, "desc": "Talas manis lembut"},
    "Pie Susu Mix": {"emoji": "🎁", "price": 20000, "desc": "Mix semua rasa"}
}

WHATSAPP_NUMBER = "6285714196687"

# WA MESSAGE
def create_message(name, product, qty, address, notes=""):
    total = PRODUCTS[product]["price"] * qty
    msg = f"""🎉 KADE PIE SUSU LEMBANG 🎉

👤 {name}
📦 {product} x{qty}
💰 Rp {total:,}
📍 {address}
📝 {notes}

⏰ {datetime.now().strftime('%d/%m/%Y %H:%M')}
"""
    return msg

load_css()

# HEADER
st.markdown("""
<div class='main-header'>
    <h1>🥧 KaDe Pie Susu Lembang</h1>
    <p>Kelezatan Asli dalam Setiap Gigitan</p>
</div>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.markdown("## 📞 Kontak")
st.sidebar.markdown(f"WhatsApp: https://wa.me/{WHATSAPP_NUMBER}")
st.sidebar.markdown("Shopee: https://s.shopee.co.id/3qJnfNJNMF")

st.sidebar.markdown("""
### 🛒 Reseller

- Toko KaDe Ciwastra  
- Rumah Talas Bogor  
- ACR Cimahi  
- Rumah Mode Bandung  
""")

# KEUNGGULAN
st.markdown("## ✨ Kenapa KaDe?")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<div class='metric-card'>🥛<br>Bahan Premium</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='metric-card'>🔥<br>Fresh Daily</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='metric-card'>🚚<br>Pengiriman Cepat</div>", unsafe_allow_html=True)

# PRODUK
st.markdown("## 🍰 Produk Kami")

cols = st.columns(2)

for i, (name, data) in enumerate(PRODUCTS.items()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='product-card'>
            <h2>{data['emoji']}</h2>
            <h3>{name}</h3>
            <p>{data['desc']}</p>
            <div class='price-tag'>Rp {data['price']:,}</div>
        </div>
        """, unsafe_allow_html=True)

# FORM
st.markdown("## 📋 Order")

with st.form("order"):
    name = st.text_input("Nama")
    phone = st.text_input("WhatsApp")
    product = st.selectbox("Produk", list(PRODUCTS.keys()))
    qty = st.number_input("Qty", 1, 100, 1)
    address = st.text_area("Alamat")
    notes = st.text_area("Catatan")

    total = PRODUCTS[product]["price"] * qty

    st.markdown(f"""
    <div style="
        background:white;
        padding:1.5rem;
        border-radius:15px;
        text-align:center;
    ">
        <h3>💰 TOTAL PEMBAYARAN</h3>
        <h1 style="color:#ff6b6b;">Rp {total:,}</h1>
    </div>
    """, unsafe_allow_html=True)

    submit = st.form_submit_button("KIRIM VIA WHATSAPP")

    if submit and name and address:
        msg = create_message(name, product, qty, address, notes)
        url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

        st.success("Pesanan siap dikirim!")
        st.markdown(f"[Klik Kirim WhatsApp]({url})")

# FOOTER
st.markdown("""
<div class='footer'>
    <h3>Terima kasih sudah berkunjung 🥧</h3>
    <p>Semoga harimu manis seperti Pie Susu kami ❤️</p>
</div>
""", unsafe_allow_html=True)
