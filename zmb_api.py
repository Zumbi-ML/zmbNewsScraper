# -*- coding: UTF-8 -*-

import os
from dotenv import load_dotenv

load_dotenv()

class ZmbApi:

    class Article:

        def path():
            api_host = os.getenv('API_HOST')
            api_port = os.getenv('API_PORT')
            api_version = os.getenv('API_VERSION')
            return f"{api_host}:{api_port}/{api_version}/articles/"
