import requests

r = requests.get('https://cex.io/api/last_price/BTC/USD')
r = requests.get('http://cex.io/api/last_price/BTC/USD')
r = requests.get('http://3.221.152.203/api/last_price/BTC/USD')
r = requests.get('https://3.221.152.203/api/last_price/BTC/USD')
r = requests.get('http://3.221.152.203:8080/api/last_price/BTC/USD')
r = requests.get('https://3.221.152.203:8080/api/last_price/BTC/USD')

print(r.json())
