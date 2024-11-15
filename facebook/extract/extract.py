import json
import urllib.parse
import locale
import requests
import pandas as pd
from facebook.config.config import FACEBOOK_TOKEN, ID_PRINCIPAL_ACCOUNT
from facebook.utils.facebook_class import Adsets_facebook,Ad_Id_facebook


# ---------------------------------------------------------------------------------------
# ---------------------           ADSET ID EXTRACT           ----------------------------
# ---------------------------------------------------------------------------------------

def extract_adset_data (date_start, date_stop):
    # Fields to extrac in facebook
    fields = 'name,id,adsets.limit(9999){name,daily_budget}'

    # URL struct to perform the extraccion
    adset_url = f"https://graph.facebook.com/v20.0/{ID_PRINCIPAL_ACCOUNT}/owned_ad_accounts?fields={fields}&access_token={FACEBOOK_TOKEN}"

    # Filter pages
    pages = ['Frontier Services', 'Windstream Internet', 'Internet Services', 'Wireless Services', 'Home Services', 'Xmart Fi', 'AT&T Dealer']
    response = requests.get(adset_url)
    data_json = response.json()

    # Scroll through the data with a For
    for data in data_json["data"]:

        # Save page and id page in variables
        page = data["name"]
        id_page = data["id"]

        if page  in pages:
            adsets_data = data['adsets']
            data_insert = []

            for data_adset in adsets_data['data']:
                # Adds fields in JSON structure
                data_adset.update({'page':page,'id_page':id_page, 'date_start':date_start, 'date_stop':date_stop})
                data_insert.append(data_adset)
            # Read JSON and convert to Data Frame
            adsets = pd.json_normalize(data_insert)
            df = pd.DataFrame(adsets)
            print(df)
            df_not_na = df.fillna(0)
            data_dict = df_not_na.to_dict(orient="records")
            print(json.dumps(data_dict, indent=4))

            # Realice bulk to data base
            try:
                info = Adsets_facebook()
                info.insert_data(data_dict)
            except Exception as e :
                print(e)


def get_data_adsets (date_stop):
    data = Adsets_facebook()
    return data.get_data(date_stop)


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------
# -------------------              AD ID EXTRACT              ---------------------------
# ---------------------------------------------------------------------------------------

def extract_ad_id_data (date_start, date_stop):

    # Fields to extrac in facebook
    fields = 'spend,reach,frequency,ad_id,ad_name,impressions,cpm,ctr,adset_id, actions'
    time_increment = 'all_days'
    date_range = {
        "since": date_start,
        "until": date_stop
    }

    # Level to we need extract data to facebook, in this case use ad (ad, adset, campaing)
    level = 'ad'

    # Call the function to get info to db and use the ID Page, to extract data.
    ids_adsets = get_data_adsets(date_stop)
    ids_adsets_dictionary = json.loads(ids_adsets)
    ids_results = []
    ids_not_results = []

    # Scroll through with For
    for id_page in ids_adsets_dictionary:

        # Create the URL with parameters
        url = (
            f"https://graph.facebook.com/v20.0/{id_page['adset_id']}/insights"
            f"?level={level}&fields={fields}"
            f"&time_range={{\"since\":\"{date_range['since']}\",\"until\":\"{date_range['until']}\"}}"
            f"&time_increment={time_increment}&access_token={FACEBOOK_TOKEN}"
        )

        # Encode  the URL
        encoded_url = urllib.parse.quote(url, safe=':/?&=')
        response = requests.get(encoded_url)

        # Define the local currency transform in this case US to convert to Dollar
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        ad_ids = response.json()

        for ad_id in ad_ids["data"]:
            try:
                # Conditional that iterates each of the actions in each ad_id and waits for the condition to be met
                if any(result["action_type"] == 'onsite_conversion.messaging_conversation_started_7d' for result in ad_id["actions"]):

                    # The value of the result is extracted by iterating each ad_id, as long as the conditional is fulfilled.
                    ad_id_result = next(result["value"] for result in ad_id["actions"] if result ["action_type"] == "onsite_conversion.messaging_conversation_started_7d")
                    cost_per_result = float(ad_id["spend"]) / float(ad_id_result)

                    # Ad aditional data in JSON object
                    ad_id.update(
                        {'results': ad_id_result,
                        'cost_per_result': cost_per_result,
                        'adset_budget': id_page['daily_budget'],
                        'page': id_page['page']
                        })

                    ids_results.append(ad_id)

                else:
                    # If the conditional is not met, a vale of zero is added
                    ad_id.update(
                        {'results': 0,
                        'cost_per_result': 0,
                        'adset_budget': id_page['daily_budget'],
                        'page': id_page['page']
                        })

                    ids_results.append(ad_id)

            except KeyError:
                # In case the ad id don't contain actions, a value of zero is added
                ad_id.update(
                    {'results': 0,
                    'cost_per_result': 0,
                    'adset_budget': id_page['daily_budget'],
                    'page': id_page['page']
                    })

                ids_results.append(ad_id)


    # Cretae dataframe
    df = pd.DataFrame(ids_results)

    # Delete fields
    df.pop('actions')

    # Transform numeric data in currency US
    df['cost_per_result'] = df['cost_per_result'].map(lambda x: locale.currency(x, grouping=True))
    df['adset_budget'] = df['adset_budget'].map(lambda x: locale.currency(x, grouping=True))

    #Transform string data in numeric to change in currency data
    df['cpm'] = pd.to_numeric(df['cpm'])
    df['cpm'] = df['cpm'].map(lambda x: locale.currency(x, grouping=True))
    df['spend'] = pd.to_numeric(df['spend'])
    df['spend'] = df['spend'].map(lambda x: locale.currency(x, grouping=True))

    # Transform dataframe in a dictionary, and later transform in JSON object
    json_data = df.to_dict(orient="records")
    print(json.dumps(json_data, indent=4))
    try:
        info = Ad_Id_facebook()
        info.insert_data(json_data)

    except Exception as e:
        print(f"error: {e}")

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
