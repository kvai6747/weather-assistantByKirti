import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FORTYGUARD_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def get_lifestyle_advice(temperature, condition="normal"):
    """Analyzes temperature and conditions to serve smart seasonal and weather alerts."""
    
    # Deep freeze / Outdoor sports & Winter prep
    if temperature <= -2:
        return "⛸️ ❄️", "Deep freeze alert! Perfect time for outdoor ice skating, but ensure your winter tires are installed and heavy blankets are out!"
    
    # Chilly weather / Jackets & Blankets
    elif -1 <= temperature <= 8:
        return "🧣 🧥", "Chilly weather ahead! Time to unpack cozy blankets, put on a warm jacket, and check if it's time to swap car tires."
    
    # Wet / Rainy conditions
    elif 9 <= temperature <= 20 and condition.lower() in ["rain", "wet", "showers"]:
        return "☔", "Rainy skies detected! Keep your umbrella handy and waterproof gear ready."
    
    # Warm / Sunny weather
    else:
        return "☀️ 🕶️", "Splendid sunny weather! Soak up some healthy Vitamin D, wear your sunglasses, and enjoy the day outside."

def main():
    print("Initializing your Seasonal Weather & Lifestyle Assistant...")
    if not API_KEY:
        print("Error: API Key not found! Check your .env configuration.")
        return
    
    print("API Key loaded successfully from safety!")
    
    # Simulated live check (this is where we will map real FortyGuard API response fields next)
    current_temp = 4
    current_condition = "clear"
    
    print(f"\nFetching live microclimate data...")
    icon, advice = get_lifestyle_advice(current_temp, current_condition)
    
    print(f"Current Status -> Temp: {current_temp}°C | Condition: {current_condition}")
    print(f"Visual Alerts: {icon}")
    print(f"Lifestyle Advice: {advice}")

if __name__ == "__main__":
    main()