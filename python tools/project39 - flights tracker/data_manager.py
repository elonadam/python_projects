import requests

sheety_url = "https://api.sheety.co/84d665c812a62c08c15ad2c0f81a0f65/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.dest_data = {}

    def get_dest_data(self):
        response = requests.get(url=sheety_url)
        data = response.json()
        self.dest_data = data['prices']
        return self.dest_data

    def store_iata_codes(self, city_id, iata_code):
        for city in self.dest_data:
            body = {
                'price': {
                    "iataCode": iata_code  # key needs to be camelCase although google sheet column is not
                }
            }
            response = requests.put(url=sheety_url + f"/{city_id}", json=body)
            response.raise_for_status()
            print(response.text)
