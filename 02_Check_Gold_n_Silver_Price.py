import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import json

def main():
    gold_prices = get_gold_price_India()
    silver_prices = get_silver_price_India()
    
    print("\nGold and Silver Prices in Bangalore :\n")
    # Combine the data into a single DataFrame
    data = {
        'Period': ["Today", "30 Days", "180 Days"],
        'Gold /10g': gold_prices,
        'Silver /1Kg': silver_prices
    }
    df = pd.DataFrame(data)
    
    # Display the DataFrame as a table with borders
    print(tabulate(df, headers='keys', tablefmt='grid'))
    print("\n")

    make_gapi_request()
    print("\n")

def get_gold_price_India():
    url = "https://upstox.com/gold-rates/gold-rates-in-bangalore/"  # Replace with the actual URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        gold_prices = []

        content = soup.find_all(class_='whitespace-nowrap')
        gold_prices.append(content[4].text)
        
        row = soup.find_all('tr')[19]
        column1 = row.find_all('td')[1].text
        gold_prices.append(column1)

        row = soup.find_all('tr')[22]
        column1 = row.find_all('td')[1].text
        gold_prices.append(column1)

        return gold_prices
    else:
        print("Failed to retrieve the webpage.", response.status_code)
        return []

def get_silver_price_India():
    url = "https://www.urbanmoney.com/silver-rate/bangalore"  # Replace with the actual URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        silver_prices = []

        content = soup.find_all(class_='font22 textBlack fontBold mb10')
        silver_prices.append(content[0].text)
        silver_prices.append("TBD")
        silver_prices.append("TBD")

        return silver_prices
    else:
        print("Failed to retrieve the webpage.", response.status_code)
        return []
    
def make_gapi_request():
    api_key = "YOUR API KEY"
    symbol = "XAU"
    curr = "INR"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()  # Parse response text to JSON
        price_gram_24k = result.get("price_gram_24k")  # Safely extract the value
        if price_gram_24k is not None:
            print(" International Gold price per gram: ₹",price_gram_24k)
        else:
            print("price_gram_24k not found in the response")
        
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()




