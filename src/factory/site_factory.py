from sites import apple

class SiteFactory:
    
    @staticmethod
    def get_all_sites():
        return [
            apple.AppleSite()
        ]