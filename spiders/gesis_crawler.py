# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:13:45 2020

@author: Tara
"""


            
from scrapy.spiders import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
import ast
import pandas as pd
import json
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError
#from scrapy.spidermiddlewares.httperror import HttpError
from random import randint
from scrapy import signals
class CustomerSpider(Spider):
    #list of possible failure status codes
    #handle_httpstatus_all=True
    handle_httpstatus_list = [400,401,403,404,408,410,408,451,500,502,503,501,504] 
    
    name= 'gesis'
    page_counter=200
    failed_urls=[]
    crawled_urls=[]
    
    
           
    def start_requests(self):
        for url in self.root_urls:
            
            yield Request(url, meta={'root_url': url,'err_flag':True}, dont_filter=True,
                          errback=self.error_handler)
            
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(CustomerSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
       
        return spider


    def spider_closed(self, spider):
        with open('failed_urls_'+country+'.json', 'w') as f1:
            json_failed_urls = json.dumps(self.failed_urls)
            f1.write(json_failed_urls)
        with open('crawled_urls_'+country+'.json', 'w') as f2:
            json_crawled_urls= json.dumps(self.crawled_urls)
            f2.write(json_crawled_urls)
        spider.logger.info('finished---------------------')
        

    def error_handler(self,failure):
        
        request = failure.request
        
        if failure.check(TimeoutError):
           
            self.failed_urls.append({'original_url':request.meta['root_url'],
                                      'url':request.url,
                                      'status':'TimeoutError'})
        elif failure.check(DNSLookupError):
            
            self.failed_urls.append({'original_url':request.meta['root_url'],
                                      'url':request.url,
                                      'status':'DNSLookupError'})
        else:
            self.failed_urls.append({'original_url':request.meta['root_url'],
                                      'url':request.url,
                                      'status':'Genaral error'})
            
    def http_error(self,response):
       user_agents=['Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
                    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)',
                    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                    'Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                    ]
       
       index = randint(0, 20)
       ua=user_agents[index]
       
       headers= {'User-Agent': ua}
       if response.meta['err_flag']==True:
           
           yield Request(response.url, meta={'root_url':response.meta['root_url'],'err_flag':False }, dont_filter=True, headers=headers)
  
       
        
    def parse(self, response):
        
           
        
        if response.status!=200 and response.meta['err_flag']:
            
            return Request(response.url, meta={'root_url':response.meta['root_url'] ,'err_flag':True }, dont_filter=True,callback=self.http_error)


        
            
        if response.status== 200: 
            filename = 'page-'+str(self.page_counter)+'.html'             
            with open(country+'/'+filename, 'wb') as f:
               
                f.write(response.body)

            self.crawled_urls.append({'original_url':response.meta['root_url'],
                                      'url':response.url,
                                      'file':self.page_counter})
            self.page_counter+=1
     
        else:
#           
           self.failed_urls.append({'original_url':response.meta['root_url'],
                                      'url':response.url,
                                      'status':response.status})
        


#
country='de'

with open('C:/Users/Tara/Desktop/html_parser/missings/missings-'+country+'.json','r') as f:
    missings=f.read()
    urls=ast.literal_eval(ast.literal_eval(missings))

urls=list(set(urls))
urls=['http://'+s for s in urls]

####reading a wapo file
#urls=[]
#with open(country+".txt",'r') as f:
#    for item in f:
#        # remove linebreak which is the last character of the string
#        url = item[:-1]
#        # add item to the list
#        urls.append(url)


a = CustomerSpider
process = CrawlerProcess()

process.crawl(a, root_urls=urls)
process.start()

