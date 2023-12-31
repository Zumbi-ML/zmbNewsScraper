# -*- coding: UTF-8 -*-

from scrapper import scrape_url_list_n_save
from config import RELEVANT_URLs_FILE
import pandas as pd
import managers.article_manager as article_manager

df = pd.read_csv(RELEVANT_URLs_FILE, sep="\t")
df.columns = ['urls']

scrape_url_list_n_save(df.urls)

#scrape_url_list_n_save(['https://br.noticias.yahoo.com/marca-obrigada-excluir-video-por-racismo-e-abuso-infantil-210156531.html'])
