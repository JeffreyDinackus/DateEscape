print("run this script after you have run the setup script")

input("Press Enter to continue... or ctrl + c to cancel")

from twilio.rest import Client


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

        with open('assets_classic_link.txt', 'r') as file5:
            assets_classic = file4.read().strip()

        return my_phone, twilio_phone, account_sid, auth_token, assets_classic
    
    except FileNotFoundError:
        print("Some required information not found.")
        print("Please run the initial_setup.py script to set up your phone numbers.")
        exit()
    except Exception as e:
        print("An error occurred while reading phone numbers:", str(e))
        exit()

# Call the function to read phone numbers
my_phone, twilio_phone, account_sid, auth_token, assets_classic = read_my_phone_numbers()

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