from flask import Flask, jsonify, request
from facebook.extract.extract import extract_adset_data, get_data_adsets, extract_ad_id_data

app = Flask(__name__)

# Endpoint to extract adsets using the Facebook API, and insert data in DB
@app.route('/adsets_extract', methods=['POST'])
def adsets_extract():
    # check the request is in JSON format
    if request.is_json:
        # Extract JSON data
        date = request.get_json()

        # Save data in variables
        date_start = date.get('date_start')
        date_stop = date.get('date_stop')

        # Call function to extract
        extract_adset_data(date_start, date_stop)
        return jsonify({
            "Message": "Data extracted success"
        }), 200
    return ""

# Endpoint to get and show data is saved in DB
@app.route('/adsets_data', methods=['POST'])
def get_adsets():
    if request.is_json:

        date = request.get_json()
        date_stop = date.get('date_stop')

        adsets = get_data_adsets(date_stop)
        return adsets
    return ""

# Endpoint to extract ads ids using the Facebook API, and insert data in DB
@app.route('/ad_id_extract', methods=['POST'])
def adid_extract():
    if request.is_json:

        date = request.get_json()
        date_start = date.get('date_start')
        date_stop = date.get('date_stop')

        extract_ad_id_data(date_start, date_stop)
        return jsonify({
            "Message": "Data extracted success"
        })
    return ""


if __name__ == '__main__':
    app.run(debug=True)
