from sqlalchemy import Column, Date, Integer, String, Float
from facebook.config.session import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'facebook'}

    id = Column(Float, primary_key = True, index = True)
    name = Column(String, index = True)
    email = Column(String, index = True)
    age = Column(Integer)

    def __repr__(self) -> str:
        return f"<User (name = {self.name}, email = {self.email}, age = {self.age})>"


# --------------- Create tables for save the information to facebook ----------------
class Facebook_ads_data(Base):
    __tablename__ = 'ads_data'
    __table_args__ = {'schema':'facebook'}

    page = Column(String, index = True)
    ad_name = Column(String, index = True)
    ad_set_budget = Column(Float)
    results = Column(Float)
    cost_per_result = Column(Float)
    reach = Column(Float)
    impressions = Column(Float)
    amount_spend = Column(Float)
    cost_per_1000_accounts_centre_accounts_reached = Column(Float)
    ctr_all = Column(Float)
    frecuency = Column(Float)
    ad_id = Column(String, index = True, primary_key = True)
    date_start = Column(Date, index = True)
    date_stop = Column(Date, index = True, primary_key = True)

    def __repr__(self) -> str:
        return f"data added successfully ad_id: {self.ad_id} with date: {self.date_start} and {self.date_stop}"


class Facebook_adset_data(Base):
    __tablename__ = 'adset_data'
    __table_args__ = {'schema':'facebook'}

    page = Column(String, index = True)
    name = Column(String, index = True)
    id_page = Column(String, index=True)
    daily_budget = Column(Integer)
    adset_id = Column(String, index = True, primary_key = True)
    date_start = Column(Date, index =  True)
    date_stop = Column(Date, index = True, primary_key = True)


# -----------------------------------------------------------------------------------


# ---------------- Create tables for save the information to Hubspot ----------------
class Hubspot_data(Base):
    __tablename__ = 'general_data'
    __table_args__ = {'schema': 'hubspot'}

    ad_id = Column(String, index=True, primary_key=True)
    create_date = Column(Date, index=True)
    first_deal_created_date = Column(Date, index=True)
    first_credit_check_date = Column(Date, index=True)
    facebook_page = Column(String, index=True)
    internet_availability = Column(String, index=True)
    availability_grade = Column(String, index=True)
    services_sold = Column(String, index=True)
    credit_results = Column(String, index=True)
    adress =  Column(String, index=True)
    zipcode = Column(String,  index=True)
    sales_wind_front = Column(String,index=True)
    date_start = Column(Date, index=True)
    date_stop = Column(Date, index=True, primary_key=True)

    def __repr__(self) -> str:
        return f"Data added successfully ad_id: {self.ad_id} with date: {self.date_start} and {self.date_stop}"

# -----------------------------------------------------------------------------------
