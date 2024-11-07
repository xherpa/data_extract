from facebook.config.session import engine, Base
# Import all models here, to create tables in the database
from facebook.utils.database_models import Hubspot_data, Facebook_ads_data, Facebook_adset_data

Base.metadata.create_all(bind=engine)
