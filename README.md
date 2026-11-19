# Basic Weather App

A beginner-friendly command-line weather application built with Python and the OpenWeatherMap Current Weather API.

## Features

- Search by city name or ZIP/postal code
- Current temperature in Celsius and Fahrenheit
- Humidity, weather description, and wind speed
- Handles invalid locations, invalid API keys, timeouts, and connection errors
- Rejects empty input and supports repeated searches

## Requirements

- Python 3.8 or newer
- An internet connection
- A free OpenWeatherMap API key

## Setup

1. Open a terminal in this project folder.
2. (Optional but recommended) Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Get an API key from https://openweathermap.org/api.
5. Copy `.env.example` to a new file named `.env` and replace the placeholder:

   ```env
   API_KEY=your_actual_api_key_here
   ```

   Keep `.env` private. It is excluded from Git by `.gitignore`.

6. Run the application:

   ```bash
   python weather_app.py
   ```

## Usage

Enter a city name such as `Hyderabad` or `London`. To search by postal code, include the country code, for example `500001,IN`. Type `exit` to quit.

## Notes

- Temperature is requested in metric units, so the API returns Celsius and wind speed in metres per second.
- Fahrenheit is calculated from Celsius.
- A newly created OpenWeatherMap API key may take some time to become active.
- API availability and limits are controlled by OpenWeatherMap.

## Project structure

```text
Basic-Weather-App/
├── weather_app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
