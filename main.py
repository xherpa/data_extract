from flask import Flask, jsonify, request
#from config.database_config import database_conection
#from facebook.database.querys import create_user,get_users
from facebook.extract.extract import extract_adset_data, get_data_adsets, extract_ad_id_data

app = Flask(__name__)

@app.route("/")
def hello():
    #user = create_user(name="Sebas", email="sebas@email.com", age=30)
    #print(f"Usuario creado: {user}")
    
    #users = get_users()
    #print(f"Los usuarios de la base de datos son: {users}")
    return "Hello"

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
            "Message": "data extracted success"
        }), 200
    return ""

@app.route('/adsets_data', methods=['POST'])
def get_adsets():
    if request.is_json:
        date = request.get_json()
        date_stop = date.get('date_stop')

        adsets = get_data_adsets(date_stop)
        return adsets
    return ""


@app.route('/adid_extract', methods=['POST'])
def adid_extract():
    if request.is_json:
        date = request.get_json()
        date_start = date.get('date_start')
        date_stop = date.get('date_stop')
        extract_ad_id_data(date_start, date_stop)


    return ""


if __name__ == '__main__':
    app.run(debug=True)
