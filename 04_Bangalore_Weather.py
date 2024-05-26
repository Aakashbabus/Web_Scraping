import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

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
        Hour_Information = soup.find_all(class_='hour')
        Forecast_Information = soup.find_all(class_='forecast-temp unitE-BI')
        Forecast_RealFeel_Information = soup.find_all(class_='forecast-feeltemp unitE-BI')
        WindSpeed_Information = soup.find_all(class_='speed-value')
        Cloudy_Information = soup.find_all(class_='entry-precipitation-value cloud-cover')
        Rain_Information = soup.find_all(class_='entry-precipitation-value rain unitE-BI')

        # Prepare lists to hold the extracted data
        hours = []
        forecasts = []
        real_feels = []
        wind_speeds = []
        cloudy_percentages = []
        rain_amounts = []

        # Extract and store the data in lists
        for i in range(12):
            hours.append(Hour_Information[i*2-1].text)
            forecasts.append(Forecast_Information[i].text)
            real_feels.append(Forecast_RealFeel_Information[i].text)
            wind_speeds.append(WindSpeed_Information[i].text)
            cloudy_percentages.append(Cloudy_Information[i].text)
            rain_amounts.append(Rain_Information[i].text)

        # Prepare the data for the DataFrame
        weather_data = {
            'Hour': hours,
            'Forecast': forecasts,
            'Real Feel': real_feels,
            'Wind Speed (km/h)': wind_speeds,
            'Cloudy (%)': cloudy_percentages,
            'Rain (mm)': rain_amounts
        }

        # Create a DataFrame
        df = pd.DataFrame(weather_data)

        # Print the DataFrame using tabulate for better formatting in terminal
        print("\n")
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        print("\n")
    else:
        print("Failed to retrieve the webpage.",response.status_code)


if __name__ == "__main__":
    main()