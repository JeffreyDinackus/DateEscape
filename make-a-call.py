import os
import time
from twilio.rest import Client


def read_environment_variables():
    my_phone = os.getenv('MY_PHONE')
    twilio_phone = os.getenv('TWILIO_PHONE')
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    assets_classic = os.getenv('ASSETS_CLASSIC_LINK')

    if None in [my_phone, twilio_phone, account_sid, auth_token, assets_classic]:
        raise ValueError("One or more environment variables are not set. Please make sure to set MY_PHONE, TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and ASSETS_CLASSIC_LINK environment variables.")

    return my_phone, twilio_phone, account_sid, auth_token, assets_classic

def start_timer(duration, text_frequency, my_phone, twilio_phone, account_sid, auth_token, assets_classic):
    client = Client(account_sid, auth_token)
    print("Timer started for", duration, "seconds.")
    sleeptime = ""
    if text_frequency == "frequently":
        sleeptime = 15
    elif text_frequency == "moderately":
        sleeptime = 30
    elif text_frequency == "rarely":
        sleeptime = 60
    
    time.sleep(duration)
    print("Timer ended.")
    print("Calling now")

    if text_frequency == "none":
        call = client.calls.create(
            url=assets_classic,
            to=my_phone,
            from_=twilio_phone
        )
        time.sleep(50)
        call = client.calls.create(
            url=assets_classic,
            to=my_phone,
            from_=twilio_phone
        )
        exit()

    # Make Twilio API requests
    call = client.calls.create(
        url=assets_classic,
        to=my_phone,
        from_=twilio_phone
    )
    message = client.messages.create(
        body='GET HOME RIGHT NOW.',
        from_=twilio_phone,
        to=my_phone
    )
    time.sleep(sleeptime)
    message = client.messages.create(
        body='GET HOME NOW.',
        from_=twilio_phone,
        to=my_phone
    )
    time.sleep(sleeptime)
    message = client.messages.create(
        body='YOU WON\'T DRIVE FOR A MONTH',
        from_=twilio_phone,
        to=my_phone
    )
    call = client.calls.create(
        url=assets_classic,
        to=my_phone,
        from_=twilio_phone
    )
    exit()

def main():
    try:
        # Read environment variables
        my_phone, twilio_phone, account_sid, auth_token, assets_classic = read_environment_variables()

        # Create Twilio client
        client = Client(account_sid, auth_token)

        # Check if the user wants to be called and texted immediately
        print("When would you like to be called and texted?")
        now = input("If NOW type NOW: ")
        if now.lower().strip() == "now":
            start_timer(0, "none", my_phone, twilio_phone, account_sid, auth_token, assets_classic)  # Call start_timer with 0 duration for immediate action

        # Prompt the user for the duration of the timer
        while sentinel1 == False: 
            minutes = int(input("How many minutes from now would you like to be called? "))
            hours = int(input("How many hours from now would you like to be called? "))
            # text_time = int(input("How long would you like to be texted for? "))
            if minutes < 0 or hours < 0 and minutes < 60 and hours < 72:
                print("Time cannot be negative")
            else:
                sentinel1 = True

        text_frequency = ""
        while text_frequency.lower().strip() not in ["frequently", "moderately", "rarely", "none"]:
            text_frequency = input("How often would you like to be texted? (more is more expensive), enter frequently, moderately, rarely, or none: Note: it needs to be exactly typed for this to work or it will ask again. CTRL+ C to exit")

        # Calculate the total duration in seconds
        total_seconds = (hours * 3600) + (minutes * 60)

        # Start the timer
        start_timer(total_seconds, text_frequency, my_phone, twilio_phone, account_sid, auth_token, assets_classic)

    except ValueError as ve:
        print(str(ve))
        exit()
    except Exception as e:
        print("An error occurred:", str(e))
        exit()

if __name__ == "__main__":
    main()