#! /bin/python3

import os

def save_phone_numbers(number1, number2):
    # Save phone numbers to files
    with open('my_phone.txt', 'w') as file1:
        file1.write(number1)
    
    with open('twilio_phone.txt', 'w') as file2:
        file2.write(number2)

    with open('account_sid.txt', 'w') as file3:
        file3.write(account_sid)

    with open('auth_token.txt', 'w') as file4:
        file4.write(auth_token)

    # Set phone numbers as environment variables
    os.environ['MY_PHONE'] = number1
    os.environ['TWILIO_PHONE'] = number2
    os.environ['account_sid'] = account_sid
    os.environ['auth_token'] = auth_token
    
# Prompt the user for phone numbers
number1 = input("Enter the phone number you would like to call: ")
number2 = input("Enter your Twilio phone number: ")
account_sid = input("Enter your Twilio Account Sid: ")
auth_token = input("Enter your Twilio Auth Token: ")

# Call the function to save phone numbers and set environment variables
save_phone_numbers(number1, number2, account_sid, auth_token)
