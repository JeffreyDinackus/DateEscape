import os

def read_my_phone_numbers():
    try:
        with open('my_phone.txt', 'r') as file1:
            phone_number1 = file1.read().strip()
        
        with open('twilio_phone.txt', 'r') as file2:
            phone_number2 = file2.read().strip()
        
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




# Print the phone numbers
print("Phone Number 1:", phone_number1)
print("Phone Number 2:", phone_number2)


# check if the user entered now, if so, execute immeadiately.




# make Twilio API requests
