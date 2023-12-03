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
collection = db.GlobalInstruments
API_URL ='https://groww.in/v1/api/stocks_data/v1/global_instruments?instrumentType=GLOBAL_INSTRUMENTS'

response = requests.get(API_URL)
data = response.json()


aggregatedGlobalInstrumentDto = data['aggregatedGlobalInstrumentDto']
collection.drop()

for i in aggregatedGlobalInstrumentDto:
    result = collection.insert_one(i)


client.close()
print("Data Updated")
