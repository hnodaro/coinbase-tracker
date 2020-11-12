[![Python 3.6|3.7|3.8](https://img.shields.io/badge/Python-3.6%2F3.7%2F3.8-blue.svg)] [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# coingecko-tracker
Get WhatsApp notifications of cryptocurrencies value from Coingecko.com. To get the notifications, you must have an account on https://www.twilio.com/. Once you get your account you have to get an Account_SID and an AUTH_TOKEN.

![capture coingecko tracker](https://user-images.githubusercontent.com/15652168/98995300-6a2ea880-2531-11eb-843a-aa4fa2e3900f.jpg)

## Installing

**Clone the repo**
```bash
git clone https://github.com/hnodaro/coingecko-tracker.git
```
**Change the working directory to coingecko-tracker**
```bash
cd coingecko-tracker
```

**Install the libraries**
```bash
pip install . -r requirements.txt
```

**Replace variables**
```bash
Modify the account_sid and auth_token variables by the variables that you get from Twilio.
Replace twilio_number by the number of Twilio (it should be 'whatsapp:+14155238886')
Replace my_phone_number by your 'whatsapp:XXX' (XXX is your phone number)
```

**Run:**
```bash
Launch main.py file
```
You are free to change the notifications sheduling or to deploy the app on Heroku to get the notifications automatically.

## Contact

If you have any question, or need extra help, you are welcome to contact me: hnodaro@gmail.com
