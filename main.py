from flask import Flask, jsonify, request
#from config.database_config import database_conection
#from facebook.database.querys import create_user,get_users
from facebook.extract.extract import extract_adset_data

app = Flask(__name__)

@app.route("/")
def hello():
    #user = create_user(name="Sebas", email="sebas@email.com", age=30)
    #print(f"Usuario creado: {user}")

    #users = get_users()
    #print(f"Los usuarios de la base de datos son: {users}")
    extract_adset_data()
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)
