#!/bin/python3
# Download the helper library from https://www.twilio.com/docs/python/install
#these imports for for twilio
import os
# from twilio.rest import Client
account_sid = os.environ.get('TWILIO_ACCOUNT_SID', 'default_value')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN', 'default_value')
MY_PHONE = os.environ.get('MY_PHONE', 'default_value')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN', 'default_value')

# if env var fails, import from file, otherwise give user a msg and end the script.

def read_my_phone_numbers():
    try:
        # Read phone numbers from files
        with open('phone1.txt', 'r') as file1:
            phone_number1 = file1.read()
    except FileNotFoundError:
        print("Phone number files not found.")
        print("Please run the initial_setup.py script to set up your phone numbers.")
        exit()
    except Exception as e:
        print("An error occurred while reading phone numbers, try running the initial_setup.py script.", str(e))
        exit()

def read_twilio_number():
    try:
        # Read phone numbers from files
        with open('twilio_phone.txt', 'r') as file1:
            twilio_phone = file1.read()
    except FileNotFoundError:
        print("Phone number files not found.")
        print("Please run the initial_setup.py script to set up your phone numbers.")
        exit()
    except Exception as e:
        print("An error occurred while reading phone numbers, try running the initial_setup.py script.", str(e))
        exit()
    
    # Return the phone numbers
    return twilio_phone


# Call the function to read phone numbers

if MY_PHONE == 'default_value':
    phone_number1 = read_my_phone_numbers()
    
    exit()

phone_number2 = read_twilio_number()

# Print the phone numbers
print("Phone Number 1:", phone_number1)
print("Phone Number 2:", phone_number2)


# check if the user entered now, if so, execute immeadiately.




# make Twilio API requests
