# stocks-checker

Hi everyone, this is a simple Stock bid price checking python script that'll play an alarm sound whenever the stock price is above a certain threshold that you assign. This uses the Yahoo Finance public API, so thank them for keeping it public and free.


### Setup

- Firstly, you need to install Python onto your computer. You can get an installer from their website: https://www.python.org/downloads/
- Second, you need to install the following Python libraries via the `pip install` command on your command prompt:
  - `pip install yfinance`
  - `pip install pygame`
- Finally, you need to find an MP3 file as your alarm sound. I did not include it in this repository in case I run into copyright issues with the alarm sound I use. So find an alarm sound you wish to use and name it `alarm.mp3`

### To run the script

- Download the script in this repository and put it in a folder for itself
- Put the `alarm.mp3` file in this folder as well
- To run the script, open your command prompt and direct it to the folder where you placed this script
- Run the command `python checker.py`
- If you wish to stop it, press CTRL + C (Windows) or CMD + C (MacOS)

That's it! The script should be running and should be displaying and checking the stock price every minute.

### Variables
You can change the following variables in the `stock_checker` class to fit your needs.
- interval - the interval this script checks the stock price in seconds
- stock_ticker - you can change which stock this ticker is looking at (currently set to AMC)
- alert_price - when the current price is greater than or equal to this value, the alarm will set off
