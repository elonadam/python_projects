from flight_data import FlightData
import requests
import os
# api documentation https://tequila.kiwi.com/portal/docs/tequila_api/search_api

kiwi_iati_url = 'https://api.tequila.kiwi.com/locations/query?'
kiwi_flight_search_url = 'https://api.tequila.kiwi.com/v2/search?'

header = {  # kiwi flights api key
    "apikey": os.environ.get('KIWIKEY')
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_data = {}

    def search_iata(self, city_name):
        parameters = {
            "term": f'{city_name}',
            'location_type': 'city',
        }
        response = requests.get(url=kiwi_iati_url, params=parameters, headers=header)
        response.raise_for_status()
        data = response.json()
        iata_code = (data['locations'][0]['code'])
        return iata_code

    def search_flight(self, origin_city, dest_city_iata, from_date, to_date):
        parameters = {
            'fly_from': origin_city,
            'fly_to': dest_city_iata,
            'date_from': from_date,
            'data_to': to_date,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'adults': 2,
            #"one_for_city": 1,
            "max_stopovers": 0,
            'curr': 'USD',

        }
        response = requests.get(url=kiwi_flight_search_url, params=parameters, headers=header)
        try:
            data = response.json()["data"][0]
            # print(data)
        except IndexError:
            print(f"No flight found for {dest_city_iata}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            deep_link=data["deep_link"],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
