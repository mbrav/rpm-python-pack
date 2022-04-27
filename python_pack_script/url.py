from httpx import Client


def get_weather(lat: float = 52.52, lon: float = 13.41):

    params = {
        'latitude': str(lat),
        'longitude': str(lon),
        'hourly': 'temperature_2m'
    }

    url = 'https://api.open-meteo.com/v1/forecast'
    with Client() as client:
        response = client.get(url, params=params)

    return response.json()
