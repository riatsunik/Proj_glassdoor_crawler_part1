# -*- coding: utf-8 -*-
'''
Spider responsible for interacting and capturing information on data-science jobs.
The Glassdoor website does not allow it to be followed by robots, this must be respected. For 
educational purposes I configured the robot to ignore this mark, but I do not recommend it.
In settings.py 
set ROBOTSTXT_OBEY = False
'''
import scrapy
from scrapy_splash import SplashRequest

class GlassdoorSpider(scrapy.Spider):
    name = 'glassdoor'
    allowed_domains = ['glassdoor.com']
    start_urls = ['https://www.glassdoor.com/Job/us-data-scientist-jobs-SRCH_IL.0,2_IN1_KO3,17.htm']
    
    # Interaction for process each url
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.1},
            )

    # Get Job List       
    def parse(self, response):
        items = response.xpath("//*[contains(@class, 'jlGrid hover')]/li")

        # Interaction for each job
        for item in items:
            url = item.xpath(".//div[contains(@class,'logoWrap')]/a/@href").extract_first()
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_detail)
                
        next_page = response.xpath(".//li[contains(@class, 'next')]/a/@href").extract_first()
        # Condition to next page
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url=url, callback=self.parse)
    
    # Get job details
    def parse_detail(self, response):     
        yield {
            'title': response.xpath("//h2[contains(@class, 'noMargTop margBotXs strong')]/text()").extract_first(),
            'local': response.xpath("//span[contains(@class, 'subtle ib')]/text()").extract_first(),
            'company_name' : response.xpath("//span[contains(@class, 'strong ib')]/text()").extract_first(),
            'salary' : response.xpath("//h2[contains(@class, 'salEst')]/text()").extract_first(),
            'description' : response.xpath("//div[contains(@class, 'jobDescriptionContent desc module pad')]").extract_first()
        }   
