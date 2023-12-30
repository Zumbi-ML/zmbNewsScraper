# -*- coding: UTF-8 -*-

from dotenv import load_dotenv

load_dotenv()

class ZmbLabels:

    class Article:

        class Source:
            def api():
                return "sources"

        class Title:
            def api():
                return "title"

        class Keyword:
            def api():
                return "keywords"

        class Section:
            def api():
                return "section"

        class Site:
            def api():
                return "site_name"

        class Author:
            def api():
                return "authors"

        class Entity:
            def api():
                return "entities"

        class Content:
            def api():
                return "content"

        class Miner:
            def api():
                return "miner"

        class PublishedTime:
            def api():
                return "published_time"

        class URL:
            def api():
                return "url"

        class HTML:
            def api():
                return "html"

        class Metadata:
            def api():
                return "meta_data"

        def all_labels():
            return [class_.api() for class_ in ZmbLabels.Article._all_classes()]

        def _all_classes():
            return [ \
                ZmbLabels.Article.Source,
                ZmbLabels.Article.Title,
                ZmbLabels.Article.Keyword,
                ZmbLabels.Article.Section,
                ZmbLabels.Article.Site,
                ZmbLabels.Article.Author,
                ZmbLabels.Article.Entity,
                ZmbLabels.Article.Content,
                ZmbLabels.Article.Miner,
                ZmbLabels.Article.PublishedTime,
                ZmbLabels.Article.URL,
                ZmbLabels.Article.HTML,
                ZmbLabels.Article.Metadata,
                ZmbLabels.Article.Miner,
            ]

        def api_url():
            return "http://0.0.0.0:5000/api/v1/articles/"

        def prep2go(article_map):
            """
            Prepare article_map for sending to zmbAPI
            """
            prepped = {}
            for class_ in ZmbLabels.Article._all_classes():
                # .api(): the label used in the API
                api_label = class_.api()
                if (api_label in article_map.keys()):
                    field_val = ""
                    if (article_map[api_label]):
                        field_val = article_map[api_label]
                    prepped[api_label] = field_val
            return prepped
