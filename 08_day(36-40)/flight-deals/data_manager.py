from requests.auth import HTTPBasicAuth
import requests

basic = HTTPBasicAuth('Thane75834', 'bausdb2133')

header = {
    "Authorization": "Basic VGhhbmU3NTgzNDpiYXVzZGIyMTMz",
}

gg_sheet_url = "https://api.sheety.co/5187d5e2d94173524a084b3d76bb6cc9/flightDeals20/prices"

class DataManager:
    def __init__(self):
        self.flight_data = {}

    def get_data(self):
        response = requests.get(url=gg_sheet_url, auth=basic, headers=header)
        response.raise_for_status()
        data = response.json()
        self.flight_data = data["prices"]
        return self.flight_data

    def update_price(self, code, new_price):
        self.get_data()
        for iataCode in self.flight_data:
            if iataCode == code:
                id = self.flight_data["id"]
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(
            url=f"{gg_sheet_url}/{id}", auth=basic, headers=header,
            json=new_data
        )
        print(response.text)

    # def update_iata(self, iataCode):
    #     self.get_data
    #     for city in self.flight_data:
    #         new_data = {
    #             "price": {
    #                 "iataCode": iataCode,
    #             }
    #         }
    #         response = requests.put(
    #             url=f"{gg_sheet_url}/{city['id']}", auth=basic, headers=header,
    #             json=new_data
    #         )
    #         print(response.text)