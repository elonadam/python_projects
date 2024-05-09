from twilio.rest import Client

TWILIO_SID = 'AC43d33746c61b3124371833da9f4f85b5'
TWILIO_AUTH_TOKEN = '001d564321a27b13cabe7c13a168da7b'
TWILIO_VIRTUAL_NUMBER = "censored"  # was my number
TWILIO_VERIFIED_NUMBER = "+14845145064"  # my twilio number


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
