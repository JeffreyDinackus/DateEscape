#!/bin/python3
# Download the helper library from https://www.twilio.com/docs/python/install
#these imports for for twilio
import os
# from twilio.rest import Client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
MY_PHONE = os.environ['MY_PHONE']
TWILIO_PHONE = os.environ['TWILIO_PHONE']
