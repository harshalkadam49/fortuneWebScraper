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
collection = db.IndianEquityTopLosersNew
API_URL ='https://groww.in/v1/api/stocks_data/explore/v2/indices/GIDXNIFTY500/market_trends?discovery_filter_types=TOP_LOSERS&size=30'

collection.drop()
response = requests.get(API_URL)
data = response.json()
itemsArray = data['categoryResponseMap']['TOP_LOSERS']['items']

dataToInsert=[]
for i in itemsArray:
    dataToInsert.append(i)

collection.drop()
collection.insert_many(dataToInsert)
print('Data Updated')
client.close()









