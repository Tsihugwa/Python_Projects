import requests
from operator import itemgetter

# Constants for the cryptocurrency rankings API
API_URL = 'https://api.coinmarketcap.com/v2/ticker/'
SORT_BY_RANK = 'rank'
SORT_BY_PERCENT_CHANGE = 'percent_change_24h'
SORT_BY_VOLUME = 'volume_24h'

def get_cryptocurrency_rankings(sort_by):
  # Make the API request
  response = requests.get(API_URL)
  data = response.json()

  # Extract the relevant data from the response
  rankings = []
  for cryptocurrency in data['data'].values():
    rank = cryptocurrency['rank']
    name = cryptocurrency['name']
    symbol = cryptocurrency['symbol']
    volume = cryptocurrency['quotes']['USD']['volume_24h']
    percent_change = cryptocurrency['quotes']['USD']['percent_change_24h']
    rankings.append({
      'rank': rank,
      'name': name,
      'symbol': symbol,
      'volume': volume,
      'percent_change': percent_change
    })

  # Sort the rankings
  rankings.sort(key=itemgetter(sort_by), reverse=True)

  return rankings

def print_rankings(rankings):
  # Print the table header
  print('Rank | Name       | Symbol | Volume       | 24h Change')
  print('--------------------------------------------------------------')

  # Print the table rows
  for cryptocurrency in rankings:
    rank = cryptocurrency['rank']
    name = cryptocurrency['name']
    symbol = cryptocurrency['symbol']
    volume = cryptocurrency['volume']
    percent_change = cryptocurrency['percent_change']
    color = '\033[32m' if percent_change > 0 else '\033[31m'
    percent_change = f'{color}{percent_change:+.2f}%\033[0m'
    print(f'{rank:4} | {name:10} | {symbol:6} | {volume:14,.2f} | {percent_change:8}')

# Get the rankings sorted by rank
rankings = get_cryptocurrency_rankings(SORT_BY_RANK)

# Print the rankings
print('\nRANKINGS SORTED BY RANK:\n')
print_rankings(rankings)

# Get the rankings sorted by daily percentage change
rankings = get_cryptocurrency_rankings(SORT_BY_PERCENT_CHANGE)

# Print the rankings
print('\nRANKINGS SORTED BY DAILY PERCENTAGE CHANGE:\n')
print_rankings(rankings)

# Get the rankings sorted by daily volume
rankings = get_cryptocurrency_rankings(SORT_BY_VOLUME)

# Print the rankings
print('\nRANKINGS SORTED BY DAILY VOLUME:\n')
print_rankings(rankings)
