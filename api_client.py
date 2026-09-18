import requests

from config import API_KEY
def get_flights(dep_iata=None, arr_iata=None, flight_status=None):
    url = "https://api.aviationstack.com/v1/flights"
    params = {"access_key": API_KEY}

    if dep_iata:
        params["dep_iata"] = dep_iata
    if arr_iata:
        params["arr_iata"] = arr_iata
    if flight_status:
        params["flight_status"] = flight_status

    response = requests.get(url, params=params)
    return response.json()