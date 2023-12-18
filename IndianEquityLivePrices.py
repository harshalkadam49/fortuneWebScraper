# DO NOT EDIT
from operator import truediv
import requests
import json
import pymongo
from dotenv import load_dotenv
import os

startOfUrl = "https://groww.in/v1/api/stocks_data/v1/tr_live_prices/exchange/NSE/segment/CASH/"
parameter = 'HINDUNILVR'
endOfUrl = "/latest"

equitySymbols = []


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

mongo_uri = MONGO_URI
client = pymongo.MongoClient(mongo_uri)
db = client.fortunewebapp

FortuneEquityMaster = db.FortuneEquityMaster
EquityLivePrices = db.EquityLivePrices


FortuneEquityMaster = FortuneEquityMaster.find({"isActive":1})

for document in FortuneEquityMaster:
    equitySymbols.append(document['Symbol'])
    # print(document['Symbol'])


dataToInsert = []

for symbol in equitySymbols:
    compeleteAPIURL = startOfUrl + symbol + endOfUrl
    response = requests.get(compeleteAPIURL)
    data = response.json()
    dataToInsert.append(data)
    
EquityLivePrices.drop()
EquityLivePrices.insert_many(dataToInsert)
print('Data Updated')
client.close()











