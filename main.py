from pycoingecko import CoinGeckoAPI
import schedule
import time
from twilio.rest import Client
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
cg = CoinGeckoAPI()   
client = Client()

def get_btc_value():
    res = cg.get_price(ids='bitcoin,ethereum', vs_currencies=['usd','eur'])
    current_date = datetime.today().strftime('%m/%d/%Y, %H:%M:%S')
    msg = current_date +"\n" + "Bitcoin current value:" + "\n" + str(res['bitcoin']['usd']) + ' USD' +"\n" \
        + str(res['bitcoin']['eur']) + ' EUR' + "\n" \
        + "Ethereum current value: " + "\n" + str(res['ethereum']['usd']) + ' USD' +"\n" \
        + str(res['ethereum']['eur']) + ' EUR' + "\n"
    send_message("whatsapp:+14155238886", "whatsapp:+33647997524", msg)

def send_message(from_number, dest_number, body):
    client.messages.create(body=body,
                        from_=from_number,
                        to=dest_number)

if __name__ == "__main__":
    schedule.every().day.at("10:30").do(get_btc_value)
    while True:
        schedule.run_pending()
        time.sleep(1)
