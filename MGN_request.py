import requests
import json


def req_api_auchan(name):
  search = requests.get(f"https://autocomplete.diginetica.net/autocomplete?st={name}&apiKey=06U4652632&strategy=vectors_extended%2Czero_queries&productsSize=100&regionId=1&forIs=true&showUnavailable=true&withContent=false&withSku=false").json()
  product_id = search['products'][0]['id']
  product_json = requests.get(f"https://api.retailrocket.ru/api/1.0/partner/5ecce55697a525075c900196/items/?itemsIds={product_id}&stock=1&format=json").json()
  return product_json

product_name = 'молочный шоколад milka'
product = req_api_auchan(product_name)


print(product[0]['Name'])
print(product[0]['Price'])