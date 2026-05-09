<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KaDe Pie Susu Bandung - Kelezatan Asli Bandung</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            color: #333;
            overflow-x: hidden;
        }

        /* Header & Navigation */
        header {
            position: fixed;
            top: 0;
            width: 100%;
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 5%;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: white;
            text-decoration: none;
        }

        .logo span {
            color: #fff;
            background: linear-gradient(45deg, #ff9a9e, #fecfef);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .nav-links a:hover {
            color: #ffed4a;
            transform: translateY(-2px);
        }

        .order-btn {
            background: #fff;
            color: #ff6b6b;
            padding: 0.8rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .order-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            background: linear-gradient(rgba(255,107,107,0.9), rgba(254,202,87,0.8)),
                        url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><radialGradient id="a" cx="50%" cy="50%"><stop offset="0%" stop-color="%23ff9a9e"/><stop offset="100%" stop-color="%23fecfef"/></radialGradient></defs><rect width="1200" height="800" fill="url(%23a)"/><circle cx="200" cy="200" r="100" fill="%23fff" opacity="0.3"/><circle cx="1000" cy="600" r="150" fill="%23ffed4a" opacity="0.2"/></svg>');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="3" fill="%23fff" opacity="0.5"/><circle cx="80" cy="80" r="2" fill="%23fff" opacity="0.3"/><circle cx="50" cy="40" r="1.5" fill="%23fff" opacity="0.4"/></svg>') repeat;
            animation: float 20s infinite linear;
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            100% { transform: translateY(-100px); }
        }

        .hero-content h1 {
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 1rem;
            animation: slideInUp 1s ease;
        }

        .hero-content p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            animation: slideInUp 1s ease 0.2s both;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            animation: slideInUp 1s ease 0.4s both;
        }

        .cta-btn {
            padding: 1rem 2.5rem;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .cta-primary {
            background: #fff;
            color: #ff6b6b;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }

        .cta-secondary {
            background: transparent;
            color: #fff;
            border: 2px solid #fff;
        }

        .cta-btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(0,0,0,0.3);
        }

        /* Sections */
        section {
            padding: 100px 5%;
            max-width: 1200px;
            margin: 0 auto;
        }

        h2 {
            font-size: 3rem;
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* About Section */
        .about {
            background: #f8f9fa;
            text-align: center;
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .about-text h3 {
            font-size: 2rem;
            color: #ff6b6b;
            margin-bottom: 1rem;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .feature {
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .feature:hover {
            transform: translateY(-10px);
        }

        .feature i {
            font-size: 3rem;
            color: #ff6b6b;
            margin-bottom: 1rem;
        }

        /* Products Section */
        .products {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .product-card {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1);
            transition: all 0.4s ease;
            position: relative;
        }

        .product-card:hover {
            transform: translateY(-15px) scale(1.02);
        }

        .product-image {
            height: 250px;
            background: linear-gradient(45deg, #ff9a9e, #fecfef);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 6rem;
            color: white;
        }

        .product-info {
            padding: 2rem;
            text-align: center;
        }

        .product-info h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #333;
        }

        .price {
            font-size: 2rem;
            font-weight: 700;
            color: #ff6b6b;
            margin: 1rem 0;
        }

        /* Order Section */
        .order-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
        }

        .order-form {
            max-width: 600px;
            margin: 0 auto;
            background: rgba(255,255,255,0.1);
            padding: 3rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
        }

        .form-group {
            margin-bottom: 1.5rem;
            text-align: left;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 1rem;
            border: none;
            border-radius: 10px;
            font-size: 1rem;
            background: rgba(255,255,255,0.9);
        }

        .submit-btn {
            width: 100%;
            padding: 1.2rem;
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        /* WhatsApp Button */
        .whatsapp-float {
            position: fixed;
            width: 60px;
            height: 60px;
            bottom: 40px;
            right: 40px;
            background: linear-gradient(45deg, #25D366, #128C7E);
            color: #FFF;
            border-radius: 50px;
            text-align: center;
            font-size: 30px;
            box-shadow: 2px 2px 3px #999;
            z-index: 100;
            animation: bounce 2s infinite;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }

        /* Footer */
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 3rem 5%;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero-content h1 {
                font-size: 2.5rem;
            }

            .about-content {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .cta-buttons {
                flex-direction: column;
                align-items: center;
            }
        }

        /* Animations */
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <nav>
            <a href="#" class="logo">Ka<span>De</span> Pie Susu</a>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">Tentang</a></li>
                <li><a href="#products">Produk</a></li>
                <li><a href="#order">Pesan</a></li>
            </ul>
            <a href="#order" class="order-btn">Pesan Sekarang</a>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <h1>KaDe Pie Susu Bandung</h1>
            <p>Kelezatan Asli Bandung dalam Setiap Gigitan</p>
            <div class="cta-buttons">
                <a href="#products" class="cta-btn cta-primary">Lihat Produk</a>
                <a href="#order" class="cta-btn cta-secondary">Pesan Sekarang</a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <h2>Mengapa KaDe Pie Susu?</h2>
        <div class="about-content">
            <div class="about-text">
                <h3>Resep Rahasia Keluarga Bandung</h3>
                <p>Dibuat dengan cinta dan resep turun-temurun dari Bandung. Setiap pie susu kami dipanggang fresh setiap hari dengan bahan-bahan premium pilihan.</p>
            </div>
            <div>
                <div class="features">
                    <div class="feature">
                        <i class="fas fa-seedling"></i>
                        <h4>Bahan Premium</h4>
                        <p>Susu segar, telur kampung, tepung terigu terbaik</p>
                    </div>
                    <div class="feature">
                        <i class="fas fa-fire"></i>
                        <h4>Panggang Fresh</h4>
                        <p>Setiap hari, langsung dari oven ke tangan Anda</p>
                    </div>
                    <div class="feature">
                        <i class="fas fa-shipping-fast"></i>
                        <h4>Pengiriman Cepat</h4>
                        <p>Bandung & sekitarnya, aman dan dingin sampai</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Products Section -->
    <section id="products" class="products">
        <h2>Produk Unggulan</h2>
        <div class="product-grid">
            <div class="product-card">
                <div class="product-image">
                    <i class="fas fa-cheese"></i>
                </div>
                <div class="product-info">
                    <h3>Classic Pie Susu</h3>
                    <div class="price">Rp 25.000</div>
                    <p>Pie susu original dengan rasa susu kental manis yang khas Bandung</p>
                    <button class="order-btn" onclick="orderNow('Classic Pie Susu')">Pesan</button>
                </div>
            </div>
            <div class="product-card">
                <div class="product-image">
                    <i class="fas fa-lemon"></i>
                </div>
                <div class="product-info">
                    <h3>Lemon Pie Susu</h3>
                    <div class="price">Rp 28.000</div>
                    <p>Sensasi segar lemon yang memikat dengan tekstur lembut</p>
                    <button class="order-btn" onclick="orderNow('Lemon Pie Susu')">Pesan</button>
                </div>
            </div>
            <div class="product-card">
                <div class="product-image">
                    <i class="fas fa-strawberry"></i>
                </div>
                <div class="product-info">
                    <h3>Strawberry Pie Susu</h3>
                    <div class="price">Rp 30.000</div>
                    <p>Perpaduan sempurna stroberi segar dan susu creamy</p>
                    <button class="order-btn" onclick="orderNow('Strawberry Pie Susu')">Pesan</button>
                </div>
            </div>
            <div class="product-card">
                <div class="product-image">
                    <i class="fas fa-crown"></i>
                </div>
                <div class="product-info">
                    <h3>Premium Box (6 pcs)</h3>
                    <div class="price">Rp 150.000</div>
                    <p>Paket spesial mix rasa, cocok untuk hadiah atau acara spesial</p>
                    <button class="order-btn" onclick="orderNow('Premium Box')">Pesan</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Order Section -->
    <section id="order" class="order-section">
        <h2>Pesan Sekarang</h2>
        <form class="order-form" onsubmit="submitOrder(event)">
            <div class="form-group">
                <label>Nama Lengkap</label>
                <input type="text" id="name" required>
            </div>
            <div class="form-group">
                <label>Nomor WhatsApp</label>
                <input type="tel" id="phone" required>
            </div>
            <div class="form-group">
                <label>Produk yang dipesan</label>
                <select id="product" required>
                    <option value="">Pilih Produk</option>
                    <option value="Classic Pie Susu - Rp25.000">Classic Pie Susu - Rp25.000</option>
                    <option value="Lemon Pie Susu - Rp28.000">Lemon Pie Susu - Rp28.000</option>
                    <option value="Strawberry Pie Susu - Rp30.000">Strawberry Pie Susu - Rp30.000</option>
                    <option value="Premium Box (6pcs) - Rp150.000">Premium Box (6pcs) - Rp150.000</option>
                </select>
            </div>
            <div class="form-group">
                <label>Jumlah</label>
                <input type="number" id="quantity" min="1" value="1" required>
            </div>
            <div class="form-group">
                <label>Alamat Pengiriman</label>
                <textarea rows="3" id="address" required></textarea>
            </div>
            <button type="submit" class="submit-btn">
                <i class="fab fa-whatsapp"></i> Kirim Pesanan via WhatsApp
            </button>
        </form>
    </section>

    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/6281234567890?text=Saya%20ingin%20pesan%20KaDe%20Pie%20Susu%20Bandung!" 
       class="whatsapp-float" target="_blank">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 KaDe Pie Susu Bandung. Dibuat dengan <i class="fas fa-heart" style="color: #ff6b6b;"></i> dari Bandung.</p>
        <p>Pesan sekarang: <i class="fab fa-whatsapp"></i> 0812-3456-7890</p>
    </footer>

    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Order now function
        function orderNow(product) {
            document.getElementById('product').value = product;
            document.getElementById('order').scrollIntoView({ behavior: 'smooth' });
        }

        // Submit order form
        function submitOrder(event) {
            event.preventDefault();
            
            const name = document.getElementById('name').value;
            const phone = document.getElementById('phone').value;
            const product = document.getElementById('product').value;
            const quantity = document.getElementById('quantity').value;
            const address = document.getElementById('address').value;

            const message = `Halo KaDe Pie Susu!%0A%0ASaya ingin pesan:%0A- Nama: ${name}%0A- Produk: ${product}%0A- Jumlah: ${quantity}%0A- Alamat: ${address}%0A%0ATerima kasih! 😊`;

            const whatsappURL = `https://wa.me/6281234567890?text=${message}`;
            window.open(whatsappURL, '_blank');
            
            // Reset form
            event.target.reset();
        }

        // Navbar scroll effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('header');
            if (window.scrollY > 100) {
                header.style.background = 'rgba(255, 107, 107, 0.95)';
                header.style.backdropFilter = 'blur(10px)';
            } else {
                header.style.background = 'linear-gradient(135deg, #ff6b6b, #feca57)';
                header.style.backdropFilter = 'none';
            }
        });
    </script>
</body>
</html>
