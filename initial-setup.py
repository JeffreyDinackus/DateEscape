#! /bin/python3

import os

def save_phone_numbers(my_phone, twilio_phone, account_sid, auth_token, assets_classic):
    # Set phone numbers as environment variables
    os.environ['MY_PHONE'] = my_phone
    os.environ['TWILIO_PHONE'] = twilio_phone
    os.environ['TWILIO_ACCOUNT_SID'] = account_sid
    os.environ['TWILIO_AUTH_TOKEN'] = auth_token
    os.environ['ASSETS_CLASSIC_LINK'] = assets_classic
    
# Prompt the user for phone numbers
def main():
    print('Welcome to DateEscape!')
    print('Please enter your info EXACTLY or it will not work')
    print('This script will save your info to environment variables')
    print('If you restart your computer, you will have to run this script again')
    print('You can find your Twilio Account SID and Auth Token at https://www.twilio.com/console')
    print('You can find your Twilio phone number at https://www.twilio.com/console/phone-numbers/incoming')
    print('The developer reccomends copying and pasting in most cases to avoid fustration')
    print("after running this script once, files will be created for each input, and you can directly edit each one in the respective .txt file")
    my_phone = input("Enter the phone number you would like to call in this format (USA country code is +1): +1xxxxxxxxxx ")
    twilio_phone = input("Enter your Twilio phone number with the country code in this format (USA country code is +1): +1xxxxxxxxxx ")
    account_sid = input("Enter your Twilio Account Sid: ")
    auth_token = input("Enter your Twilio Auth Token (remember to keep this secret): ")
    assets_classic = input("Enter your link to assets classic on twilio. This is the link to the mp3 file you want to play. You will need the full link and upload it yourself. (under functions and assets -> Assets(classic), a url) ")

    print("you have entered the following: ")
    print("Your Phone Number:", my_phone)
    print("Twilio Account SID:", account_sid)
    print("Twilio Auth Token:", auth_token)
    print("Twilio Phone Number:", twilio_phone)
    print("Twilio Assets Classic Link: ", assets_classic)


    # Call the function to save phone numbers
    save_phone_numbers(my_phone, twilio_phone, account_sid, auth_token, assets_classic)


if __name__ == "__main__":
    main()