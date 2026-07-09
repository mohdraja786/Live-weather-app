from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        
        if city:
            # बिना किसी API Key के सीधे चलने वाला सुपर यूआरएल (wttr.in)
            # ?format=j1 लिखने से यह हमें पूरा डेटा JSON फॉर्मेट में देता है
            url = f"https://wttr.in/{city}?format=j1"
            
            try:
                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # इस API से तापमान, मौसम का हाल और नमी निकालना
                    current_condition = data['current_condition'][0]
                    area_name = data['nearest_area'][0]['areaName'][0]['value']
                    
                    weather_data = {
                        'city': area_name, # शहर का नाम
                        'temp': f"{current_condition['temp_C']}°C", # सेल्सियस में तापमान
                        'desc': current_condition['weatherDesc'][0]['value'], # मौसम का हाल
                        'humidity': f"{current_condition['humidity']}%" # नमी
                    }
                else:
                    error_message = "शहर नहीं मिला! कृपया अंग्रेजी में सही स्पेलिंग लिखें (e.g. Muzaffarpur, Delhi)।"
                    
            except Exception as e:
                error_message = "मौसम का डेटा लाने में थोड़ी दिक्कत हुई। कृपया दोबारा कोशिश करें।"

    return render_template('index.html', weather=weather_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)