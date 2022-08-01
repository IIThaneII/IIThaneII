from email import message
from twilio.rest import Client

account_sid = "ACddae4be71f292bfaab501a697d7b9e9d"
auth_token = "1cb1353de176b3549ec450f5ea929853"
client = Client(account_sid, auth_token)

class NotificationManager:
    def __init__(self):
        self.message = client.messages \
        .create(
            body=self.message,
            from_="+17432008088",
            to="+84963425495"
        )
        print(self.message.status)

    def message_body(self, cityTo, price):
        self.message = f"New lowest plane ticket price!\n\nFlight to {cityTo} with only {price} Euro."