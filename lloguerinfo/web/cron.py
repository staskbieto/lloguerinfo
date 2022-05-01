from scrapy.utils.project import get_project_settings

from scrapyd_api import ScrapydAPI

def run_scrapy_fotocasa(scrapyd_url= 'http://localhost:6800'):
    scrapyd = ScrapydAPI(scrapyd_url)
    scrapyd.schedule('default', 'fotocasa_flats', settings=get_project_settings())