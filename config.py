# -*- coding: UTF-8 -*-

from newspaper import Config

# Scraper
# ==============================================================================
SCRAPER_LANGUAGE = 'pt'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

scrapper_cfg = Config()
scrapper_cfg.browser_user_agent = USER_AGENT
scrapper_cfg.request_timeout = 10
scrapper_cfg.memoize_articles = False
