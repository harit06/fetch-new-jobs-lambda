from factory.site_factory import SiteFactory
from wrapper.jobs import Jobs
from datetime import datetime
from factory.filter_factory import FiltersFactorySingleton
from util.constants import Constants
from util.jobs_handler import JobsHandler
from util.util import Utility
from collections import defaultdict

class Driver:
    @staticmethod
    def get_today_jobs():
        all_jobs =  Driver.__get_jobs_from_sites(SiteFactory.get_all_sites())
        filters = FiltersFactorySingleton()
        
        # DB Fetch Jobs
        all_jobs_stored = {}
        
        all_jobs_today = {}
        for company, jobs in all_jobs.items():
            today_jobs = set(filter(lambda job: filters.get_filter(job.company, Constants.FILTER_TYPE_DATE_FILTER, Utility.get_todays_date()).apply_filter(job), jobs))
            if today_jobs and len(today_jobs)>1:
                all_jobs_today[company] = today_jobs
        
        # today_jobs = set(filter(lambda job: filters.get_filter(job.company, Constants.FILTER_TYPE_DATE_FILTER, Utility.get_todays_date()).apply_filter(job), all_jobs))

        return all_jobs_today
    
    @staticmethod
    def __get_jobs_from_sites(sites):
        jobs = defaultdict(list)                                                # jobs = set()
        for site in sites:
            job_response = site.fetch_jobs()                                
            for k in site.mapper.job_path.split('.'):
                if isinstance(job_response, list):
                    job_response = job_response[0]
                job_response = job_response.get(k, {})
            jobs[site.company] = (Driver.__jobs_adapter(job_response if len(job_response)>0 else [], site.mapper, site.company, site.job_link))
            # jobs.update(set(Driver.__jobs_adapter(job_response if len(job_response)>0 else [], site.mapper, site.company, site.job_link)))
        return jobs

    @staticmethod
    def __jobs_adapter(job_list, mapper, company, job_link_prefix):  
        jobs = set()
        for job in job_list:
            j = Jobs(company)
            for key, value in mapper.__dict__.items():
                if key == 'link':
                    j[key] = job_link_prefix + str(job[value])
                elif key == 'posted_date' or key == 'updated_date':
                    j[key] = JobsHandler.handle_dates(job[value], company)
                elif key == 'extras':
                    valueList = value.split('.')
                    d={}
                    for v in valueList:
                        d[v] = job[v]
                    j[key] = d
                else:
                    j[key] = job[value]
            jobs.add(j)
        return jobs