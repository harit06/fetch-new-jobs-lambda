from filter.filter import Filter 

class DateFilter(Filter):
    def __init__(self, date):
        self.date = date
    def apply_filter(self, job):
        if not job.updated_date:
            return job.posted_date.date() == self.date
        return job.posted_date.date() == self.date or job.updated_date.date() == self.date