import requests

response = requests.get("https://kpk.kss45.ru/")
print(response)
print(type(response))
print(response.sta)