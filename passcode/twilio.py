import os

from twilio.rest import Client


twilio = Client(
    os.getenv('TWILLIO_SID'),
    os.getenv('TWILLIO_TOKEN')
)
