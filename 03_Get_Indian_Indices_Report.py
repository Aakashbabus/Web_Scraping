import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

def main():
    data = []
    data.append(get_SENSEX_Data())
    data.append(get_NIFTY50_Data())
    data.append(get_NIFTYBANK_Data())
    data.append(get_NIFTYNXT50_Data())
    data.append(get_NIFTYMIDCAP50_Data())
    data.append(get_NIFTYSMALLCAP50_Data())
    data.append(get_NIFTYIT_Data())

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["Index", "Share Price", "1D Change", "1M Change", "1Y Change"])
    
    
    # Print the DataFrame as a table
    print("\n")
    print(tabulate(df, headers='keys', tablefmt='grid'))
    print("\n")
    
def get_NIFTY50_Data():
    url = "https://upstox.com/indices/nifty-50-share-price/"
    return get_data(url, "NIFTY 50")

def get_SENSEX_Data():
    url = "https://upstox.com/indices/sensex-share-price/"
    return get_data3(url, "SENSEX")

def get_NIFTYBANK_Data():
    url = "https://upstox.com/indices/nifty-bank-share-price/"
    return get_data1(url, "NIFTY BANK")

def get_NIFTYNXT50_Data():
    url = "https://upstox.com/indices/nifty-next-50-share-price/"
    return get_data1(url, "NIFTY NXT50")

def get_NIFTYMIDCAP50_Data():
    url = "https://upstox.com/indices/nifty-midcap-50-share-price/"
    return get_data(url, "NIFTY MIDCAP50")

def get_NIFTYSMALLCAP50_Data():
    url = "https://upstox.com/indices/nifty-smlcap-50-share-price/"
    return get_data(url, "NIFTY SMALLCAP50")

def get_NIFTYIT_Data():
    url = "https://upstox.com/indices/nifty-it-share-price/"
    return get_data2(url, "NIFTY IT")

def get_data(url, index_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        content3 = soup.find_all(class_='text-sm font-medium leading-5 text-bar-chart-green')
        share_price = content1[0].text
        Day_Change = content2[3].text
        Month_Change = content3[2].text
        Year_Change = content3[4].text
        return [index_name, share_price, Day_Change, Month_Change, Year_Change]
    else:
        return [index_name, "Failed to retrieve data", "", "", ""]
    
def get_data1(url, index_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        content3 = soup.find_all(class_='text-sm font-medium leading-5 text-bar-chart-green')
        share_price = content1[0].text
        Day_Change = content2[3].text
        Month_Change = content3[3].text
        Year_Change = content3[5].text
        return [index_name, share_price, Day_Change, Month_Change, Year_Change]
    else:
        return [index_name, "Failed to retrieve data", "", "", ""]
    
def get_data2(url, index_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        content3 = soup.find_all(class_='text-sm font-medium leading-5 text-bar-chart-green')
        share_price = content1[0].text
        Day_Change = content2[3].text
        Month_Change = content3[2].text
        Year_Change = content3[3].text
        return [index_name, share_price, Day_Change, Month_Change, Year_Change]
    else:
        return [index_name, "Failed to retrieve data", "", "", ""]
    
def get_data3(url, index_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content1 = soup.find_all(class_='text-[32px]')
        content2 = soup.find_all(class_='text-base')
        content3 = soup.find_all(class_='text-sm font-medium leading-5 text-bar-chart-green')
        share_price = content1[0].text
        Day_Change = content2[3].text
        Month_Change = "TBD"
        Year_Change = content3[0].text
        return [index_name, share_price, Day_Change, Month_Change, Year_Change]
    else:
        return [index_name, "Failed to retrieve data", "", "", ""]
    
if __name__ == "__main__":
    main()
