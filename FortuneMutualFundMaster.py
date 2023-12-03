# DO NOT EDIT
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
collection = db.FortuneMutualFundMaster



startOfUrl = "https://groww.in/v1/api/search/v1/derived/scheme?available_for_investment=true&doc_type=scheme&max_aum=&page="
endOfUrl = "&plan_type=Direct&q=&size=15&sort_by=3"

collection.drop()
for i in range(0,88):
    completeURL = startOfUrl + str(i) + endOfUrl

    response = requests.get(completeURL)
    data = response.json()
    content = data['content']

    # print(content)

    for i in content:
        newModel = {
        'search_id': i['search_id'],
        }
        json_string = json.dumps(newModel)
        result = collection.insert_one(newModel)
client.close()
print("Data Updated")







