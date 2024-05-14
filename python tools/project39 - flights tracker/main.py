# searching for low-cost flights, based on flight budget from a google sheet connected as API
# when a low price flight found, sending me SMS with the details

from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_dest_data()  # get data from sheet
notification_manager = NotificationManager()

origin_city_iata = 'TLV'

tomorrow = (datetime.today() + timedelta(1)).strftime('%d/%m/%Y')
six_month_from_now = (datetime.today() + timedelta(180)).strftime('%d/%m/%Y')

if sheet_data[0]['iataCode'] == '' : # no iata code in sheet
    for city in sheet_data:
        iata_code = flight_search.search_iata(city['city'])  # get iata codes
        city['iataCode'] = iata_code  # set a new iata codes
        index = sheet_data.index(city) + 2
        data_manager.store_iata_codes()

for destination in sheet_data: # search flights for each destination
    flight = flight_search.search_flight(
        origin_city_iata,
        dest_city_iata=destination['iataCode'],
        from_date=tomorrow,to_date=six_month_from_now
    )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to"
                    f" {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to"
                    f" {flight.return_date}.\n click here to purchase {flight.deep_link}"
        )
