import yfinance as yf
import threading
import datetime
from pygame import mixer

class StockChecker():
    alarmed = False

    # Alarm sound initialization
    mixer.init()
    mixer.music.load('alarm.mp3')

    def __init__(self, stock_ticker_name=None, interval=60, alert_price=100.0, interface=None):
        self.stock_ticker_name = stock_ticker_name
        self.current_price = 0.00

        if stock_ticker_name is not None:
            self.interval = interval # In seconds
            self.alert_price = alert_price # Price point when the alarm would trigger
            self.stock_ticker = yf.Ticker(self.stock_ticker_name) # Stock ticker we are checking
            self.interface = interface
        else:
            stock_ticker_name = "No stock selected"

    def check_stock(self):
        data = self.stock_ticker.history()
        self.current_price = (data.tail(1)['Close'].iloc[0])
        print("Current bid for " + self.stock_ticker_name + " is $" + str(round(self.current_price, 4)) + " as of " + str(datetime.datetime.now()))

        if self.current_price >= self.alert_price:
            print("Alert price point reached!")
            mixer.music.play(-1, 0.0)
            self.alarmed = True

    def start_process(self):
        if not self.alarmed:
            self.check_stock()
            if not self.alarmed:
                threading.Timer(self.interval, self.start_process).start()

            if self.interface is not None:
                self.interface.update_labels(
                    current_price=self.current_price
                )
    
    def stop_process(self):
        self.alarmed = True
        mixer.music.stop()

if __name__ == "__main__":
    stocks_checker = StockChecker(
        stock_ticker_name="AMC",
        interval=60,
        alert_price=1000.0
    )
    stocks_checker.start_process()
