class Constants: 
    FILTER_TYPE_DATE_FILTER     = 'Date_Filter'
    
    COMPANY_NAME_AMAZON         = 'Amazon'
    COMPANY_NAME_APPLE          = 'Apple'
    COMPANY_NAME_MICROSOFT      = 'Microsoft'
    COMPANY_NAME_JP_MORGAN      = 'JP Morgan Chase'
    COMPANY_NAME_CHEWY          = 'Chewy'
    COMPANY_NAME_NETFLIX        = 'Netflix'
    COMPANY_NAME_UBER           = 'Uber'
    COMPANY_NAME_TMOBILE        = 'Tmobile'
    COMPANY_NAME_AMEX           = 'AMEX'
    COMPANY_NAME_ORCALE         = 'Oracle'
    COMPANY_NAME_BNY            = 'BNY'
    COMPANY_NAME_PAYPAL         = 'Paypal'
    COMPANY_NAME_MILLINIUM      = 'Millinium'
    COMPANY_NAME_DEFAULT        = 'DEFAULT'
    
    DATE_FORMAT_AMAZON          = '%B %d, %Y'
    DATE_FORMAT_APPLE           = '%b %d, %Y'
    DATE_FORMAT_TIMESTAMP_WO_MS = '%Y-%m-%dT%H:%M:%S%z'
    DATE_FORMAT_TIMESTAMP       = '%Y-%m-%dT%H:%M:%S.%f%z'
    DATE_FORMAT_DATE            = '%Y-%m-%d'
    
    COMPANIES_DATE_FORMAT_MAP = {
        COMPANY_NAME_AMAZON         :DATE_FORMAT_AMAZON,
        COMPANY_NAME_APPLE          :DATE_FORMAT_APPLE,
        COMPANY_NAME_MICROSOFT      :DATE_FORMAT_TIMESTAMP_WO_MS, 
        COMPANY_NAME_JP_MORGAN      :DATE_FORMAT_DATE,
        COMPANY_NAME_DEFAULT        :DATE_FORMAT_TIMESTAMP,
        COMPANY_NAME_ORCALE         :DATE_FORMAT_DATE,
        COMPANY_NAME_BNY            :DATE_FORMAT_DATE
    }