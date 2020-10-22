from selenium import webdriver
from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):

    def __init__(self):
        self.driver = webdriver.Firefox() # Or whichever browser you want

    # Here you get the request you are making to the urls which your LinkExtractor found and use selenium to get them and return a response.
    def process_request(self, request, spider):
        self.driver.get(request.url)
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)