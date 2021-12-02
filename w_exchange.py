#30/11/2021 - do not develop here, go w_ing_asset_class
# Python helper functions to get the real-time currency exchange rates etc
# Based on # https://www.geeksforgeeks.org/python-get-the-real-time-currency-exchange-rate/
# yaml entries needed for 
# from_currency = "BTC"
# to_currency = "NZD"
# api_key = {YOUR API KEY} - https://www.alphavantage.co/support/#api-key
#=============================================================================================================
import requests, yaml
import pandas as pd
#============================================================================================
def ProcessYAML (yaml_file) :
    """This function opens the yaml file and returns the data objec

    Args:
        yaml_file (file): yaml file to be loaded

    Returns:
        (boolean, object): returns debug flag and the yaml object
    """
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (debug, y_data)  

# Function to get real time currency exchange ================================================================
def RealTimeCurrencyExchangeRate(api_key, from_currency, to_currency) :
    """This function returns the current exchange rate from Alphavantage.
    
    Args:
        api_key (string): your key
        from_currency (string): the crypto currency
        to_currency (string): the destination currency
    
    Returns:
        (float): A float with the current exchange rate
    """
    base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"  # base_url variable store base url
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key # main_url variable store complete url
    # get method of requests module
	# return response object
    try: 
        req_ob = requests.get(main_url)
    except requests.exceptions.RequestException as e: 
        raise SystemExit(e)
	# json method return json format data into python dictionary data type.
	# result contains list of nested dictionaries
    result = req_ob.json()
    try:
        exchange_rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    except KeyError: 
        print(f"Exception finding exchange rate for {from_currency}. Using 10 units of default currency instead.")
        exchange_rate = float(10)
    if debug == True : 
        print("Result before parsing the json data :\n", result)
        print("Realtime currency exchange rate for", result["Realtime Currency Exchange Rate"]["2. From_Currency Name"], "TO", result["Realtime Currency Exchange Rate"]["4. To_Currency Name"], "is", round(exchange_rate,2), to_currency)
    return(exchange_rate)

# Function to get monthly crypto from alphavantage ================================================================
def MonthlyCryptoPrice (api_key, crypto, market, months=24) :
    """This function loads the historic monthly crypto values from alphavantage.

    Args:
        api_key (string): your key
        crypto (string): the crypto currency
        market (string): the destination currency
        months (int, optional): Number of months, defaults to 24

    Returns:
        (dataframe): A data frame with the values of #crypto in #market for months
    """
    base_url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY"
    main_url = base_url + "&symbol=" + crypto + "&market=" + market + "&apikey=" + api_key
    req_ob = requests.get(main_url)                     #get method of requests module & return response object
    result = req_ob.json()                              #json method return json format data into python dictionary data typ & result contains list of nested dictionaries
    hc_df=pd.DataFrame.from_dict(result['Time Series (Digital Currency Monthly)'], orient="index")  # json to df       
    hc_df.index = pd.to_datetime(hc_df.index, format='%Y-%m-%d')           #https://stackoverflow.com/questions/47124440/build-pandas-dataframe-from-json-data#47560590
    hc_df.index.name = 'Date'
    hc_df['1b. open (USD)'] = hc_df['1b. open (USD)'].astype(float)
    hc_df['2b. high (USD)'] = hc_df['2b. high (USD)'].astype(float)
    hc_df['3b. low (USD)'] = hc_df['3b. low (USD)'].astype(float)
    hc_df['4b. close (USD)'] = hc_df['4b. close (USD)'].astype(float)
    hc_df['5. volume'] = hc_df['5. volume'].astype(float)
    hc_df['6. market cap (USD)'] = hc_df['6. market cap (USD)'].astype(float)
    if debug == True :
        print(hc_df[['1b. open (USD)', '4b. close (USD)']])
    return(hc_df.head(months))

# Function to get monthly crypto from alphavantage ================================================================
def DailyCryptoPrice (api_key, crypto, market, days=7) :
    """This function loads the historic daily crypto values from alphavantage.
    
    Args:
        api_key (string): your key
        crypto (string): the crypto currency
        market (string): the destination currency
        days (int, optional): Number of day, defaults to 7
    
    Returns:
        (dataframe): A data frame with the values of #crypto in #market for #days
    """
    base_url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY"
    main_url = base_url + "&symbol=" + crypto + "&market=" + market + "&apikey=" + api_key
    req_ob = requests.get(main_url)                     #get method of requests module & return response object
    result = req_ob.json()                              #json method return json format data into python dictionary data typ & result contains list of nested dictionaries
    dc_df=pd.DataFrame.from_dict(result['Time Series (Digital Currency Daily)'], orient="index")  # json to df       
    dc_df.index = pd.to_datetime(dc_df.index, format='%Y-%m-%d')           #https://stackoverflow.com/questions/47124440/build-pandas-dataframe-from-json-data#47560590
    dc_df.index.name = 'Date'
    dc_df['1b. open (USD)'] = dc_df['1b. open (USD)'].astype(float)
    dc_df['2b. high (USD)'] = dc_df['2b. high (USD)'].astype(float)
    dc_df['3b. low (USD)'] = dc_df['3b. low (USD)'].astype(float)
    dc_df['4b. close (USD)'] = dc_df['4b. close (USD)'].astype(float)
    dc_df['5. volume'] = dc_df['5. volume'].astype(float)
    dc_df['6. market cap (USD)'] = dc_df['6. market cap (USD)'].astype(float)
    if debug == True :
        print(dc_df[['1b. open (USD)', '4b. close (USD)']])
    return(dc_df.head(days))
#==============================================================================================================    
debug, yaml_data = ProcessYAML('portfolio.yaml')  