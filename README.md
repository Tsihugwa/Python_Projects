# Python_Projects
Welcome to the cryptocurrency rankings GitHub repository!

This code allows you to retrieve and display the current rankings of various cryptocurrencies based on their rank, daily percentage change, or daily volume.

To use this code, you will need to install the requests library. Simply run pip install requests in your terminal to install it.

The API used to retrieve the data is the CoinMarketCap API, located at 'https://api.coinmarketcap.com/v2/ticker/'. You can change the API URL in the API_URL constant if needed.

To retrieve the rankings, call the get_cryptocurrency_rankings() function with the desired sorting parameter. The options for sorting are SORT_BY_RANK, SORT_BY_PERCENT_CHANGE, and SORT_BY_VOLUME.

To display the rankings, call the print_rankings() function with the list of rankings returned by get_cryptocurrency_rankings(). The rankings will be printed in a table format with the rank, name, symbol, daily volume, and daily percentage change for each cryptocurrency.

Thank you for using this code! If you have any questions or issues, please feel free to open a new issue in this repository.

Author RYAN TSIHUGWA
