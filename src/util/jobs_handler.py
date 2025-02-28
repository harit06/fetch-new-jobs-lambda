from util.constants import Constants
from datetime import datetime
class JobsHandler:
    
    @staticmethod
    def handle_dates(date_field, company):
        if isinstance(date_field, int):
            date_time_obj = datetime.fromtimestamp(date_field)
        else:
            date_time_obj = datetime.strptime(date_field, Constants.COMPANIES_DATE_FORMAT_MAP.get(company, Constants.COMPANIES_DATE_FORMAT_MAP.get(Constants.COMPANY_NAME_DEFAULT)))
        if not date_time_obj:
            raise ValueError('Date format doesnt exist for {company}')
        return date_time_obj
            