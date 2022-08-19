from datetime import datetime, timedelta

time_now = datetime.now()

class FlightData:
    def __init__(self):
        self.dateFrom = time_now.strftime('%Y-%m-%d')
        self.dateTo = datetime.strftime(datetime.now() + timedelta(172),'%Y-%m-%d')
        
    def flight_info(self, fly_from, fly_to):
        self.parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "dateFrom": self.dateFrom,
            "dateTo": self.dateTo,
        }
        return self.parameters