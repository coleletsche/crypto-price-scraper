
# Cryptocurrency Price Tracker

This script uses web scraping to track the prices of various cryptocurrencies. It fetches the current prices from [CoinMarketCap](https://coinmarketcap.com/), calculates the percent change in their prices, and displays this information to the user. It also logs this data to a text file.

## Functionality

1. Imports necessary modules:
   - `requests`: for sending HTTP requests
   - `BeautifulSoup`: for parsing HTML and XML documents
   - `time`: for controlling the frequency of requests
   - `datetime`: for timestamping the price data
   - `termcolor`: for colorizing the output

2. Defines some constants for representing price increase, decrease, and no change.

3. Defines the URLs of the cryptocurrencies on CoinMarketCap that it will track.

4. Initializes a dictionary to store the previous prices of the cryptocurrencies.

5. Begins an infinite loop where it:
   - Prints some headers for each iteration
   - Loops over each cryptocurrency URL, fetches the page, parses it to find the current price, and calculates the percent change since the last price
   - Prints the current price and percent change (color-coded based on whether it's an increase, decrease, or no change)
   - Logs the current price and time to a text file
   - Waits a short period before moving on to the next cryptocurrency
   - Once it's gone through all the cryptocurrencies, it waits a longer period before starting the next iteration

## Requirements

- Python 3
- `requests` module
- `BeautifulSoup` module
- `termcolor` module

## Usage

Run the script with Python:

```
python main.py
```
