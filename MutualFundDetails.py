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
collection = db.MutualFundMaster

allMFFundNames = []
MFcollections = db.FortuneMutualFundMaster
MFcollectionsdata = MFcollections.find({})

for MFNames in MFcollectionsdata:
    allMFFundNames.append(MFNames['search_id'])

startOfUrl = "https://groww.in/v1/api/data/mf/web/v2/scheme/search/"
endOfUrl = "?include_swp_frequency=false"


dataToInsert=[]

for fundNames in allMFFundNames:
    compeleteAPIURL = startOfUrl + fundNames + endOfUrl
    response = requests.get(compeleteAPIURL)
    data = response.json()

    print(compeleteAPIURL)
    # //dummy
    newModel = {
        'search_id':data['search_id'],
        "meta_title": data["meta_title"],
        "meta_desc": data["meta_desc"],
        "amc": data["meta_desc"],
        "scheme_code": data["scheme_code"],
        "direct_scheme_code": data["direct_scheme_code"],
        "regular_search_id": data["regular_search_id"],
        "scheme_name": data["scheme_name"],
        "registrar_agent": data["registrar_agent"],
        "min_investment_amount": data["min_investment_amount"],
        "fund_house": data["fund_house"],
        "fund_manager": data["fund_manager"],
        "launch_date": data["launch_date"],
        "mini_additional_investment": data["mini_additional_investment"],
        "groww_rating": data["groww_rating"],
        "category": data["category"],
        "rta_scheme_code": data["rta_scheme_code"],
        "exit_load": data["exit_load"],
        "sub_category": data["sub_category"],
        "description": data["description"],
        "aum": data["aum"],
        "super_category": data["super_category"],
        "min_sip_investment": data["min_sip_investment"],
        "min_withdrawal": data["min_withdrawal"],
        "max_sip_investment": data["max_sip_investment"],
        "available_for_investment": data["available_for_investment"],
        "analysis": data["analysis"],
        "amc_info": data["amc_info"],
        "stats": data["stats"],
        "return_stats": data["return_stats"],
        "sip_allowed": data["sip_allowed"],
        "lumpsum_allowed": data["lumpsum_allowed"],
        "plan_type": data["plan_type"],
        "scheme_type": data["scheme_type"],
        "logo_url": data["logo_url"],
        "sid_url": data["sid_url"],
        "amc_page_url": data["amc_page_url"],
        "isin": data["isin"],
        "scheme_code": data["groww_scheme_code"],
        "sip_return": data["sip_return"],
        "plan_type": data["plan_type"],
        "nav":data["nav"],
        "nav_date":data["nav_date"],
        'holdings':data["holdings"]
        }
    dataToInsert.append(newModel)


collection.drop()
collection.insert_many(dataToInsert)
print('Data Updated')
client.close()







