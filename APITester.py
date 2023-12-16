import requests
import json
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

mongo_uri = MONGO_URI
client = pymongo.MongoClient(mongo_uri)
db = client.fortunewebapp
collection = db.test2

collection.drop()
API_URL = "https://groww.in/v1/api/charting_service/v2/chart/exchange/NSE/segment/CASH/ICICIBANK/daily?intervalInMinutes=1&minimal=true"
response = requests.get(API_URL)
data = response.json()
cnadles = data["candles"]
# print(cnadles)
# collection.insert_one(data)
# for i in results:
#     result = collection.insert_one(i)
# client.close()
# print("Data Updated")

prices = []
for i in cnadles:
   prices.append(i[1])


print(prices)



