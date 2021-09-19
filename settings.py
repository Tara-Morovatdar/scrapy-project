# -*- coding: utf-8 -*-

# Scrapy settings for GesisSpyder project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'GesisSpyder'

SPIDER_MODULES = ['GesisSpyder.spiders']
NEWSPIDER_MODULE = 'GesisSpyder.spiders'
###this part is by me#####
###use user agent if you want to use google bot user agent
#USER_AGENT= "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
#USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
#RETRY_HTTP_CODES = [451,500, 503, 504, 400, 403, 408]
#ROTATING_PROXY_LIST = [
#    'morovatdar:gesiscrawler@us-wa.proxymesh.com:31280'
#   
#    # ...
#]
DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#    'scrapy_proxies.RandomProxy': 100,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # ...
    #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    #'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    ## below is for rotating user agents selected from USER_AGENTS list
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
    ##belowis from scrapy-user-agents library
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    #below is for ip ban due to request limit
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}

####This user-list is for scrapying wapo urls
#USER_AGENTS = [
#'Mozilla/5.0 (Windows NT 6.1) '
#'AppleWebKit/537.36 (KHTML, like Gecko) '
#'Chrome/41.0.2272.104 Safari/537.36',
#'Mozilla/5.0 (Windows NT 6.1; WOW64) '
#'AppleWebKit/537.36 (KHTML, like Gecko) '
#'Chrome/43.0.2357.124 Safari/537.36',
#'Mozilla/5.0 (X11; Linux x86_64) '
#'AppleWebKit/537.36 (KHTML, like Gecko) '
#'Chrome/42.0.2311.135 Safari/537.36',
#'Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K) '
#'AppleWebKit/537.36 (KHTML, like Gecko) '
#'Chrome/69.0.3497.100 Mobile Safari/537.36',
#'Mozilla/5.0 (X11; Linux x86_64) '
#'AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) '
#'Chrome/27.0.1453 Safari/537.36',
#'Mozilla/5.0 (Windows NT 6.1; WOW64) '
#'AppleWebKit/537.36 (KHTML, like Gecko) '
#'Chrome/49.0.2623.110 Safari/537.36',
#'Mozilla/5.0 (Windows NT 6.1; WOW64) '
#'AppleWebKit/537.36 (KHTML, like Gecko) '
#'Chrome/38.0.2125.111 Safari/537.36',
# 
#]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'GesisSpyder (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#  'GesisSpyder.middlewares.GesisspyderDownloaderMiddleware': 543,
#}
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#    #'GesisSpyder.middlewares.CustomDownloaderMiddleware': 543,#To activate a downloader middleware component
#}


# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'GesisSpyder.middlewares.GesisspyderSpiderMiddleware': 543,
#}



# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'GesisSpyder.pipelines.GesisspyderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
