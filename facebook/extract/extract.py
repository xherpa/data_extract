from datetime import datetime
import json
from os import walk
import urllib.parse
import requests
import pandas as pd
from sqlalchemy import except_
from facebook.config.config import FACEBOOK_TOKEN, ID_PRINCIPAL_ACCOUNT
from facebook.utils.facebook_class import Adsets_facebook


# ---------------------------------------------------------------------------------------
# ---------------------           ADSET ID EXTRACT           ----------------------------
# ---------------------------------------------------------------------------------------

def extract_adset_data (date_start, date_stop):
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
                    info = Adsets_facebook()
                    info.insert_data(page=data["page"], id_page=data["id_page"], name_adset=data["name"], daily_budget=data["daily_budget"],id_adset=data["id"], date_stop=date_stop, date_start=date_start)
                except:
                    print("Data is exist or not have daily budget")


def get_data_adsets (date_stop):
    data = Adsets_facebook()
    return data.get_data(date_stop)


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------
# -------------------              AD ID EXTRACT              ---------------------------
# ---------------------------------------------------------------------------------------

def extract_ad_id_data (date_start, date_stop):
    #date_start = datetime.strptime(date_start, "%Y-%m-%d")
    #date_stop = datetime.strptime(date_stop, "%Y-%m-%d")

    # Fields to extrac in facebook
    fields = 'spend,reach,frequency,ad_id,ad_name,impressions,cpm,ctr,adset_id, actions'
    time_increment = 'all_days'
    date_range = {
        "since": date_start,
        "until": date_stop
    }

    print(date_range)
    increment = '90'
    level = 'ad'


    ids_adsets = get_data_adsets(date_stop)
    data = pd.read_json(ids_adsets)
    dict_data = data.to_dict(orient="records")
    ids_data = []
    for id_page in dict_data:
        id_page['id_page']
        
        url = (
            f"https://graph.facebook.com/v20.0/{id_page['id_page']}/insights"
            f"?level={level}&fields={fields}"
            f"&time_range={{\"since\":\"{date_range['since']}\",\"until\":\"{date_range['until']}\"}}"
            f"&time_increment={time_increment}&access_token={FACEBOOK_TOKEN}"
        )

        encoded_url = urllib.parse.quote(url, safe=':/?&=')
        response = requests.get(encoded_url)
        
        ad_ids = response.json()
        for ad_id in ad_ids["data"]:
            #print(ad_id["actions"])
            try:
                for results in ad_id["actions"]:
                    if results["action_type"] == 'onsite_conversion.messaging_conversation_started_7d':
                        ad_id_result = results["value"]
                        ad_id.update({'results': ad_id_result})
                ids_data.append(ad_id)
            except:
                #print("")
                ids_data.append(ad_id)


    df = pd.DataFrame(ids_data)
    print(df.dropna())
    print(df)



# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

