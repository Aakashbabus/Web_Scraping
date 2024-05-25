import requests
from bs4 import BeautifulSoup

def main():
    print ("\n")
    get_SENSEX_Data()
    get_NIFTY50_Data()
    get_NIFTYBANK_Data()
    get_NIFTYNXT50_Data()
    get_NIFTYMIDCAP50_Data()
    get_NIFTYSMALLCAP50_Data()
    get_NIFTYIT_Data()
    print ("\n")

def get_NIFTY50_Data():
    # URL of the webpage to scrape
    url = "https://upstox.com/indices/nifty-50-share-price/"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        print("NIFTY 50             Share Price:",content1[0].text,content2[3].text)

    else:
        print("Failed to retrieve the webpage.",response.status_code)


def get_SENSEX_Data():
    # URL of the webpage to scrape
    url = "https://upstox.com/indices/sensex-share-price/"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        print("SENSEX               Share Price:",content1[0].text,content2[3].text)

    else:
        print("Failed to retrieve the webpage.",response.status_code)

def get_NIFTYBANK_Data():
    # URL of the webpage to scrape
    url = "https://upstox.com/indices/nifty-bank-share-price/"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        print("NIFTY BANK           Share Price:",content1[0].text,content2[3].text)

    else:
        print("Failed to retrieve the webpage.",response.status_code)

def get_NIFTYNXT50_Data():
    # URL of the webpage to scrape
    url = "https://upstox.com/indices/nifty-next-50-share-price/"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        print("NIFTY NXT50          Share Price:",content1[0].text,content2[3].text)

    else:
        print("Failed to retrieve the webpage.",response.status_code)

def get_NIFTYMIDCAP50_Data():
    # URL of the webpage to scrape
    url = "https://upstox.com/indices/nifty-midcap-50-share-price/"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        print("NIFTY MIDCAP50       Share Price:",content1[0].text,content2[3].text)

    else:
        print("Failed to retrieve the webpage.",response.status_code)

def  get_NIFTYSMALLCAP50_Data():
    # URL of the webpage to scrape
    url = "https://upstox.com/indices/nifty-smlcap-50-share-price/"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        print("NIFTY SMALLCAP50     Share Price:",content1[0].text,content2[3].text)

    else:
        print("Failed to retrieve the webpage.",response.status_code)

def get_NIFTYIT_Data():
    # URL of the webpage to scrape
    url = "https://upstox.com/indices/nifty-it-share-price/"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        print("NIFTY IT             Share Price:",content1[0].text,content2[3].text)

    else:
        print("Failed to retrieve the webpage.",response.status_code)


if __name__ == "__main__":
    main()