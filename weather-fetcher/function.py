import requests

def get_weather_info(city):
    API_KEY = "APPI_KEY"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(requests_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] - 273.15, 2)
        result = f"Pogoda: {weather}\nTemperatura: {temperature}°C"
        print(result)  # Dodano dla debugowania
        return result
    else:
        error_message = "Błąd: Nie można znaleźć miasta"
        print(error_message)  # Dodano dla debugowania
        return error_message
