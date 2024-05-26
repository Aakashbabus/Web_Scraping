import requests
import pandas as pd

# Define the API endpoint and your API key
api_key = '85821e370dc0ced57d487392'  # Replace 'YOUR_API_KEY' with your actual API key
url = f'https://v6.exchangerate-api.com/v6/85821e370dc0ced57d487392/latest/USD'

# Fetch the data
response = requests.get(url)
data = response.json()

# Check if the request was successful
if data['result'] == 'success':
    # Extract relevant exchange rates
    rates = data['conversion_rates']
    usd_to_eur = rates['EUR']
    usd_to_jpy = rates['JPY']
    usd_to_inr = rates['INR']
    usd_to_gbp = rates['GBP']
    usd_to_aud = rates['AUD']
    usd_to_cad = rates['CAD']
    usd_to_cny = rates['CNY']
    usd_to_hkd = rates['HKD']
    
    # Prepare the data for the DataFrame
    forex_data = {
        'Currency Pair': ['USD to EUR', 'USD to JPY', 'USD to INR', 'USD to GBP', 'USD to AUD', 'USD to CAD', 'USD to CNY', 'USD to HKD'],
        'Exchange Rate': [usd_to_eur, usd_to_jpy, usd_to_inr, usd_to_gbp, usd_to_aud, usd_to_cad, usd_to_cny, usd_to_hkd]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(forex_data)
    
    # Display the DataFrame
    print(df)
else:
    print("Failed to retrieve data")