import requests

flight_search_url = "http://tequila-api.kiwi.com/v2/search"
get_iata_url = "https://tequila-api.kiwi.com/locations/query"
api_key = "yc-i-0Ptd7MnaNbJZINu02PykKVVXQbY"

header = {
    "apikey": api_key
}

class FlightSearch:
    def __init__(self):
        self.price = []
        self.iata_code = []

    def get_price(self, parameters: dict):
        self.response = requests.get(url=flight_search_url, params=parameters, headers=header)
        self.response.raise_for_status()
        self.flight_data = self.response.json()
        for i in range(0, len(self.flight_data["data"])):
            self.price.append(self.flight_data["data"][i]["price"])
        return self.price

    # def get_iata_code(self, sheet_data: dict):
    #     for city in sheet_data:
    #         parameters = {
    #             "term": city,
    #             "locale": "en-US",
    #             "location_types": "airport",
    #             "limit":1,
    #             "active_only": "true"
    #         }
    #         response = requests.get(url=get_iata_url, headers=header, params=parameters)
    #         response.raise_for_status()
    #         data = response.json()
    #         self.iata_code.append(data["locations"][0]["code"])
    #     return self.iata_code   