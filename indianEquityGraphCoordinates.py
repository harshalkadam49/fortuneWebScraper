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
IndianEquityGraphCoordinates = db.IndianEquityGraphCoordinates

FortuneEquityMaster = db.FortuneEquityMaster
EquityLivePrices = db.EquityLivePrices

equitySymbols = ["VICEROY","VIVIMEDLAB","ZICOM"]

FortuneEquityMaster = FortuneEquityMaster.find({"isActive":1})

for document in FortuneEquityMaster:
    equitySymbols.append(document['Symbol'])
    # print(document['Symbol'])
   
   
   
StartofURL = "https://groww.in/v1/api/charting_service/v2/chart/exchange/NSE/segment/CASH/"
parameter = ""
endOfURL = "/daily?intervalInMinutes=1&minimal=true"
for symbol in equitySymbols:
   compeleteAPIURL =  StartofURL+ symbol +endOfURL
   response = requests.get(compeleteAPIURL)
   data = response.json()
   cnadles = data["candles"]
   print(compeleteAPIURL)
   
   

dataToInsert = []

for i in cnadles:
   dataToInsert.append(i[1])

# IndianEquityGraphCoordinates.drop()
# IndianEquityGraphCoordinates.insert_many(dataToInsert)
# print('Data Updated')
# client.close()


