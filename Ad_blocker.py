import urllib.request
from bs4 import BeautifulSoup

# URL of the website to block ads on
url = 'https://www.facebook.com'

# Fetch the website content
response = urllib.request.urlopen(url)
html = response.read()

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all the div elements that contain ads
ads = soup.find_all('div', class_='ad')

# Remove the ads from the website content
for ad in ads:
    ad.decompose()

# Print the modified website content
print(soup)
