import requests
from bs4 import BeautifulSoup

def main():
    get_Bangalore_Hourly_Weather_Report()


def get_Bangalore_Hourly_Weather_Report():
    # URL of the webpage to scrape
    url = "https://weather.interia.com/detailed-forecast-bangalore,cId,45191"  # Replace with the actual URL

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find content with specific class and extract their text
        Hour_Information = soup.find_all(class_ ='hour')
        Forecast_Information = soup.find_all(class_ ='forecast-temp unitE-BI')
        Forecast_RealFeel_Information = soup.find_all(class_ ='forecast-feeltemp unitE-BI')
        WindSpeed_Information = soup.find_all(class_ ='speed-value')
        Cloudy_Inforamtion = soup.find_all(class_ ='entry-precipitation-value cloud-cover')
        Rain_Information = soup.find_all(class_ ='entry-precipitation-value rain unitE-BI')

        for i in range(0,12):
            print("Hour         :",Hour_Information[i*2-1].text)
            print("Forecast     :",Forecast_Information[i].text)
            print("Real Feel    :",Forecast_RealFeel_Information[i].text)
            print("Wind Speed   :",WindSpeed_Information[i].text,"km/h")
            print("Cloudy       :",Cloudy_Inforamtion[i].text)
            print("Rain         :",Rain_Information[i].text)
            print("\n")

    else:
        print("Failed to retrieve the webpage.",response.status_code)


if __name__ == "__main__":
    main()