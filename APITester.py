# DO NOT EDIT
import requests
import json
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# startOfUrl = "https://groww.in/v1/api/stocks_data/v1/company/search_id/"
# endOfUrl = "?page=0&size=10"
#
# equitySearchIDs = []
# mongo_uri = "mongodb+srv://fortune:letsbuildfortune@fortune.alrip3a.mongodb.net/fortunewebapp?retryWrites=true&w=majority"
# client = pymongo.MongoClient(mongo_uri)
# db = client.fortunewebapp
#
# equityCollection = db.FortuneEquityMaster
# equityDetailsCollection = db.IndianEquityDetails
#
# equityCollectionData = equityCollection.find({})
# equityDetailsCollectionData = equityDetailsCollection.find({})
#
# for document in equityDetailsCollectionData:
#     print(document)
#     # equitySearchIDs.append(document['search_id'])
#
#
# # for searchIDS in equitySearchIDs:
