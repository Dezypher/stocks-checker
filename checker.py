import yfinance as yf
import threading
import datetime
from pygame import mixer

class stock_checker():
    # Variables
    interval = 60 # In seconds
    amc_ticker = yf.Ticker("AMC") # Stock ticker we are checking
    alert_price = 20.0 # Price point when the alarm would trigger

    alarmed = False

    # Alarm sound initialization
    mixer.init()
    mixer.music.load('alarm.mp3')


    def check_stock(self):
        stock_info = self.amc_ticker.info
        data = self.amc_ticker.history()
        last_quote = (data.tail(1)['Close'].iloc[0])
        bid = stock_info['bid']
        print("Current bid for AMC is $" + str(round(last_quote, 2)) + " as of " + str(datetime.datetime.now()))

        if bid >= self.alert_price:
            print("Alert price point reached!")
            mixer.music.play()
            self.alarmed = True

    def start_process(self):
        if not self.alarmed:
            threading.Timer(self.interval, self.start_process).start()
            self.check_stock()

stock_checker_instance = stock_checker()
stock_checker_instance.start_process()