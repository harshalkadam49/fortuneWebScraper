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

collection.drop()
API_URL = "https://groww.in/v1/api/groww_news/v1/stocks_news/news?1&size=20"
response = requests.get(API_URL)
data = response.json()
results = data['results']

for i in results:
    result = collection.insert_one(i)
client.close()
print("Data Updated")



