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
collection = db.IndianInstruments
API_URL ='https://groww.in/v1/api/stocks_data/v1/company/search_id/nifty?fields=ALL_ASSETS&page=0&size=10'

response = requests.get(API_URL)
data = response.json()
allAssets = data['allAssets']

collection.drop()

for i in allAssets:
    result = collection.insert_one(i)

client.close()
print("Data Updated")








