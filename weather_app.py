import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(location):
    """Fetch and display current weather for a city or ZIP code."""
    if not API_KEY or API_KEY == "your_actual_api_key_here":
        print("\nError: API key not configured.")
        print("Add your OpenWeatherMap key to the .env file.")
        return

    # A ZIP code should include its country code, e.g. 500001,IN.
    if "," in location and location.split(",", 1)[0].strip().isdigit():
        params = {"zip": location, "appid": API_KEY, "units": "metric"}
    elif location.isdigit():
        print("\nTip: For ZIP codes, include the country code, e.g. 500001,IN.")
        params = {"zip": location, "appid": API_KEY, "units": "metric"}
    else:
        params = {"q": location, "appid": API_KEY, "units": "metric"}

    try:
        print("\nFetching weather information...")
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 404:
            print("\nError: City or ZIP code not found.")
            return
        if response.status_code == 401:
            print("\nError: Invalid API key. Check your OpenWeatherMap key.")
            return
        if response.status_code == 429:
            print("\nError: API request limit exceeded. Try again later.")
            return

        response.raise_for_status()
        data = response.json()

        city = data["name"]
        country = data["sys"]["country"]
        temperature_c = data["main"]["temp"]
        temperature_f = temperature_c * 9 / 5 + 32
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data.get("wind", {}).get("speed", 0)

        print("\n" + "=" * 42)
        print("             WEATHER REPORT")
        print("=" * 42)
        print(f"Location       : {city}, {country}")
        print(f"Temperature    : {temperature_c:.1f} °C")
        print(f"Temperature    : {temperature_f:.1f} °F")
        print(f"Weather        : {description.title()}")
        print(f"Humidity       : {humidity}%")
        print(f"Wind Speed     : {wind_speed} m/s")
        print("=" * 42)

    except requests.exceptions.Timeout:
        print("\nError: Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect. Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"\nHTTP error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"\nNetwork error: {error}")
    except (KeyError, IndexError, ValueError):
        print("\nError: The weather service returned unexpected data.")


def main():
    print("=" * 42)
    print("          BASIC WEATHER APPLICATION")
    print("=" * 42)

    while True:
        location = input(
            "\nEnter city name or ZIP code (or 'exit' to quit): "
        ).strip()

        if location.lower() == "exit":
            print("\nThank you for using the Weather App!")
            break

        if not location:
            print("\nError: City name or ZIP code cannot be empty.")
            continue

        get_weather(location)


if __name__ == "__main__":
    main()
