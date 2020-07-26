# -*- coding: utf-8 -*-
import scrapy
#import pandas as pd
#import openpyxl

class TableDataSpider(scrapy.Spider):
    name = 'table_data'
    
    def start_requests(self):
        allowed_domains = ['https://www.worldometers.info']
        start_urls = ['https://www.worldometers.info/coronavirus/']
    
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for row in response.xpath('//*[@id="main_table_countries_yesterday"]//tbody//tr'):
            yield {
                'countries' : row.xpath('td[1]//text()').extract_first(),
                'tot_cases' : row.xpath('td[2]//text()').extract_first(),
                'new_case' : row.xpath('td[3]//text()').extract_first(),    
                'tot_death' : row.xpath('td[4]//text()').extract_first(),    
                'new_death' : row.xpath('td[5]//text()').extract_first(),
                'tot_recover' : row.xpath('td[6]//text()').extract_first()
                }
                
# class TableDataSpider(scrapy.Spider):
#     name = 'table_data'
#     allowed_domains = ['https://www.worldometers.info']
#     start_urls = ['https://www.worldometers.info/coronavirus/']

#     def parse(self, response):
#         df = pd.DataFrame()
        
#         columns = []
#         for x in range(4):
#             #temp = pd.DataFrame()
#             column = []
#             for row in response.xpath('//*[@id="main_table_countries_today"]//tbody//tr'):
#                 data = row.xpath('td//text()')[x].extract()
#                 column.append(data)
#             columns.append(column)
        
#         df = pd.DataFrame({i:columns[i] for i in range(4)})

            
#         print(df)
#         df.to_excel("output.xlsx", sheet_name='sheet_name1')
#         #return df 
#         pass