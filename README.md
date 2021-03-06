# stocks-checker

Hi everyone, this is a simple stock price checking python script that'll play an alarm sound whenever the stock price is above a certain threshold that you assign. This uses the Yahoo Finance public API, so thank them for keeping it public and free. As an ape who lives in a country where the NYC Stock Market opens at 10:30PM, it would be unhealthy to stay up all night watching a stock's ticker. I decided to make this script to solve this problem.


### Setup
You will probably need some speakers to fully utilize this script. It can also be used in the background while you're using your computer.

- Firstly, you need to install Python onto your computer. You can get an installer from their website: https://www.python.org/downloads/
- Second, you need to install the following Python libraries via the `pip install` command on your Command Prompt (Windows) or Terminal (MacOS):
  - `pip install yfinance`
  - `pip install pygame`
- Finally, you need to find an MP3 file as your alarm sound. I did not include it in this repository in case I run into copyright issues with the alarm sound I use. So find an alarm sound you wish to use and name it `alarm.mp3` (I personally am using some rock song that I used to jam to, I find it annoying now so I'll definitely wake up from it)

### To run the script

- Download the script "checker.py" in this repository and put it in a folder for itself
- Put the `alarm.mp3` file in this folder as well
- To run the script, open your command prompt and direct it to the folder where you placed this script
- Run the command `python checker.py`
- If you wish to stop it, press CTRL + C (Windows) or CMD + C (MacOS) (It may lag a bit)

That's it! The script should be running and should be displaying and checking the stock price every minute.

### Variables
You can change the following variables in the `stock_checker` class to fit your needs.
- interval - the interval this script checks the stock price in seconds (currently set to 60)
- stock_ticker - you can change which stock this ticker is looking at (currently set to AMC)
- alert_price - when the current price is greater than or equal to this value, the alarm will set off (set to 1000.0, obviously)


Now you apes can go about your day without having to check the stock price every second.
