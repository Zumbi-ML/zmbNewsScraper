# -*- coding: UTF-8 -*-

import managers.article_manager as article_manager
import asyncio
from config import sender_logger
from dotenv import load_dotenv
import json
import managers.ner_manager as ner_manager
from time import sleep
import requests
import managers.source_manager as source_manager
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zmb_codes import StatusCode
from zmb_api import ZmbApi
from time import sleep
from zmb_labels import ZmbLabels

load_dotenv()

def send_scrapped_articles():
    """
    Send an article for saving into the API
    """
    articles_not_sent = article_manager.get_all_articles_not_sent()

    for article in articles_not_sent:
        url = article['url']
        try:
            send_article(article)
        except:
            print(f"Error in sending: {url}")

def send_article(article_map):
    """
    """

    prepped = ZmbLabels.Article.prep2go(article_map)

    url = prepped['url']
    try:
        response = post(prepped)
        print(response)
        sleep(0.5)
    except HTTPError as e:
        msg = f"[FAILED]\t{url}"
        sender_logger.error(msg)
        raise e

    json_response = json.loads(response)

    mark_article_as_sent(json_response, url)
    log_sending_attempt(json_response)

def post(article_pkg):
    """
    Make a post request
    """
    url = ZmbLabels.Article.api_url()
    request = Request(url, urlencode(article_pkg).encode())
    #await asyncio.sleep(0.01)
    response = urlopen(request).read().decode()
    return response

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

def log_sending_attempt(json_response):
    """
    Logs sending attempts
    """
    status_code = json_response['status_code']
    message = json_response['message']
    if (status_code == StatusCode.DUPLICATE_KEY.code()):
        sender_logger.error(message)
    elif (status_code == StatusCode.SUCCESS.code()):
        sender_logger.info(message)


send_scrapped_articles()

#asyncio.run(send_scrapped_articles())
