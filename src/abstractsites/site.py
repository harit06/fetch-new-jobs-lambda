from abc import ABC, abstractmethod
import requests

class Site(ABC):
  def __init__(self, url, params, headers, company, mapper, link):
    self.__url = url
    self.__params = params
    self.__headers = headers
    self.__company = company
    self.__job_mapper = mapper
    self.__job_link = link
  
  @abstractmethod
  def fetch_jobs(self):
    pass
  
  '''-------------------------------Getters----------------------------------'''
  @property
  def url(self):
    return self.__url
  
  @property
  def params(self):
    return self.__params
  
  @property
  def headers(self):
    return self.__headers
  
  @property
  def company(self):
    return self.__company
  
  @property
  def mapper(self):
    return self.__job_mapper
  
  @property
  def job_link(self):
    return self.__job_link