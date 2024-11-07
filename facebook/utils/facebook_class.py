from sqlalchemy import insert, select
from facebook.database.create_session import get_db
from facebook.utils.database_models import Facebook_adset_data

class Adsets_facebook:
    def __init__(self, page, id_page, name_adset, daily_budget, id_adset, date_start, date_stop) -> None:
        self.page = page
        self.id_page = id_page
        self.name_adset = name_adset
        self.daily_budget = daily_budget
        self.id_adset = id_adset
        self.date_start = date_start
        self.date_stop = date_stop

    def insert_data (self):
        db = next(get_db()) # Create Session
        new_adset = Facebook_adset_data(page= self.page, name=self.name_adset, id_page=self.id_page, daily_budget=self.daily_budget, adset_id=self.id_adset, date_start=self.date_start, date_stop=self.date_stop)
        db.add(new_adset) # Add data to stage
        db.commit() # Transaction comfirm
        db.refresh(new_adset) # Refresh state of new_adset
        return new_adset

    def get_data(self):
        db = next(get_db())
        return db.query(Facebook_adset_data).all()


