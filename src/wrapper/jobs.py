class Jobs:
    def __init__(self, company, link='failed to get link', job_title = 'no job title', posted_date= 'no posted date', location = "USA", extras = "Not Available", updated_date = None):
        
        self.job_title = job_title
        self.posted_date = posted_date
        self.updated_date = updated_date
        self.link = link
        self.location = location
        self.extras = extras
        self.company = company
    
    def __setitem__(self, key, value):
        setattr(self, key, value)
    def __hash__(self):
        return hash((self.link, self.job_title, self.posted_date))
    def __eq__(self, other):
        return (self.link, self.job_title, self.posted_date) == (other.link, other.job_title, other.posted_date)
    def __str__(self):
        return f"Link: {self.link}\tJob Title: {self.job_title}\tPosted Date: {self.posted_date}\tLocation: {self.location}\tDesc: {self.extras}\n"
    def __repr__(self):
            return f"Jobs(job_title={self.job_title!r}, link={self.link!r}, posted_date={self.posted_date!r} , location={self.location}, desc={self.extras}, company={self.company}, updated_date={self.updated_date}) \n"