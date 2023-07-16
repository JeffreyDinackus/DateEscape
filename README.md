<h1><i>DateEscape</i> </h1>

This project will allow you to use twilio to send yourself calls and text messages in order to get out of dates and other things. On the other end of the line will be a recording (any sound you want) really talking into your phone and you will recieve a stream of text messages. 

This project will need a few things to work, and it is a command line interface application. 

Things you will need: 

- A t.2 micro AWS EC2 instance running ubuntu (this can be free, and is cheap otherwise)
- A twilio account and phone number (free if you don't use it a ton, otherwise cheap) Note that you will need a mobile phone of your own for confirmation, they do this to avoid spammers I think.

I will now walk you through step by step to create the application.

First, create a twilio account. They should give you some free credit you can use.
https://www.twilio.com/try-twilio

Now follow this guide to set up your account and get a free phone number from twilio (necessary)
https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account

Record a voice message to play on the call when you call
Then, upload to Twilio Assets Classic. It will generate a link for you to use when you set up the connection to your instance.

Copy the Twilio Phone Number you claim as well as the account sid, and auth on the console page, you will need later. 



Next create a t.2 micro AWS ec2 Instance running ubuntu. Do only step 1 and 2 of this guide. Step 3 is required when you want to end the instance. 
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

Enter these commands in your EC2 instance terminal.

git clone <repository .git link>

sudo apt install python3-pip

pip3 install twilio

Then enter

python3 initial-setup.py
python3 test-connection.py
if you recieve a text message after entering that last command, you are good to go. 


To start the script for real usage, enter

python3 make-a-call.py

please note: the text messages are currently set up to be like they are from a angry dad. Feel free to change them. You would need to change the "body" field of the Twilio API requests. 


Example: 
    message = client.messages \
    .create(
            body='YOU WONT DRIVE FOR A MONTH', // this one, just change the text between the quotes.
            #hidden for privacy
            from_=twilio_phone,
            to=my_phone
    )


Troubleshooting

This project makes a number of files holding your specifics. If you think you mistyped any info, you can edit the file and change the values.


<p> This was originally a hackathon project, named QuickEscape, for Hoohacks 2023. </p> <p> <a href='https://github.com/JeffreyDinackus/QuickEscape.tech'>https://github.com/JeffreyDinackus/QuickEscape.tech</a></p>
