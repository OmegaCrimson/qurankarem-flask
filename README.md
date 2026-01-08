# 📖 القرآن الكريم بصوت الشيخ بدر التركي (تطبيق Flask)

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-green.svg)
![Waitress](https://img.shields.io/badge/waitress-3.0-orange.svg)
![Bootstrap](https://img.shields.io/badge/bootstrap-5.3-purple.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

تطبيق ويب بسيط وأنيق باستخدام **Flask** يعرض جميع سور القرآن الكريم (١١٤ سورة) مع بيانات وصفية وتشغيل صوتي لتلاوة الشيخ **بدر التركي**.  
تم بناؤه باستخدام **Flask + Waitress** للتشغيل، مع تصميم احترافي باستخدام **Bootstrap** وخط عربي Amiri.

---

## ✨ المميزات
- 📚 قائمة كاملة بـ **١١٤ سورة** مع الاسم، عدد الآيات، النوع (مكية / مدنية)، الأسماء الأخرى، والموضوعات.
- 🎵 مشغل صوت مدمج لكل سورة (ملفات MP3 من موقع mp3quran.net).
- 🌐 واجهة مستخدم احترافية باستخدام Bootstrap وخط Amiri العربي.
- 🖥️ يفتح تلقائياً في المتصفح عند تشغيله محلياً.
- ⚡ يعمل بخادم Waitress الجاهز للإنتاج.

---

## 📂 هيكل المشروع
```
qurankarem-flask/
│
├── app.py                # التطبيق الرئيسي
├── models/
│   └── data.json         # بيانات السور وروابط الصوت
├── templates/
│   ├── index.html        # الصفحة الرئيسية (قائمة السور)
│   └── surah.html        # صفحة تفاصيل السورة
├── static/               # ملفات CSS/JS/صور إضافية
└── README.md             # ملف التوثيق
```

---

## 🚀 طريقة التشغيل

### ١. استنساخ المستودع
```bash
git clone https://github.com/OmegaCrimson/qurankarem-flask.git
cd qurankarem-flask
```

### ٢. إنشاء بيئة افتراضية (مستحسن)
```bash
python -m venv venv
source venv/bin/activate   # على Linux/Mac
venv\Scripts\activate      # على Windows
```

### ٣. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

### ٤. تشغيل التطبيق
```bash
python app.py
```

سيفتح التطبيق تلقائياً في المتصفح على:
```
http://127.0.0.1:8080/
```

---

## 📸 لقطات شاشة
- **الصفحة الرئيسية**: قائمة السور مع عدد الآيات.  
![Homepage Screenshot](screenshots/main.png)

- **صفحة السورة**: بيانات وصفية + مشغل صوت.  
![Surah Screenshot](screenshots/3.png)

---

## 🛠️ التقنيات المستخدمة
- **الخلفية**: Flask, Waitress  
- **الواجهة**: Bootstrap 5, خط Amiri  
- **البيانات**: JSON (بيانات السور وروابط الصوت)

---

## 📜 الرخصة
هذا المشروع مفتوح المصدر تحت رخصة **MIT**.  
يمكنك استخدامه، تعديله، ومشاركته بحرية.

---

## 🙏 الشكر
- التلاوات الصوتية من [mp3quran.net](https://mp3quran.net).  
- الخطوط من [Google Fonts](https://fonts.google.com/specimen/Amiri).  
- إطار Bootstrap للتصميم.

---

# 📖 Quran Kareem with Sheikh Badr Al-Turki (Flask App)

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-green.svg)
![Waitress](https://img.shields.io/badge/waitress-3.0-orange.svg)
![Bootstrap](https://img.shields.io/badge/bootstrap-5.3-purple.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A simple and elegant **Flask web application** that displays all 114 surahs of the Holy Qur’an with metadata and audio recitation by **Sheikh Badr Al-Turki**.  
Built with **Flask + Waitress** for serving, and styled using **Bootstrap** with Arabic typography.

---

## ✨ Features
- 📚 Full list of **114 surahs** with names, ayah counts, type (Meccan / Medinan), other names, and topics.
- 🎵 Integrated **audio player** for each surah (MP3 from mp3quran.net).
- 🌐 Professional **Bootstrap UI** with Amiri Arabic font.
- 🖥️ Auto-opens in your browser when you run the app locally.
- ⚡ Powered by **Waitress** for production-ready serving.

---

## 📂 Project Structure
```
qurankarem-flask/
│
├── app.py                # Main Flask application
├── models/
│   └── data.json         # Surah metadata + audio links
├── templates/
│   ├── index.html        # Homepage listing all surahs
│   └── surah.html        # Surah detail page
├── static/               # Optional CSS/JS/images
└── README.md             # Project documentation
```

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/OmegaCrimson/qurankarem-flask.git
cd qurankarem-flask
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

The app will automatically open in your browser at:
```
http://127.0.0.1:8080/
```

---

## 📸 Screenshots
- **Homepage**: List of surahs with ayah counts.  
![Homepage Screenshot](screenshots/main.png)

- **Surah Page**: Metadata + audio player.  
![Surah Screenshot](screenshots/3.png)

---

## 🛠️ Tech Stack
- **Backend**: Flask, Waitress  
- **Frontend**: Bootstrap 5, Amiri font  
- **Data**: JSON (surah metadata + audio links)

---

## 📜 License
This project is open-source under the **MIT License**.  
Feel free to use, modify, and share.

---

## 🙏 Acknowledgements
- Audio recitations from [mp3quran.net](https://mp3quran.net).  
- Fonts from [Google Fonts](https://fonts.google.com/specimen/Amiri).  
- Bootstrap framework for styling.
