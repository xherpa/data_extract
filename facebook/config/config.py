from dotenv import load_dotenv
import os

load_dotenv()

# Credential DataBase in case you want use SQL sentences
HOST = os.getenv("HOST")
USER_DATABASE = os.getenv("USER_DATABASE")
DATABASE = os.getenv("DATABASE")
PASSWORD = os.getenv("PASSWORD")
PORT_DB = int(os.getenv("PORT_DB",5432))

# URL credentials in case you want use a ORM
URL_DATABASE = str(os.getenv("URL_DATABASE"))

# Credentials Facebook
ID_PRINCIPAL_ACCOUNT = os.getenv("ID_PRINCIPAL_ACCOUNT")
FACEBOOK_TOKEN = os.getenv("FACEBOOK_TOKEN")


# Credentials Hubspot
HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")
