import streamlit as st
import pandas as pd
from datetime import datetime
import base64
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="KaDe Pie Susu Lembang",
    page_icon="",
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
        border: 3px solid transparent;
    }
    
    .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2) !important;
        border-color: #ff6b6b;
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
        color: white !important;
        border: none !important;
        width: 100%;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: #333;
    }
    
    .stButton > button {
        border-radius: 50px !important;
        font-weight: 600 !important;
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
    
    .success-box {
        background: linear-gradient(135deg, #56ab2f, #a8e6cf);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Data Produk 
PRODUCTS = {
    "Pie Susu Original": {
        "emoji": "🥧",
        "price": 20000,
        "desc": "Pie susu original rasa susu khas"
    },
    "Pie Susu Coklat": {
        "emoji": "🍫", 
        "price": 20000,
        "desc": "Rasa coklat dengan tekstur lembut creamy"
    },
    "Pie Susu Keju": {
        "emoji": "🧀",
        "price": 20000,
        "desc": "Keju premium bertemu susu krim lembut"
     },
    "Pie Susu Matcha": {
        "emoji": "🍃",
        "price": 20000,
        "desc": "Matcha yang khas bertemu susu krim lembut"
     },
    "Pie Talas Susu": {
        "emoji": "🍠",
        "price": 20000,
        "desc": "Talas segar bertemu susu krim lembut"
    },
    "Pie Susu Mix": {
        "emoji": "",
        "price": 20000,
        "desc": "Mix 7 rasa spesial, cocok untuk hadiah"
    }
}

# Nomor WhatsApp 
WHATSAPP_NUMBER = "6285714196687"  # 

# Fungsi untuk generate WhatsApp message
@st.cache_data
def create_whatsapp_message(name, product, qty, address, notes=""):
    total = PRODUCTS[product]["price"] * int(qty)
    message = f"""🎉 HALO KADE PIE SUSU LEMBANG! 🎉

👤 Nama: {name}
📦 Pesanan: {product} x{qty}
💰 Total: Rp {total:,}
📍 Alamat: {address}
📝 Catatan: {notes}

⏰ Waktu: {datetime.now().strftime('%d/%m/%Y %H:%M')}

Terima kasih! 🥧✨"""
    return message

# Load CSS
load_css()

# Header
st.markdown("""
<div class='main-header'>
    <h1 style='font-size: 3.5rem; margin: 0;'>Ka<span style='color: #fff;'>De</span> Pie Susu Lembang</h1>
    <p style='font-size: 1.5rem; margin: 1rem 0;'>Kelezatan Asli dalam Setiap Gigitan! ✨</p>
    <h3 style='margin: 0;'>Panggang Fresh Setiap Hari</h3>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📞 Kontak Cepat")
st.sidebar.markdown(f"**WhatsApp:** [wa.me/{WHATSAPP_NUMBER}](https://wa.me/{WHATSAPP_NUMBER})")
st.sidebar.markdown(f"**Shopee:** https://s.shopee.co.id/3qJnfNJNMF?share_channel_code=1")
st.sidebar.markdown("**📍 Wilayah:** Jawa Barat & Sekitarnya")
st.sidebar.markdown("**⏰ Jam Buka:** 07.00 - 18.00")
st.sidebar.markdown("""
### 🛒 Info Mitra & Reseller

**BOGOR**
1. Toko Kade 
Jl. Raya Taman Pagelaran No.1, Padasuka, Kec. Ciomas, Kabupaten Bogor 
2. Rumah Talas Jl. Pajajaran No.102, RT.03/RW.12, Bantarjati, Kec. Bogor Utara, Kota Bogor 
3. Damri 
4. Toko Gloria 
Jalan Pandu Raya No.197 Ruko No.4, Bogor Timur, RT.04/RW.15, Tegal Gundil, Kec. Bogor Utara, Kota Bogor 
5. Toko Han-Han 
Pertigaan Pancasan dekat RS Umi 
6. Toko Kue Al 
Jl. Raya Ciomas Kreteg No.41a, Pagelaran, Kec. Ciomas, Kabupaten Bogor 
7. Warung Talas Caringin 
8. Warung Talas Cisarua 
Cisarua, Kabupaten Bogor, Jawa Barat 
9. Kabayan Cake Cipayung 
(seberang Cimory Riverside), Kabupaten Bogor, Jawa Barat 

**BANDUNG**
1. Toko KaDe Ciwastra 
Jl. Ciwastra Kalapa Dua No.189 Ruko No.5 
2. Toko Kanami 
Jl. Raya Bodogol (depan masjid) 
3. Toko Kade Bojongsoang 
Jl. Raya Bojongsoang No.253, Lengkong 
4. Toko Pandan Wangi 
Jl. Gegerkalong Girang No.57, Gegerkalong 
5. Toko Laris Manis 
Jl. Raya Cijerah No.51A, Cijerah, Kec. Bandung 
6. Toko Sangkali 
7. Al' Maksoem 
8. Toko Bagus Cimahi 1 
Jl. Jend. H. Amir Machmud No.476, Cibabat 
9. Toko Bagus Cimahi 2 
10. Toko Bagus Cimindi 
11. Toko Bagus M Toha 
12. Toko Bagus GatSu 
13. Toko Bagus Cikutra 
14. Toko Bagus Cinunuk 
15. Toko Kedai Zian 
Cihampelas, Kabupaten Bandung Barat 
16. Toko PGB 
Jl. Gudang Utara No.29, Merdeka, Bandung 
17. Toko Citra Rasa 
Jl. Tol Padaleunyi, Rest Area Tol Desa No.149, Kec. Bojongsoang, Bandung 
18. Toko G & Z 
Jl. Cipamokolan No.48, Cipamokolan, Kec. Rancasari, Kota Bandung, Jawa Barat 40292 
19. Toko Manis Group 
20. Toko Cinta 
Terusan Buah Batu No.191D 
21. Toko Barokah 
Jl. Raya Cinunuk No.181 
22. Toko Michele 
Jl. Margacinta No.52A, Cijaura, Kec. Buahbatu, Kota Bandung 
23. Toko Laris 
24. Pasmart LP Banceuy 
Sukajadi Kawung Sari, Wargamekar, Kec. Baleendah, Bandung 
25. Aisyah Cake 
Jatinangor, Kabupaten Sumedang, Jawa Barat 
26. Asia Afrika Snack 
Lembang Bandung No.71, Gudangkahuripan, Kec. Lembang 
27. Oleh2 Nusantara Snack Cihampelas 
Jl. Cihampelas No.175, Cipaganti, Kecamatan Coblong, Kota Bandung 
28. Sarimanis 3 Ciwidey 
Jl. Raya Patenggang – Jl. Raya Ciwidey Rancabali No.Km.4, Ciwidey 
29. Rahayu Snack 
30. Sariraos 5 Lembang 
Jl. Raya Lembang No.240, Lembang, Kec. Lembang, Kabupaten Bandung Barat 
31. Odjolali Snack 
Jl. Cihampelas No.131, Cipaganti, Kecamatan Coblong, Kota Bandung 
32. ACR Pusat (Cimahi) 
Jl. Kerkof No.1, Leuwigajah, Cimahi 
33. ACR Mekarwangi 
Jl. Indrayasa No.154B, Cibaduyut 
34. ACR Pajajaran 
Jl. Pajajaran No.85, Arjuna, Cicendo 
35. ACR Cihanjuang 
Jl. Cihanjuang No.104, Cibabat 
36. Nanakam Freshmart 
Jl. L. R.E. Martadinata No.22A, Citarum 
37. Rumah Mode 
Jl. Dr. Setiabudi No.41, Pasteur 
38. RM Cibiuk 
Jl. Soekarno Hatta No.508, Batununggal
""")


# Section 1: Keunggulan
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #ff6b6b; font-size: 2.5rem; margin-bottom: 3rem;'>✨ Mengapa Pilih KaDe?</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class='metric-card'>
        <h2 style='font-size: 4rem;'>🥛</h2>
        <h3 style='color: #ff6b6b;'>Bahan
        Premium</h3>
        <p>Dibuat dengan kualitas premium untuk rasa yang lebih istimewa.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <h2 style='font-size: 4rem;'>🔥</h2>
        <h3 style='color: #feca57;'>Panggang
        Fresh</h3>
        <p>Langsung dari oven panas ke tangan Anda 😋</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <h2 style='font-size: 4rem;'>🚚</h2>
        <h3 style='color: #ff9a9e;'>Pengiriman
        Cepat</h3>
        <p>Packing khusus, Pengiriman cepat, dan Aman.</p>
    </div>
    """, unsafe_allow_html=True)

# Section 2: Produk
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #ff6b6b; font-size: 2.5rem;'>🍰 Produk Unggulan Kami</h2>", unsafe_allow_html=True)

cols = st.columns(2)
for i, (product_name, data) in enumerate(PRODUCTS.items()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='product-card'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>{data['emoji']}</div>
            <h3 style='color: #333; margin-bottom: 1rem;'>{product_name}</h3>
            <div class='price-tag'>Rp {data['price']:,}</div>
            <p style='color: #666; margin: 1.5rem 0;'>{data['desc']}</p>
            <a href='#' onclick='document.getElementById("order-form").scrollIntoView();' style='text-decoration: none;'>
                <button style='background: linear-gradient(45deg, #ff6b6b, #feca57); color: white; border: none; padding: 1rem 2rem; border-radius: 50px; font-weight: 600; width: 100%; cursor: pointer;'>🛒 Pesan Sekarang</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# Section 3: Form Pemesanan
st.markdown("---")
st.markdown("""
<div class='order-section'>
    <h2 style='margin-bottom: 2rem;'>📋 Pesan Sekarang - Mudah & Cepat!</h2>
""", unsafe_allow_html=True)

# Form Pemesanan
with st.form(key="order_form", clear_on_submit=True):

    st.markdown("### 👤 Data Pelanggan")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Nama Lengkap")

    with col2:
        phone = st.text_input("No. WhatsApp")

    st.markdown("### 🛒 Detail Pesanan")

    col1, col2 = st.columns(2)

    with col1:
        selected_product = st.selectbox(
            "Pilih Produk:",
            options=list(PRODUCTS.keys())
        )

    with col2:
        quantity = st.number_input(
            "Jumlah",
            min_value=1,
            max_value=100,
            value=1,
            step=1
        )

    address = st.text_area("Alamat")
    notes = st.text_area("Catatan")
    
    # Total Harga
   selected_product = st.selectbox(
    "Pilih Produk:",
    options=list(PRODUCTS.keys())
)

quantity = st.number_input("Jumlah", min_value=1, max_value=100, value=1, step=1)

total_price = PRODUCTS[selected_product]["price"] * quantity
   st.markdown(f"""
<div style="
    background: white;
    padding: 1.5rem;
    border-radius: 15px;
    margin: 2rem 0;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
">
    <h3 style="
        margin: 0;
        color: #333;
        font-size: 1.5rem;
    ">
        💰 TOTAL PEMBAYARAN
    </h3>

    <h1 style="
        color: #ff6b6b;
        margin-top: 1rem;
        font-size: 3rem;
        font-weight: 700;
    ">
        Rp {total_price:,}
    </h1>
</div>
""", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        submitted = st.form_submit_button("🚀 KIRIM PESANAN VIA WHATSAPP", 
                                        use_container_width=True,
                                        help="Pesanan akan terkirim otomatis ke WA admin")
    
    if submitted and name and phone and address:
        # Generate message
        message = create_whatsapp_message(name, selected_product, quantity, address, notes)
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={message.replace('#', '%23').replace(' ', '%20').replace('\n', '%0A')}"
        
        # Success animation
        st.balloons()
        st.markdown("""
        <div class='success-box'>
            <h2>✅ Pesanan Berhasil!</h2>
            <p>Pesan sudah terkirim ke WhatsApp admin. Silakan buka WA untuk konfirmasi pembayaran.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Big WhatsApp Button
        st.markdown(f"""
        <div style='margin: 2rem 0;'>
            <a href='{whatsapp_url}' target='_blank' class='whatsapp-btn'>
                📱 BUKA WHATSAPP SEKARANG
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        st.info(f"**Link WhatsApp:** [Klik Disini]({whatsapp_url})")
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# Footer
# Footer
# Footer
# Footer
st.markdown("---")

st.markdown("""
<div class='footer'>
    <h2> Terima Kasih telah mempercayai KaDe Pie Susu Lembang </h2>
     <h2> Semoga harimu semakin manis di setiap gigitan ❤️</h2>
</div>
""", unsafe_allow_html=True)
# Hide Streamlit menu & footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
