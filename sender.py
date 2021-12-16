# -*- coding: UTF-8 -*-

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
import article_manager
import source_manager
import ner_manager
import json
from utils import hash_url
from urllib.error import HTTPError
from time import sleep
import asyncio
from zmb_codes import StatusCode
from config import posting_logger

async def post(article_pkg):
    """
    """
    url = 'http://0.0.0.0:5000/api/v1/articles/'
    request = Request(url, urlencode(article_pkg).encode())
    await asyncio.sleep(0.01)
    response = urlopen(request).read().decode()
    return response

def prepare_article(article_map):
    """
    Adapt article_map for sending to the API
    """
    article_pkg = {}

    source_id = article_map['source_id']
    source_name = source_manager.find_name_by_id(source_id)

    article_pkg['source'] = source_name
    article_pkg['url'] = article_map['url']

    published_time = None
    if (article_map['published_time']):
        published_time = article_map['published_time'].strftime("%Y-%m-%d")
    article_pkg['published_time'] = published_time

    article_pkg['title'] = article_map['title']
    article_pkg['keywords'] = article_map['keywords']
    article_pkg['section'] = article_map['section']
    article_pkg['site_name'] = article_map['site_name']
    article_pkg['authors'] = article_map['authors']
    article_pkg['entities'] = article_map['entities']
    article_pkg['content'] = article_map['content']
    article_pkg['miner'] = "zmbnews"

    return article_pkg

def log_sending_attempt(json_response):
    """
    Logs sending attempts
    """
    status_code = json_response['status_code']
    message = json_response['message']
    if (status_code == StatusCode.DUPLICATE_KEY.code()):
        posting_logger.error(message)
    elif (status_code == StatusCode.SUCCESS.code()):
        posting_logger.info(message)

async def send_scrapped_articles():
    """
    Send an article for saving into the API
    """
    articles_not_sent = article_manager.get_all_articles_not_sent()

    for article in articles_not_sent:
        prepared_to_be_sent_article = prepare_article(article)

        url = prepared_to_be_sent_article['url']
        try:
            response = await post(prepared_to_be_sent_article)
        except HTTPError as e:
            msg = f"[FAILED]\t{url}"
            posting_logger.error(msg)
            continue

        json_response = json.loads(response)

        mark_article_as_sent(json_response, url)
        log_sending_attempt(json_response)

def mark_article_as_sent(json_response, url):
    """
    Marks an article as sent
    Args:
        json_response: the response as a json dictionary
        url: the URL that has been processed
    """
    status_code = json_response['status_code']

    if (status_code == StatusCode.DUPLICATE_KEY.code() or
        status_code == StatusCode.SUCCESS.code()):
        # If the article already exists in the API database or if the insert
        # operation has been successful then mark the article as sent
        article_manager.mark_article_as_sent(url)

#asyncio.run(send_scrapped_articles())
