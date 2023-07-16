import os

def save_phone_numbers_to_files(my_phone, twilio_phone, account_sid, auth_token, assets_classic):
    # Save phone numbers to separate files
    with open('my_phone.txt', 'w') as file1:
        file1.write(my_phone)
        
    with open('twilio_phone.txt', 'w') as file2:
        file2.write(twilio_phone)
        
    with open('account_sid.txt', 'w') as file3:
        file3.write(account_sid)
        
    with open('auth_token.txt', 'w') as file4:
        file4.write(auth_token)

    with open('assets_classic_link.txt', 'w') as file5:
        file5.write(assets_classic)

# Prompt the user for phone numbers
def main():
    print('Welcome to DateEscape!')
    print('Please enter your info EXACTLY or it will not work')
    print('This script will save your info to files')
    print('If you restart your computer, you can load your info from the files')
    print('You can find your Twilio Account SID and Auth Token at https://www.twilio.com/console')
    print('You can find your Twilio phone number at https://www.twilio.com/console/phone-numbers/incoming')
    print('The developer recommends copying and pasting in most cases to avoid frustration')

    my_phone = input("Enter the phone number you would like to call in this format (USA country code is +1): +1xxxxxxxxxx ")
    twilio_phone = input("Enter your Twilio phone number with the country code in this format (USA country code is +1): +1xxxxxxxxxx ")
    account_sid = input("Enter your Twilio Account Sid: ")
    auth_token = input("Enter your Twilio Auth Token (remember to keep this secret): ")
    assets_classic = input("Enter your link to assets classic on Twilio. This is the link to the mp3 file you want to play. You will need the full link and upload it yourself. (under functions and assets -> Assets(classic), a url) ")

    print("\nYou have entered the following:")
    print("Your Phone Number:", my_phone)
    print("Twilio Account SID:", account_sid)
    print("Twilio Auth Token:", auth_token)
    print("Twilio Phone Number:", twilio_phone)
    print("Twilio Assets Classic Link: ", assets_classic)

    # Save phone numbers to files
    save_phone_numbers_to_files(my_phone, twilio_phone, account_sid, auth_token, assets_classic)

if __name__ == "__main__":
    main()
