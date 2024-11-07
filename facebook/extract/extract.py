import json
import requests
import pandas as pd
from sqlalchemy import except_
from facebook.config.config import FACEBOOK_TOKEN, ID_PRINCIPAL_ACCOUNT
from facebook.utils.facebook_class import Adsets_facebook

def extract_adset_data ():
    # Fields to extrac in facebook
    fields = 'name,id,adsets{name,daily_budget}'

    # URL struct to perform the extraccion
    adset_url = f"https://graph.facebook.com/v20.0/{ID_PRINCIPAL_ACCOUNT}/owned_ad_accounts?fields={fields}&access_token={FACEBOOK_TOKEN}"

    # Filter pages
    pages = ['Frontier Services', 'Windstream Internet', 'Internet Services', 'Wireless Services', 'Home Services', 'Xmart Fi', 'AT&T Dealer']
    response = requests.get(adset_url)
    data_json = response.json()

    for data in data_json["data"]:
        page = data["name"]
        id_page = data["id"]

        if page  in pages:
            adsets_data = data['adsets']
            data_insert = []

            for data_adset in adsets_data['data']:
                # Adds fields in JSON structure
                data_adset.update({'page':page,'id_page':id_page})
                data_insert.append(data_adset)

            adsets = pd.json_normalize(data_insert)
            df = pd.DataFrame(adsets)
            df_depured = df.fillna({
                "daily_budget": 0
            })

            # Type the structure to create the dictionary
            json_data = df_depured.to_dict(orient="records")
            
            # Format JSON
            format_json = json.dumps(json_data,indent=4)

            #
            for data in data_insert:
                try:
                    info = Adsets_facebook(page=data["page"], id_page=data["id_page"], name_adset=data["name"], daily_budget=data["daily_budget"],id_adset=data["id"], date_stop='2024-11-11', date_start='2024-11-01')
                    info.insert_data()
                except:
                    print("Data is exist or not have daily budget")
