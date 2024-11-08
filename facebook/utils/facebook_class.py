from datetime import date
from sqlalchemy import insert, select
import  json
from facebook.database.create_session import get_db
from facebook.utils.database_models import Facebook_adset_data

class Adsets_facebook:
    def insert_data (self, page, id_page, name_adset, daily_budget, id_adset, date_start, date_stop):
        self.page = page
        self.id_page = id_page
        self.name_adset = name_adset
        self.daily_budget = daily_budget
        self.id_adset = id_adset
        self.date_start = date_start
        self.date_stop = date_stop
        
        db = next(get_db()) # Create Session
        new_adset = Facebook_adset_data(page= self.page, name=self.name_adset, id_page=self.id_page, daily_budget=self.daily_budget, adset_id=self.id_adset, date_start=self.date_start, date_stop=self.date_stop)
        db.add(new_adset) # Add data to stage
        db.commit() # Transaction comfirm
        db.refresh(new_adset) # Refresh state of new_adset
        return new_adset

    def get_data(self, date_stop_query):
        db = next(get_db())
        query = select(Facebook_adset_data).where(Facebook_adset_data.date_stop == date_stop_query).order_by(Facebook_adset_data.page)
        results = db.execute(query).scalars().all()

    # Convertir los resultados a JSON-friendly data
        data_list = []
        for result in results:
            result_dict = {column.name: getattr(result, column.name) for column in result.__table__.columns}

            # Convertir fechas a string
            for key, value in result_dict.items():
                if isinstance(value, date):
                    result_dict[key] = value.isoformat()  # Convierte la fecha a formato string ISO (YYYY-MM-DD)

            data_list.append(result_dict)
        
        adset_data =  json.dumps(data_list, indent=4)
        return adset_data

