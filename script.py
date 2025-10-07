# สร้างไฟล์ HTML สำหรับหน้า Home อย่างเดียว พร้อมพื้นหลังขยับได้
html_home = '''<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Home - Alex Script Writer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style>
        /* รีเซ็ตและตั้งค่าสไตล์พื้นฐาน */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body, html {
            height: 100%;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
            background: #1a0000;
            color: white;
        }

        /* พื้นหลังขยับแบบไดนามิก */
        #background {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
            background: radial-gradient(circle, #ff4444 0%, #330000 70%);
            animation: bgMove 20s linear infinite alternate;
        }

        @keyframes bgMove {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        /* เนื้อหาโฮม */
        .hero {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            padding: 80px 10%;
            height: 100vh;
        }

        .hero-content {
            max-width: 600px;
        }

        .hero-content h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .highlight {
            color: #ff4444;
            font-weight: bold;
        }

        .subtitle {
            color: #ff4444;
            font-size: 20px;
            margin-bottom: 20px;
        }

        .hero-content p {
            color: #ccc;
            font-size: 16px;
            line-height: 1.8;
            margin-bottom: 30px;
        }

        .social-icons {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
        }

        .social-icons a {
            width: 45px;
            height: 45px;
            border: 2px solid white;
            border-radius: 50%;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            text-decoration: none;
            transition: background-color 0.3s, color 0.3s;
        }

        .social-icons a:hover {
            background-color: #ff4444;
            border-color: #ff4444;
            color: white;
        }

        .btn {
            display: inline-block;
            padding: 12px 40px;
            color: white;
            text-decoration: none;
            border: 2px solid white;
            border-radius: 25px;
            transition: background-color 0.3s, border-color 0.3s;
            cursor: pointer;
        }

        .btn:hover {
            background-color: #ff4444;
            border-color: #ff4444;
        }

        .hero-image {
            width: 400px;
            position: relative;
        }

        .red-circle {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: radial-gradient(circle, #ff4444 0%, #cc0000 100%);
            opacity: 0.9;
            top: 0;
            left: 0;
            z-index: 1;
        }

        svg.profile-img {
            position: relative;
            width: 100%;
            height: auto;
            z-index: 2;
            display: block;
            margin-top: 80px;
            filter: drop-shadow(2px 5px 6px rgba(0,0,0,0.9));
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero {
                flex-direction: column-reverse;
                text-align: center;
                padding: 60px 5%;
                height: auto;
            }
            .hero-image {
                width: 300px;
                margin-bottom: 30px;
            }
        }
    </style>
</head>
<body>
    <div id="background"></div>
    <section class="hero">
        <div class="hero-content">
            <h1>Hi, It's <span class="highlight">Alex</span></h1>
            <p class="subtitle">I'm a Script Writer</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Quisque euismod, justo et dapibus pulvinar, nunc tellus rhoncus leo, in dapibus nulla orci eu orci.</p>
            <div class="social-icons">
                <a href="#"><i class="fab fa-facebook-f"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-linkedin-in"></i></a>
            </div>
            <a href="#" class="btn">Hire me</a>
        </div>
        <div class="hero-image">
            <div class="red-circle"></div>
            <svg class="profile-img" viewBox="0 0 200 300" style="fill: #000;">
                <ellipse cx="100" cy="250" rx="80" ry="50" fill="#1a0000"/>
                <rect x="60" y="120" width="80" height="150" rx="40" fill="#222"/>
                <circle cx="100" cy="80" r="50" fill="#333"/>
            </svg>
        </div>
    </section>
</body>
</html>'''

# save to file
with open('home_only.html', 'w', encoding='utf-8') as f:
    f.write(html_home)

print("✅ สร้างไฟล์ home_only.html พร้อมพื้นหลังขยับเรียบร้อยแล้ว")
print("\nวิธีใช้งาน:")
print("1. ดับเบิลคลิกเปิด home_only.html ในเว็บเบราว์เซอร์")
print("2. แก้ไขข้อความและรูปภาพตามต้องการ")