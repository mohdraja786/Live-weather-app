# 🌤️ Real-Time Dynamic Weather Web App

यह एक एडवांस और रिस्पॉन्सिव वेदर वेब एप्लीकेशन है जिसे **Python (Flask)**, **Requests (API Handling)**, और **JavaScript** की मदद से बनाया गया है। यह ऐप बिना किसी चाबी (API Key) के झंझट के सीधे पब्लिक वेदर सर्वर से दुनिया के किसी भी शहर का बिल्कुल लाइव मौसम खींचकर लाता है।

## 🌐 लाइव प्रोजेक्ट लिंक
आप इस प्रोजेक्ट को इंटरनेट पर यहाँ लाइव चलाकर देख सकते हैं:
👉 **[https://my-live-weather-app.onrender.com](https://my-live-weather-app.onrender.com)** *(यदि आपने रेंडर पर अलग नाम रखा है, तो उसे यहाँ बदल सकते हैं)*

---

## ✨ मुख्य फीचर्स (Key Features)

* **🌍 Global Search:** दुनिया के किसी भी शहर (जैसे: Muzaffarpur, Delhi, London, New Delhi) का नाम डालते ही वहाँ का लाइव मौसम सेकंडों में स्क्रीन पर आ जाता है।
* **🎭 Smart Weather Backgrounds:** इसमें एक स्मार्ट जावास्क्रिप्ट एल्गोरिदम लगा है, जो मौसम का हाल (जैसे: Sunny, Rainy, Cloudy) पढ़कर पूरी वेबसाइट का बैकग्राउंड थीम अपने आप बदल देता है।
* **⚡ Keyless API Integration:** इसे `wttr.in` API से कनेक्ट किया गया है, जो बिना किसी चाबी के ब्लॉक होने के झंझट के हमेशा 100% स्पीड के साथ चलता है।
* **🛡️ Input Validation:** यदि कोई गलत शहर का नाम या स्पेलिंग लिखता है, तो ऐप क्रैश नहीं होता, बल्कि यूजर को एक सुंदर सा अलर्ट मैसेज दिखाता है।

---

## 🛠️ इस्तेमाल की गई तकनीकें (Tech Stack)

* **Backend:** Python, Flask
* **API Engine:** Requests Library (wttr.in JSON API)
* **Frontend UI:** HTML5, CSS3, Bootstrap 5 (Glassmorphism Glass Card UI)
* **Logic:** Vanilla JavaScript (Dynamic UI Theme Swapping)
* **Deployment:** GitHub, Render Cloud

---

## 💻 अपने कंप्यूटर पर सेटअप कैसे करें? (Local Installation)

1. प्रोजेक्ट फोल्डर में टर्मिनल खोलें।
2. जरूरी लाइब्रेरी इंस्टॉल करें:
   ```bash
   pip install flask requests gunicorn