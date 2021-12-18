# -*- coding: UTF-8 -*-

from scrapper import scrape_url_list_n_save, scrape_url_n_save, wrap_unseen_url
from config import RELEVANT_URLs_FILE
import pandas as pd
import article_manager

df = pd.read_csv(RELEVANT_URLs_FILE, sep="\t")
df.columns = ['urls']

scrape_url_list_n_save(df.urls)
