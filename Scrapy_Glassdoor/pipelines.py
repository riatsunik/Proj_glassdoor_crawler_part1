# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import CsvItemExporter
import string
from bs4 import BeautifulSoup
from string import punctuation
import unicodedata

class ProjetodsPipeline(object):
    # Create the csv file.
    def __init__(self):
        self.file = open("booksdata.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    # Process each job detail 
    def process_item(self, item, spider):
        #Clean text (punctuation)
        translator=str.maketrans('','',string.punctuation)
        item['title'] = item['title'].translate(translator)
        item['local'] = item['local'].translate(translator).replace(" – "," ")
        item['company_name'] = item['company_name'].translate(translator)
        # Remove HTML Markup
        soup = BeautifulSoup(item['description'])
        item['description'] = soup.get_text(" ", strip=True).translate(translator)
        # Treat empty field
        if item['salary'] is None :
            item['salary'] = "NA"
        else:    
            item['salary'] = item['salary'].replace(",",".")

        self.exporter.export_item(item)
        
        return item