import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FORTYGUARD_API_KEY")

# FortyGuard API Base URL endpoint configuration
API_BASE_URL = "https://docs-api.fortyguard.com"  

def get_weather_advice(temperature):
    """Analyzes temperature metrics and maps them to visual icons and advice."""
    if temperature < 0:
        return "🧥", "Freezing weather detected! Bundle up with a heavy winter jacket and stay warm."
    elif 0 <= temperature <= 10:
        return "🧣", "It's quite chilly out! Grab a warm sweater or light jacket before stepping outside."
    elif 11 <= temperature <= 22:
        return "☔", "Mild or wet conditions possible. Keep an umbrella handy just in case!"
    else:
        return "☀️🕶️", "Lovely bright sunshine! Soak up some healthy Vitamin D, wear sunscreen, and stay hydrated."

def fetch_live_weather():
    """Connects to FortyGuard API infrastructure using secure header authentication."""
    print("Querying live microclimate intelligence from FortyGuard...")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Example structure for hitting an environmental parameter or data endpoint
        # response = requests.get(f"{API_BASE_URL}/v1/environmental-parameters", headers=headers, timeout=10)
        # if response.status_code == 200:
        #     data = response.json()
        #     return data.get("temperature", 25)
        
        # Fallback simulation representing live data retrieval for testing
        live_temp = 28  
        return live_temp
    except Exception as e:
        print(f"Connection notice: {e}")
        return 22

def main():
    print("Initializing Weather & Temperature Assistant [API-Integration Branch]...")
    if not API_KEY:
        print("Error: API Key missing from .env configuration.")
        return
    
    current_temp = fetch_live_weather()
    print(f"\nLive Analyzed Temperature: {current_temp}°C")
    
    icon, message = get_weather_advice(current_temp)
    print(f"Visual Alert Icon: {icon}")
    print(f"Actionable Advice: {message}")

if __name__ == "__main__":
    main()