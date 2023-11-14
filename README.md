<h1><i>DateEscape</i> </h1>

> **Note**
> Release Version: 1.0


This project will allow you to use twilio to send yourself calls and text messages in order to get out of dates and other things. On the other end of the line will be a recording (any sound you want) really talking into your phone and you will recieve a stream of text messages. 

This project will need a few things to work, and it is a command line interface application but if you are using EC2, it can be accessed anywhere. 

### Things you will need: 

- A t.2 micro AWS EC2 instance running ubuntu (this can be free, and is cheap otherwise)
- A twilio account and phone number (free if you don't use it a ton, otherwise cheap) Note that you will need a mobile phone of your own for confirmation, they do this to avoid spammers I think.
- A recording to be played over the phone when you pick up (the default text content is that your dad is angry at you but this can be easily changed and is explained in this guide.)
- You need to verify your phone number so you can send texts and calls to yourself if you have a trial account. 

### Setup

I will now walk you through step by step to create the application.

If you ever run into problems during installation, search the error code or what you need help with or use ChatGPT.

First, create a twilio account. They should give you some free credit you can use.
https://www.twilio.com/try-twilio

Now follow this guide to set up your account and get a free phone number from twilio (necessary)
https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account

Verify your personal phone number, you can reference this link
https://support.twilio.com/hc/en-us/articles/223180048-How-to-Add-and-Remove-a-Verified-Phone-Number-or-Caller-ID-with-Twilio

Copy the Twilio Phone Number you claim as well as the account sid, and auth on the console page to a .txt on your computer, you will need later. 

Record a voice message to play on the call when you call
Then, upload to Twilio Assets Classic. It will generate a link for you to use when you set up the connection to your instance.

It is reccomended that you save your twilio phone number as a contact with a name to correspond with your recording, for added realism. This can be changed by changing the name of the contact at any time. Otherwise, it will show up as a 1888 number and will look like spam. 


Next create a t.2 micro AWS ec2 Instance running ubuntu. Do only step 1 and 2 of this guide. Step 3 is required when you want to end the instance. Do not use Amazon Linux 2.
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

it's advised by the developer that you keep the instance running for multiple uses, as long as it is t.2 micro and you created your account within the last year and don't have any other instances running, it should be free. 

Enter these commands in your EC2 instance terminal.

If this next command doesn't work, you will need to copy the .git link yourself from the DateEscape github page, look for a green button that says "code" and there will be a link inside of it when you click on it.
git clone https://github.com/JeffreyDinackus/DateEscape.git

You don't need this command unless the last one didn't work, you replace the <> with the .git link for DateEscape.
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


Example(this is a text):
''' python
    message = client.messages \
    .create(
            body='YOU WONT DRIVE FOR A MONTH', # this one, just change the text between the quotes.
            from_=twilio_phone,
            to=my_phone
    )

You have complete control over the order of texts and calls and what is said via text or said over the phone via your recording. Modify the code by adding more or less texts in your script(copy and paste twilio API requests) and more or less calls (copy and paste Call API requests). 

``` python 
Example(this is a call):
    call = client.calls.create(
        url=assets_classic,
        to=my_phone,
        from_=twilio_phone
    )
```

### Troubleshooting

This project makes a number of files holding your specifics. If you think you mistyped any info, you can edit the file and change the values.


this program only allows minutes less than 60 and hours less than 72 in the future, you can change this easily by edting this line in make-a-call.py 

if minutes < 0 or hours < 0 and minutes < 60 and hours < 72:


If you would like to instead use environmental varaibles, you'll have to figure that out yourself. Perhaps in the future that will be added. Contributions welcome!


<p> This was originally a hackathon project, named QuickEscape, for Hoohacks 2023. </p> <p> <a href='https://github.com/JeffreyDinackus/QuickEscape.tech'>https://github.com/JeffreyDinackus/QuickEscape.tech</a></p>
