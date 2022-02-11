

from urllib.request import urlopen
from xml.etree.ElementTree import parse

expansion_url = 'https://e00-expansion.uecdn.es/rss/empresas.xml'
confidencial_url = 'https://rss.elconfidencial.com/economia/'

# EXPANSION
expansion_open = urlopen(expansion_url)
expansion_xml = parse(expansion_open)

# EXPANSION HEADLINES
expansion_headlines = list(map(lambda item: item.findtext('title'), expansion_xml.findall('./channel/item')))

# Filtering - 'Santander'
santander_news = list(filter(lambda title: 'Santander' in title, expansion_headlines))

print(santander_news)

