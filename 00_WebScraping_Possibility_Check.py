import requests
from bs4 import BeautifulSoup

def check_scrape_website(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the content of the response
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract and print the title of the page
            title = soup.title.string if soup.title else 'No title found'
            print(f"Successfully accessed the page. Title: {title}")
        else:
            print(f"Failed to access the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# URL to scrape
url = "https://www.goodreturns.in/gold-rates/bangalore.html"

# Check if scraping is possible
check_scrape_website(url)
