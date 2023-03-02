import scrapy
from scrapy_selenium.http import SeleniumRequest
from scrapy.selector.unified import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime

class DotDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class MySpider(scrapy.Spider):
    name = 'mySpider'
    allowed_domains = ['cwb.gov.tw']
    start_urls = ['https://www.cwb.gov.tw/V8/C/W/OBS_Map.html']
    _config = {
        'each_country_row': '#town li',
        'city_name': 'span.city',
        'temperature': 'span.tem-C i'
    }
    config = DotDict(_config)
    output_path = f'output_{name.lower()}.txt'

    def start_requests(self):
        self.writelines(f'Start {self.name} ...')
        request = SeleniumRequest(url = self.start_urls[0], callback = self.parse, dont_filter=True)
        yield  request

    def writelines(self, string):
        open(self.output_path, 'a').write(f"[{datetime.datetime.now()}] {string} \n")
    
    def parse(self, response):
        self.driver = response.meta['driver']
        self.driver.get(response.url)

        cities = self.driver.find_elements(By.CSS_SELECTOR, self.config.each_country_row)
        self.writelines(f'the number of cities: {len(cities)}')
        
        for _city in cities:
            city = _city.find_element(By.CSS_SELECTOR, self.config.city_name).text
            temp = _city.find_element(By.CSS_SELECTOR, self.config.temperature).text
            self.writelines(f'{city}: {temp}')
        self.driver.close()

    def closed(self, reason):
        self.writelines(f'End {self.name}')
        self.driver.quit()