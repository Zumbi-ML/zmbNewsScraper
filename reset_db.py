from db_utils import drop_n_create_db
from managers.source_manager import add_sources
from scrapper import *

drop_n_create_db()
# ALTER DATABASE database_name CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
# ALTER TABLE tb_articles CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# GRANT ALL PRIVILEGES ON zmb_scrapper_db.* TO 'scrapper'@'localhost';

def get_sources():
    return [ \
        ["folha.uol", "Folha de São Paulo", "http://folha.uol.com.br/", 1],
        ["folhape", "Folha de Pernambuco", "http://folhape.com.br/", 1],
        ["g1.globo", "G1", "http://g1.globo.com", 1],
        ["observatoriodaimprensa", "Observário da Imprensa", "http://www.observatoriodaimprensa.com.br/", 1],
        ["agenciabrasil.ebc", "Agência Brasil", "https://agenciabrasil.ebc.com.br/", 1],
        ["brasil.elpais", "El País Brasil", "https://brasil.elpais.com/", 1],
        ["canaltech", "Canal Tech", "https://canaltech.com.br/", 1],
        ["capricho.abril", "Capricho", "https://capricho.abril.com.br/", 1],
        ["catracalivre", "Catraca Livre", "https://catracalivre.com.br/", 1],
        ["cbn.globoradio.globo", "CBN", "https://cbn.globoradio.globo.com/", 1],
        ["computerworld", "Computer World", "https://computerworld.com.br/", 1],
        ["exame", "Exame", "https://exame.com/", 1],
        ["gizmodo.uol", "Gizmodo Brasil", "https://gizmodo.uol.com.br/", 1],
        ["globoesporte.globo", "Globo Esporte", "https://globoesporte.globo.com/", 1],
        ["istoe", "Isto É", "https://istoe.com.br/", 1],
        ["jornal.usp", "Jornal da USP", "https://jornal.usp.br/", 1],
        ["jornaldebrasilia", "Jornal de Brasília", "https://jornaldebrasilia.com.br/", 1],
        ["jovempan", "Jovem Pan", "https://jovempan.com.br/", 1],
        ["noticias.r7", "R7", "https://noticias.r7.com/", 1],
        ["oglobo.globo", "O Globo", "https://oglobo.globo.com/", 1],
        ["epoca.globo", "Época", None, 0],
        ["olhardigital", "Olhar Digital", "https://olhardigital.com.br/", 1],
        ["revistagloborural.globo", "Revista Globo Rural", "https://revistagloborural.globo.com/", 1],
        ["revistapegn.globo", "Revista PEGN", "https://revistapegn.globo.com/", 1],
        ["veja.abril", "Veja", "https://veja.abril.com.br/", 1],
        ["agazeta", "A Gazeta", "https://www.agazeta.com.br/", 1],
        ["bbc", "BBC", "https://www.bbc.com/portuguese/", 1],
        ["bemparana", "Bem Paraná", "https://www.bemparana.com.br/", 1],
        ["brasil247", "Brasil 247", "https://www.brasil247.com/", 1],
        ["brasildefato", "Brasil de Fato", "https://www.brasildefato.com.br/", 1],
        ["camara", "Agência da Câmara", "https://www.camara.leg.br/", 1],
        ["cartacapital", "Carta Capital", "https://www.cartacapital.com.br/", 1],
        ["cnnbrasil", "CNN Brasil", "https://www.cnnbrasil.com.br/", 1],
        ["correiobraziliense", "Correio Brasiliense", "https://www.correiobraziliense.com.br/", 1],
        ["dw", "Deutsche Walle", "https://www.dw.com/pt-br/", 1],
        ["espn", "ESPN", "https://www.espn.com.br/", 1],
        ["estadao", "Estadão", "https://www.estadao.com.br/", 1],
        ["gazetadopovo", "Gazeta do Povo", "https://www.gazetadopovo.com.br/", 1],
        ["gazetaesportiva", "Gazeta Esportiva", "https://www.gazetaesportiva.com/", 1],
        ["infomoney", "InfoMoney", "https://www.infomoney.com.br/", 1],
        ["metropoles", "Metrópoles", "https://www.metropoles.com/", 1],
        ["opovo", "O Povo", "https://www.opovo.com.br/", 1],
        ["poder360", "Poder 360", "https://www.poder360.com.br/", 1],
        ["techtudo", "TechTudo", "https://www.techtudo.com.br/", 1],
        ["tecmundo", "TecMundo", "https://www.tecmundo.com.br/", 1],
        ["terra", "Terra", "https://www.terra.com.br/", 1],
        ["uol", "UOL", "https://www.uol.com.br/", 1],
        ["senado", "Senado", "https://www12.senado.leg.br/", 1],
        ["diarioesportes", "Diário Esportes", None, 0],
        ["acidadeon", "A Cidade On", None, 0],
        ["aen.pr", "Agência de Notícias do Paraná", None, 0],
        ["agenciapara", "Agência Pará", None, 0],
        ["altairtavares", "Altair Tavares", None, 0],
        ["amazonasatual", "Amazona Atual", None, 0],
        ["aventurasnahistoria.uol", "Aventuras na História", None, 0],
        ["bahianoticias", "Bahia Notícias", None, 0],
        ["bebe.abril", "Bebê", None, 0],
        ["brasildefatomg", "Brasil de Fato MG", None, 0],
        ["brasildefatope", "Brasil de Fato Pe", None, 0],
        ["brasildefatorj", "Brasil de Fato RJ", None, 0],
        ["brasildefators", "Brasil de Fato RS", None, 0],
        ["cbncuritiba", "CBN Curitiba", None, 0],
        ["cidadeverde", "Cidade Verde", None, 0],
        ["cineset", "Cine Set", None, 0],
        ["claudia.abril", "Cláudia", None, 0],
        ["conjur", "Conjur", None, 0],
        ["defatoonline", "De Fato", None, 0],
        ["diariodaregiao", "Diário da Região", None, 0],
        ["diariodecanoas", "Diário de Canoas", None, 0],
        ["dn", "Diário de Notícias", None, 0],
        ["diariodeuberlandia", "Diário de Uberlândia", None, 0],
        ["diariodocomercio", "Diário do Comércio", None, 0],
        ["diariodorio", "Diário do Rio", None, 0],
        ["diariodoturismo", "DIário do Turismo", None, 0],
        ["tvi24.iol", "Diário IOL", None, 0],
        ["domtotal", "Dom Total", None, 0],
        ["radios.ebc", "EBC", None, 0],
        ["epocanegocios.globo", "Época Negócios", None, 0],
        ["link.estadao", "Estadão", None, 0],
        ["politica.estadao", "Estadão", None, 0],
        ["esportes.estadao", "Estadão", None, 0],
        ["economia.estadao", "Estadão", None, 0],
        ["cultura.estadao", "Estadão", None, 0],
        ["internacional.estadao", "Estadão", None, 0],
        ["emais.estadao", "Estadão", None, 0],
        ["pme.estadao", "Estadão", None, 0],
        ["mg.superesportes", "Estado de Minas", None, 0],
        ["em", "Estado de Minas", None, 0],
        ["estudosnacionais", "Estudos Nacionais", None, 0],
        ["expresso", "Expresso", None, 0],
        ["extraclasse", "Extra Classe", None, 0],
        ["falauniversidades", "Fala Universidades", None, 0],
        ["focus.jor", "Focus", None, 0],
        ["orapois.blogfolha.uol", "Folha Blogs", None, 0],
        ["mural.blogfolha.uol", "Folha Blogs", None, 0],
        ["inteligenciademercado.blogfolha.uol", "Folha Blogs", None, 0],
        ["f5.folha.uol", "Folha de São Paulo", None, 0],
        ["folhavitoria", "Folha Vitória", None, 0],
        ["futebolatino.lance", "Futebol Latino", None, 0],
        ["gauchazh.clicrbs", "Gaúcha ZH", None, 0],
        ["geledes", "Geledés", None, 0],
        ["revistaglamour.globo", "Glamour", None, 0],
        ["blogs.oglobo.globo", "Globo Blogs", None, 0],
        ["ceara", "Governo do Ceará", None, 0],
        ["gq.globo", "GQ", None, 0],
        ["grandepremio", "Grande Prêmio", None, 0],
        ["gshow.globo", "GShow", None, 0],
        ["guia21.sul21", "Guia21", None, 0],
        ["hojeemdia", "Hoje em Dia", None, 0],
        ["hugogloss.uol", "Hugo Gloss", None, 0],
        ["hypeness", "Hypeness", None, 0],
        ["gente.ig", "iG", None, 0],
        ["tecnologia.ig", "iG", None, 0],
        ["ultimosegundo.ig", "iG", None, 0],
        ["economia.ig", "iG", None, 0],
        ["esporte.ig", "iG", None, 0],
        ["istoedinheiro", "Isto É Dinheiro", None, 0],
        ["jcnet", "JCNET", None, 0],
        ["jmonline", "Jornal da Manhã", None, 0],
        ["jb", "Jornal do Brasil", None, 0],
        ["jornaldocomercio", "Jornal do Comércio", None, 0],
        ["ionline.sapo", "Jornal I", None, 0],
        ["midiamax", "Jornal MidiaMax", None, 0],
        ["lance", "Lance", None, 0],
        ["legiaodosherois", "Legião dos Heróis", None, 0],
        ["marcozero", "Marco Zero", None, 0],
        ["revistamarieclaire.globo", "Marie Claire", None, 0],
        ["meon", "Meon", None, 0],
        ["migalhas", "Migalhas", None, 0],
        ["revistamonet.globo", "Monet", None, 0],
        ["moneytimes", "MoneyTimes", None, 0],
        ["mpf.mp", "MPF", None, 0],
        ["multiversomais", "Multiverso +", None, 0],
        ["nsctotal", "NCS", None, 0],
        ["ndmais", "ND", None, 0],
        ["nexojornal", "Nexo", None, 0],
        ["cartamaior", "Notícia Concursos", None, 0],
        ["noticiasconcursos", "Notícia Concursos", None, 0],
        ["noticiasaominuto", "Notícias ao Minuto", None, 0],
        ["obrasilianista", "O Brasilianista", None, 0],
        ["odia.ig", "O Dia", None, 0],
        ["extra.globo", "O Globo", None, 0],
        ["kogut.oglobo.globo", "O Globo", None, 0],
        ["liberal", "O Liberal", None, 0],
        ["progresso", "O Progresso Digital", None, 0],
        ["otempo", "O Tempo", None, 0],
        ["oabam", "OAB Amazonas", None, 0],
        ["observador", "Observador", None, 0],
        ["observatoriodocinema.uol", "Observatório do Cinema", None, 0],
        ["observatoriodosfamosos.uol", "Observatório dos Famosos", None, 0],
        ["observatorio3setor", "Observatório3Setor", None, 0],
        ["omelete", "Omelete", None, 0],
        ["tab.uol", "Outra Coisa", None, 0],
        ["paraibaja", "Paraíba Já", None, 0],
        ["paranaportal.uol", "Paraná Portal", None, 0],
        ["piaui.folha.uol", "Piauí", None, 0],
        ["policiacivil.pr", "Polícia Civil do Paraná", None, 0],
        ["ponte", "Ponte", None, 0],
        ["atarde.uol", "Portal a Tarde", None, 0],
        ["portalcorreio", "Portal Correio", None, 0],
        ["registro.portaldacidade", "Portal da Cidade", None, 0],
        ["diaonline.ig", "Portal Dia Online", None, 0],
        ["embarquenaviagem", "Portal Embarque na Viagem", None, 0],
        ["portalmultiplix", "Portal Multiplix", None, 0],
        ["uai", "Portal Uai", None, 0],
        ["portugaldigital", "Portugal Digital", None, 0],
        ["porvir", "Porvir", None, 0],
        ["pplware.sapo", "Pplware", None, 0],
        ["itajai.sc", "Prefeitura de Itajaí", None, 0],
        ["projetocolabora", "Projeto Colabora", None, 0],
        ["publico", "Público", None, 0],
        ["purebreak", "PureBreak Brasil", None, 0],
        ["querobolsa", "Quero Bolsa", None, 0],
        ["recordtv.r7", "R7", None, 0],
        ["entretenimento.r7", "R7", None, 0],
        ["esportes.r7", "R7", None, 0],
        ["razoesparaacreditar", "Razões para Acreditar", None, 0],
        ["redebrasilatual", "Rede Brasil Atual", None, 0],
        ["redepara", "Rede Pará", None, 0],
        ["revista.algomais", "Revista Algo Mais", None, 0],
        ["revistacrescer.globo", "Revista Crescer", None, 0],
        ["revistaforum", "Revista Fórum", None, 0],
        ["revistagalileu.globo", "Revista Galileu", None, 0],
        ["revistaquem.globo", "Revista Quem", None, 0],
        ["rollingstone.uol", "Rolling Stone", None, 0],
        ["sala7design", "Sala 7 Design", None, 0],
        ["web.satc", "SATC", None, 0],
        ["saude.abril", "Saúde", None, 0],
        ["seculodiario", "Século", None, 0],
        ["setor3", "Senac SP", None, 0],
        ["spbancarios", "Sindicato dos Bancários de SP", None, 0],
        ["sportbuzz.uol", "SportBuzz", None, 0],
        ["super.abril", "Super Interessante", None, 0],
        ["tenhomaisdiscosqueamigos", "Tenho mais discos que amigos", None, 0],
        ["goal", "Terra", None, 0],
        ["epipoca", "Terra", None, 0],
        ["theintercept", "The Intercept", None, 0],
        ["torcedores", "Torcedores", None, 0],
        ["tribunademinas", "Tribuna de Minas", None, 0],
        ["tribunadonorte", "Tribuna do Norte", None, 0],
        ["uaaau", "Uaaau", None, 0],
        ["ufmg", "UFMG", None, 0],
        ["universoracionalista", "Universio Racionalista", None, 0],
        ["noticiasdatv.uol", "UOL", None, 0],
        ["tvefamosos.uol", "UOL", None, 0],
        ["entretenimento.uol", "UOL", None, 0],
        ["educacao.uol", "UOL", None, 0],
        ["economia.uol", "UOL", None, 0],
        ["noticias.uol", "UOL", None, 0],
        ["emdesconstrucao.blogosfera.uol", "UOL Blogs", None, 0],
        ["valor.globo", "Valor", None, 0],
        ["valorinveste.globo", "Valor Investe", None, 0],
        ["varginhaonline", "Varginha Online", None, 0],
        ["vejario.abril", "Veja Rio", None, 0],
        ["vejasp.abril", "Veja SP", None, 0],
        ["viagemeturismo.abril", "Viagem e Turismo", None, 0],
        ["visao.sapo", "Visão", None, 0],
        ["vocerh.abril", "Você RH", None, 0],
        ["vocesa.abril", "Você SA", None, 0],
        ["vogue.globo", "Vogue", None, 0],
        ["esportes.yahoo", "Yahoo Esportes", None, 0],
        ["br.financas.yahoo", "Yahoo Finanças", None, 0],
        ["br.noticias.yahoo", "Yahoo Notícias", None, 0],
        ["esquerda", "Esquerda.net", None, 0],
        ["coletiva", "Coletiva.net", None, 0],
        ["aeroin", "AEROIN", None, 0],
        ]

source_map_list = []
for source in get_sources():
    url_key, name, home_url, enabled = source
    source_map_list.append(
        {"url_key": url_key, "name": name, "home_url": home_url, "enabled": enabled}
    )
add_sources(source_map_list)

scrape_url_list_n_save(urls)

#scrape_url_n_save('https://www1.folha.uol.com.br/poder/2021/12/simone-tebet-se-lanca-pre-candidata-a-presidencia-e-critica-lideres-que-dividem-pais.shtml', 1)