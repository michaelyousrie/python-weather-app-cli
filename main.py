import os
import json
import datetime
import requests
from dotenv import load_dotenv

def main(city):
    def save_to_file(city, data, file_path='results'):
        city = city.lower()
        file_path = f"{file_path}/{city}.json"

        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Load Existing Data or create a new list if the file does not exist
        all_data = []

        if os.path.exists(file_path):  # Check if the file exists
            try:
                with open(file_path, 'r') as file:
                    current_data = json.load(file)
                    all_data.extend(current_data)  # Add existing data to all_data
            except json.JSONDecodeError:
                # Handle the case where the file is empty or corrupted
                print(f"Warning: {file_path} is empty or corrupted, starting fresh.")
            #endtry
        #endif

        # Append new data
        all_data.append(data)

        # Save to file
        try:
            with open(file_path, 'w') as file:
                json.dump(all_data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")
            return False
        #endtry

        return True
    #enddef save_to_file

    # Load .env file
    load_dotenv()

    # Your OpenWeatherMap API key (replace with your own)
    API_KEY = os.getenv('WEATHER_API_KEY')
    # Base URL for OpenWeatherMap API
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    # Complete URL
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract main weather details
        main = data['main']
        weather = data['weather'][0]

        # Get temperature and weather description
        temperature = main['temp']
        description = weather['description']

        # Print the weather data
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description}")

        weather_data = {
            "Time"          : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Temperature"   : f"{temperature}°C",
            "Condition"     : f"{description}"
        }

        save_to_file(city, weather_data)
    else:
        # If city not found or any error
        print(f"What the heck is {city} ?!")
    #endif
#enddef

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    main(city)
#endif
