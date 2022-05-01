# -*- coding: utf-8 -*-

# Scrapy settings for fotocasa project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from __future__ import unicode_literals
import os
import sys
import django

from .proxies import get_proxies
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lloguerinfo.settings")
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../..","../"))

django.setup()


###########################
# Main configuration
###########################

BOT_NAME = 'fotocasa'

SPIDER_MODULES = ['fotocasa.spiders']
NEWSPIDER_MODULE = 'fotocasa.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620    
}

DOWNLOAD_TIMEOUT = 200

DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://www.fotocasa.es/'
}

###########################
# User agent configurarion
###########################
USER_AGENT_LIST = "./useragents.txt"

#########################
# Proxies configuration
#########################

RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]

#ROTATING_PROXY_PAGE_RETRY_TIMES = 99999999999
#ROTATING_PROXY_LIST = get_proxies()

ITEM_PIPELINES = {
    'fotocasa.pipelines.FotocasaPipeline': 300
}