print("run this script after you have run the setup script")

input("Press Enter to continue... or ctrl + c to cancel")

from twilio.rest import Client
import os


def read_environment_variables():
    my_phone = os.getenv('MY_PHONE')
    twilio_phone = os.getenv('TWILIO_PHONE')
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    assets_classic = os.getenv('ASSETS_CLASSIC_LINK')

    if None in [my_phone, twilio_phone, account_sid, auth_token, assets_classic]:
        raise ValueError("One or more environment variables are not set. Please make sure to set MY_PHONE, TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and ASSETS_CLASSIC_LINK environment variables.")

    return my_phone, twilio_phone, account_sid, auth_token, assets_classic

print(os.environ)
# Call the function to read phone numbers
my_phone, twilio_phone, account_sid, auth_token, assets_classic = read_environment_variables()




print("Testing connection to Twilio API...")
client = Client(account_sid, auth_token)

print("Using data:", my_phone, twilio_phone, account_sid, auth_token, assets_classic)

print("If all works well you will recieve a text message and a phone call.")

message = client.messages \
.create(
  body='Connection established (for text only)!',
  #hidden for privacy
  from_=twilio_phone,
  to=my_phone
)
print("text sent")
call = client.calls.create(
    #this is hosted by twilio assets static hosting. 
    url=assets_classic,
    to=my_phone,
    from_=twilio_phone
)
print("call sent")
print("if you don't recieve both a phone call and text message, check your files and try again.")