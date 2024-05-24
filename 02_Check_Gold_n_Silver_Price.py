import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://upstox.com/gold-rates/gold-rates-in-bangalore/"  # Replace with the actual URL

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find content with specific class and extract their text
    content = soup.find_all(class_='whitespace-nowrap')
    
    # Loop through each heading and print its text
    #for heading in content:
    #   print(heading.text)
    print("Price of 24 Carrot Gold per gram in Bangalore today is :",content[4].text)

else:
    print("Failed to retrieve the webpage.",response.status_code)


# URL of the webpage to scrape
url = "https://www.urbanmoney.com/silver-rate/bangalore"  # Replace with the actual URL

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find content with specific class and extract their text
    content = soup.find_all(class_='font22 textBlack fontBold mb10')
    
    # Loop through each heading and print its text
    #for heading in content:
    #   print(heading.text)
    print("Price of 1kg pure silver in Bangalore today is :",content[0].text)

else:
    print("Failed to retrieve the webpage.",response.status_code)