

from urllib.request import urlopen
from xml.etree.ElementTree import parse

cinco_dias_url = 'https://cincodias.elpais.com/seccion/rss/mercados/'

# CINCO DIAS
cinco_dias_open = urlopen(cinco_dias_url)
cinco_dias_xml = parse(cinco_dias_open)

# EXPANSION HEADLINES
cinco_dias_headlines = list(map(lambda x: x.findtext('title'), cinco_dias_xml.findall('./channel/item')))

# Filtering - 'Indra'
indra_news = list(filter(lambda x: 'Indra' in x, cinco_dias_headlines))

print(indra_news)