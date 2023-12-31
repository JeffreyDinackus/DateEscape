import os
import time
from twilio.rest import Client


# def read_environment_variables():
#     my_phone = os.getenv('MY_PHONE')
#     twilio_phone = os.getenv('TWILIO_PHONE')
#     account_sid = os.getenv('TWILIO_ACCOUNT_SID')
#     auth_token = os.getenv('TWILIO_AUTH_TOKEN')
#     assets_classic = os.getenv('ASSETS_CLASSIC_LINK')

#     if None in [my_phone, twilio_phone, account_sid, auth_token, assets_classic]:
#         raise ValueError("One or more environment variables are not set. Please make sure to set MY_PHONE, TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and ASSETS_CLASSIC_LINK environment variables.")

#     return my_phone, twilio_phone, account_sid, auth_token, assets_classic

def read_phone_numbers_from_files():
    # Read phone numbers from files
    try:
        with open('my_phone.txt', 'r') as file1:
            my_phone = file1.read().strip()
        
        with open('twilio_phone.txt', 'r') as file2:
            twilio_phone = file2.read().strip()
        
        with open('account_sid.txt', 'r') as file3:
            account_sid = file3.read().strip()
        
        with open('auth_token.txt', 'r') as file4:
            auth_token = file4.read().strip()

        with open('assets_classic_link.txt', 'r') as file5:
            assets_classic = file5.read().strip()

        return my_phone, twilio_phone, account_sid, auth_token, assets_classic

    except FileNotFoundError:
        print("Phone number files not found.")
        print("Please run the script and enter your phone numbers.")
        exit()
    except Exception as e:
        print("An error occurred while reading phone numbers:", str(e))
        exit()


def start_timer(duration, text_frequency, my_phone, twilio_phone, account_sid, auth_token, assets_classic):
    sleeptime = ""
    # do not set lower than 15-30 seconds because of Twilio's API rate limits. You can get your account shut down. 
    if text_frequency == "frequently":
        sleeptime = 30
    elif text_frequency == "moderately":
        sleeptime = 60
    elif text_frequency == "rarely":
        sleeptime = 120
    elif text_frequency == "none":
        sleeptime = 30
    else:
        print("warning, no text frequency selected, defaulting to 30 seconds")
        sleeptime = 30
    if duration == None:
        print("Duration cannot be null")
        exit()
    elif duration == 0:
        print("Calling now")
        call(my_phone, twilio_phone, account_sid, auth_token, assets_classic, sleeptime)

    elif type(duration) != int:
        print("Duration must be an integer")
        exit()
    else:
        print("Timer started for", duration, "seconds.")
        time.sleep(duration)
        print("Timer ended.")
        print("Calling now")
        # make the call
        call(my_phone, twilio_phone, account_sid, auth_token, assets_classic, sleeptime)

def call(my_phone, twilio_phone, account_sid, auth_token, assets_classic, sleeptime=30):
    print(my_phone, twilio_phone, account_sid, auth_token, assets_classic, sleeptime)
    # Create Twilio client
    client = Client(account_sid, auth_token)
    # Make Twilio API requests
    call = client.calls.create(
        url=assets_classic,
        to=my_phone,
        from_=twilio_phone
    )
    print(call.sid)
    message = client.messages \
        .create(
        body='GET HOME RIGHT NOW.',
        from_=twilio_phone,
        to=my_phone
    )
    time.sleep(sleeptime)
    message = client.messages \
        .create(
        body='GET HOME NOW.',
        from_=twilio_phone,
        to=my_phone
    )
    print(message.sid)
    time.sleep(sleeptime)
    message = client.messages \
        .create(
        body='YOU WON\'T DRIVE FOR A MONTH',
        from_=twilio_phone,
        to=my_phone
    )
    print(message.sid)
    call = client.calls.create(
        url=assets_classic,
        to=my_phone,
        from_=twilio_phone
    )
    print(call.sid)
    exit()        


def main():
    try:
        # Read environment variables
        my_phone, twilio_phone, account_sid, auth_token, assets_classic = read_phone_numbers_from_files()

        # Check if the user wants to be called and texted immediately
        print("When would you like to be called and texted?")
        now = input("If NOW type NOW: ")
        if now.lower().strip() == "now":
            start_timer(0, "none", my_phone, twilio_phone, account_sid, auth_token, assets_classic)  # Call start_timer with 0 duration for immediate action

        # Prompt the user for the duration of the timer
        sentinel1 = False
        while sentinel1 == False: 
            minutes = int(input("How many minutes from now would you like to be called? max by default 60: "))
            hours = int(input("How many hours from now would you like to be called? Max by default 72: "))
            # text_time = int(input("How long would you like to be texted for? "))
            if minutes < 0 or hours < 0 and minutes < 60 and hours < 72:
                print("Time cannot be negative")
            else:
                sentinel1 = True

        text_frequency = ""
        while text_frequency.lower().strip() not in ["frequently", "moderately", "rarely", "none"]:
            text_frequency = input("How often would you like to be texted? (more is quicker), enter frequently, moderately, rarely, or none: Note: it needs to be exactly typed for this to work or it will ask again. CTRL+ C to exit: ")

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