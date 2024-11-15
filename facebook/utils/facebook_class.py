from datetime import date
from sqlalchemy import select
import  json
from  typing import List
from facebook.database.create_session import get_db
from facebook.utils.database_models import Facebook_adset_data, Facebook_ads_data

class Adsets_facebook:
    def insert_data (self, data_list: List[dict]):
        adsets = [
            Facebook_adset_data(
                page= item["page"],
                name=item["name"],
                id_page=item["id_page"],
                daily_budget=item["daily_budget"],
                adset_id=item["id"],
                date_start=item["date_start"],
                date_stop=item["date_stop"]
            )
            for item in data_list
        ]

        db = next(get_db()) # Create Session
        db.bulk_save_objects(adsets)
        db.commit() # Transaction comfirm
        return adsets

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


class Ad_Id_facebook:
    def insert_data(self, data_list: List[dict]):
        ad_ids = [
            Facebook_ads_data(
                page=item["page"],
                ad_name=item["ad_name"],
                adset_budget=item["adset_budget"],
                results=item["results"],
                cost_per_result=item["cost_per_result"],
                reach=item["reach"],
                impressions=item["impressions"],
                amount_spend=item["spend"],
                cost_per_1000_accounts_centre_accounts_reached=item["cpm"],
                ctr_all=item["ctr"],
                frequency=item["frequency"],
                ad_id=item["ad_id"],
                date_start=item["date_start"],
                date_stop=item["date_stop"]
            )
            for item in data_list
        ]
        db = next(get_db())
        db.bulk_save_objects(ad_ids)
        db.commit()
        return ad_ids


    def get_data(self, date_stop_query):
        db = next(get_db())
        query = select(Facebook_ads_data).where(Facebook_ads_data.date_stop == date_stop_query).order_by(Facebook_ads_data.page)
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
        
        ads_data =  json.dumps(data_list, indent=4)
        return ads_data


