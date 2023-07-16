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

# if my_phone == 'default_value' or twilio_phone == 'default_value' or account_sid == 'default_value' or auth_token == 'default_value':
#     print("One or more environment variables are not set.")
#     print("Please run the initial_setup.py script to set up your phone numbers.")
#     exit()


client = Client(account_sid, auth_token)


# check if the user entered now, if so, execute immeadiately.
print("when would you like to be called and texted?")
now = input("If NOW type :")
if now == "now" or now == "Now" or now == "NOW":
    print("calling now")
    # make Twilio API requests
    call = client.calls.create(
            #this is hosted by twilio assets static hosting. 
            url='https://telemagenta-goldfish-8538.twil.io/assets/angry_dad.mp3',
            to=my_phone,
            from_=twilio_phone
            )
    message = client.messages \
    .create(
            body='GET HOME RIGHT NOW.',
            #hidden for privacy
            from_=twilio_phone,
            to=my_phone
    )
    time.sleep(10)
    message = client.messages \
    .create(
            body='GET HOME NOW.',
            #hidden for privacy
            from_=twilio_phone,
            to=my_phone
    )

    time.sleep(10)
    message = client.messages \
    .create(
            body='YOU WONT DRIVE FOR A MONTH',
            #hidden for privacy
            from_=twilio_phone,
            to=my_phone
    )



import time

def start_timer(duration, text_frequentcy, text_time):
    print("Timer started for", duration, "seconds.")
    sleeptime = ""
    if text_frequentcy == "frequently":
        sleeptime = 15

    elif text_frequentcy == "moderately":
        sleeptime = 30
    
    elif text_frequentcy == "rarely":  
        sleeptime = 60
    
    time.sleep(duration)
    print("Timer ended.")
    print("calling now")

    if text_frequentcy == "none":
        call = client.calls.create(
            #this is hosted by twilio assets static hosting. 
            url='https://telemagenta-goldfish-8538.twil.io/assets/angry_dad.mp3',
            to=my_phone,
            from_=twilio_phone
            )
        time.sleep(50)
        call = client.calls.create(
            #this is hosted by twilio assets static hosting. 
            url='https://telemagenta-goldfish-8538.twil.io/assets/angry_dad.mp3',
            to=my_phone,
            from_=twilio_phone
            )
        exit()

    # make Twilio API requests
    call = client.calls.create(
            #this is hosted by twilio assets static hosting. 
            url='https://telemagenta-goldfish-8538.twil.io/assets/angry_dad.mp3',
            to=my_phone,
            from_=twilio_phone
            )
    message = client.messages \
    .create(
            body='GET HOME RIGHT NOW.',
            #hidden for privacy
            from_=twilio_phone,
            to=my_phone
    )
    time.sleep(sleeptime)
    message = client.messages \
    .create(
            body='GET HOME NOW.',
            #hidden for privacy
            from_=twilio_phone,
            to=my_phone
    )

    time.sleep(sleeptime)
    message = client.messages \
    .create(
            body='YOU WONT DRIVE FOR A MONTH',
            #hidden for privacy
            from_=twilio_phone,
            to=my_phone
    )
    call = client.calls.create(
        #this is hosted by twilio assets static hosting. 
        url='https://telemagenta-goldfish-8538.twil.io/assets/angry_dad.mp3',
        to=my_phone,
        from_=twilio_phone
    )
    exit()

# Prompt the user for the duration of the timer
minutes = int(input("How many minutes from now would you like to be called? "))
hours = int(input("How many hours from now would you like to be called? "))
text_time = input("How long would you like to be texted for? ")

text_frequentcy = ""

while text_frequentcy.lower() not in ["frequently", "moderately", "rarely", "none"]:
    text_frequentcy = input("How often would you like to be texted? (more is more expensive), enter frequently, moderately, rarely, or none: ")

if text_frequentcy == "frequently" or text_frequentcy == "Frequently" or text_frequentcy == "FREQUENTLY":
    X = 1
    print(X)

# Calculate the total duration in seconds
total_seconds = (hours * 3600) + (minutes * 60)

# Start the timer
start_timer(total_seconds, text_frequentcy, text_time)

