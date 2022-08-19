from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager 
from notification_manager import NotificationManager

Noti = NotificationManager()

cityFrom = "SGN"
cityTo = input("Where you want to go to? ")

flight_info = FlightData()
parameters = flight_info.flight_info(cityFrom, cityTo)

sheet = DataManager()
sheet_data = sheet.get_data()

flight_price_data = FlightSearch()
flight_price = flight_price_data.get_price(parameters)

for data in sheet_data:
    if cityTo == data["iataCode"]:
        if min(flight_price) < data["lowerPrice"]:
            sheet_data = sheet.update_price(cityTo, min(flight_price))
            message_to = Noti.message_body(data["city"], min(flight_price))