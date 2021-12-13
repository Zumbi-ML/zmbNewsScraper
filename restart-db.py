from db_utils import drop_n_create_db
from source_manager import add_source
from URLs import urls
from scrapper import *

drop_n_create_db()

add_source({'name': 'Folha de São Paulo', 'home_url': 'https://www.folha.uol.com.br', 'enabled': True})
add_source({'name': 'Estadão', 'home_url': 'https://www.estadao.com.br/', 'enabled': True})
add_source({'name': 'O Globo', 'home_url': 'https://oglobo.globo.com/', 'enabled': True})

scrape_url_list_n_save(urls)

#scrape_url_n_save('https://www1.folha.uol.com.br/poder/2021/12/simone-tebet-se-lanca-pre-candidata-a-presidencia-e-critica-lideres-que-dividem-pais.shtml', 1)
