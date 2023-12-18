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
collection = db.IndianEquityNews

API_URL = "https://groww.in/v1/api/groww_news/v1/stocks_news/news?1&size=20"
response = requests.get(API_URL)
data = response.json()
results = data['results']

dataToInsert=[]
for i in results:
    dataToInsert.append(i)


collection.drop()
collection.insert_many(dataToInsert)
print('Data Updated')
client.close()


