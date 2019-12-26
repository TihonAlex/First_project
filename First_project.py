import requests

url = "https://www.xe.com/currencyconverter/"
response = requests.get(url)
print(response)