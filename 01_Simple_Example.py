import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://profitablepursuits.in/2023/09/19/bankbalance-vs-investment/"  # Replace with the actual URL

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find content with specific class and extract their text
    content = soup.find_all(class_='wp-block-heading')
    
    # Loop through each heading and print its text
    for heading in content:
        print(heading.text)

    # Loop through each paragraph and print its text
    for paragraph in content:
        print(paragraph.text)
else:
    print("Failed to retrieve the webpage.")


