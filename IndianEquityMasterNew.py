# DO NOT EDIT
import requests
import json
import pymongo
from dotenv import load_dotenv
import os

startOfUrl = "https://groww.in/v1/api/stocks_data/v1/company/search_id/"
endOfUrl = "?page=0&size=10"


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

mongo_uri = MONGO_URI

equitySearchIDs = []
client = pymongo.MongoClient(mongo_uri)
db = client.fortunewebapp

equityCollection = db.FortuneEquityMaster
indianEquityDetails = db.IndianEquityDetails

equityCollectionData = equityCollection.find({})
#
for document in equityCollectionData:
    equitySearchIDs.append(document['search_id'])

indianEquityDetails.drop()

for searchIDS in equitySearchIDs:
    compeleteAPIURL = startOfUrl + searchIDS + endOfUrl
    response = requests.get(compeleteAPIURL)
    data = response.json()
    result = indianEquityDetails.insert_one(data)
    if response.status_code != 200:
        print(compeleteAPIURL)       

print('Data Updated')
