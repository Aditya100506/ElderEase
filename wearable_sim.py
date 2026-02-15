import requests
import random
import time

URL = "http://127.0.0.1:5000/upload_vitals"

while True:
    vitals = {
        "heart_rate": random.randint(60, 120),
        "bp": f"{random.randint(110,140)}/{random.randint(70,90)}",
        "temperature": round(random.uniform(36.0, 38.5), 1),
        "acceleration": round(random.uniform(0.5, 3.5), 2)
    }

    try:
        response = requests.post(URL, json=vitals)
        print("Sent:", vitals)
        print("Server Response:", response.json())
    except Exception as e:
        print("Server not running yet...")
    
    time.sleep(3)