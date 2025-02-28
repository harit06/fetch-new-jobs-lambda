from util.constants import Constants
from filter.date_filter import DateFilter

class FiltersFactorySingleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FiltersFactorySingleton, cls).__new__(cls)
            cls._instance.__filters = cls.__register_all_filters()
        return cls._instance

    @classmethod
    def __register_all_filters(cls):
        filters = Filters()

        return filters

    def get_filter(self, company, filter_type, value):
        return self.__filters.get_filter(company, filter_type, value)



class Filters:
    def __init__(self):
        self.__registered_filters = {}

    def register_filter(self, company, filter_type, filter_class, value):
        if company not in self.__registered_filters:
            self.__registered_filters[company] = {}
        if filter_type not in self.__registered_filters[company]:
            self.__registered_filters[company][filter_type] = {}
        self.__registered_filters[company][filter_type][value] = filter_class(value)
        return self.__registered_filters[company][filter_type][value]

    def get_filter(self, company, filter_type, value):
        filter_class = self.__registered_filters.get(company, {}).get(filter_type, {}).get(value, None)
        filter_class = filter_class if filter_class is not None else self.register_filter('default', filter_type, self.__get_default_filter(filter_type), value)
        return filter_class

    def __get_default_filter(self, filter_type):
        if filter_type == Constants.FILTER_TYPE_DATE_FILTER:
            return DateFilter
        raise ValueError(f"No default filter available for filter type {filter_type}")