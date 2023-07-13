import os

def read_my_phone_numbers():
    try:
        with open('my_phone.txt', 'r') as file1:
            my_phone = file1.read().strip()
        
        with open('twilio_phone.txt', 'r') as file2:
            twilio_phone = file2.read().strip()
        
        with open('account_sid.txt', 'r') as file3:
            account_sid = file3.read().strip()
        
        with open('auth_token.txt', 'r') as file4:
            auth_token = file4.read().strip()
        
        return my_phone, twilio_phone, account_sid, auth_token
    
    except FileNotFoundError:
        print("Phone number files not found.")
        print("Please run the initial_setup.py script to set up your phone numbers.")
        exit()
    except Exception as e:
        print("An error occurred while reading phone numbers:", str(e))
        exit()

# Call the function to read phone numbers
my_phone, twilio_phone, account_sid, auth_token = read_my_phone_numbers()

if my_phone == 'default_value' or twilio_phone == 'default_value' or account_sid == 'default_value' or auth_token == 'default_value':
    print("One or more environment variables are not set.")
    print("Please run the initial_setup.py script to set up your phone numbers.")
    exit()

# check if the user entered now, if so, execute immeadiately.

print("when would you like to be called and texted?")
now = input("If NOW type :")
if now == "now" or now == "Now" or now == "NOW":
    print("calling now")
    # make Twilio API requests



import time

def start_timer(duration):
    print("Timer started for", duration)
    time.sleep(duration)
    print("Timer ended.")

# Prompt the user for the duration of the timer
minutes = int(input("How many minutes from now would you like to be called? "))
hours = int(input("How many hours from now would you like to be called? "))

# Calculate the total duration in seconds
total_seconds = (hours * 3600) + (minutes * 60)

# Start the timer
start_timer(total_seconds)





# make Twilio API requests
