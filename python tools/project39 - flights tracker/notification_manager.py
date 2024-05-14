from twilio.rest import Client
import os

twilio_sid = os.environ.get('SID')
auth_token = os.environ.get('AUTHTOKEN')
twilio_number = "+15709337522"  # my twilio number
my_number = os.environ.get('MYNUMBER')


# print(f"sid is {twilio_sid} auth is {auth_token} my num is {my_number}")


class NotificationManager:
    def __init__(self):
        self.client = Client(twilio_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_number,
            to=my_number,
        )
        print(message.sid)
