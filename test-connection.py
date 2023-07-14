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

print("Testing connection to Twilio API...")
client = Client(account_sid, auth_token)

print("Using data:", my_phone, twilio_phone, account_sid, auth_token)

message = client.messages \
.create(
  body='Connection established!',
  #hidden for privacy
  from_=twilio_phone,
  to=my_phone
)

print("if you don't recieve a text message, check your phone number files and try again.")