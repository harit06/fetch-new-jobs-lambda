from abstractsites.postrequest import PostRequestSite
from util.constants import Constants

class AppleSite(PostRequestSite):
  def __init__(self):
    url = 'https://jobs.apple.com/api/role/search'
    body = {
        "query": "Software",
        "filters": {
            "postingpostLocation": ["postLocation-USA"],
            "range": {
                "standardWeeklyHours": {
                    "start": None,
                    "end": None
                }
            }
        },
        "page": 1,
        "locale": "en-us",
        "sort": "newest"
    }
    headers = {
        "Content-Type": "application/json"
    }
    company = Constants.COMPANY_NAME_APPLE
    mapper = AppleJobsMapper()
    link = 'https://jobs.apple.com/en-us/details/'
    super().__init__(url, body,company, mapper, link=link, headers=headers)

 

class AppleJobsMapper:
  job_path = 'searchResults'
  
  def __init__(self):
      self.job_title = 'postingTitle'
      self.link = 'positionId'
      self.posted_date = 'postingDate'