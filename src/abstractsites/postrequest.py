import requests
from abstractsites.site import Site
import json

class PostRequestSite(Site):
  def __init__(self, url, body, company, mapper, params = {}, headers={}, link=''):
    self.body = body
    super().__init__(url, params, headers, company, mapper, link)

  def fetch_jobs(self):
    response = requests.post(self.url, headers=self.headers, data=json.dumps(self.body))
    data = None
    if response.status_code == 200:
      data = response.json()
    else:
      print(f"Failed to get data for {self.company}: {response.status_code}")
    return data