

from urllib.request import urlopen
from xml.etree.ElementTree import parse

el_economista_url = 'https://www.eleconomista.es/rss/rss-economia.php'

# EL ECONOMISTA
el_economista_open = urlopen(el_economista_url)
el_economista_xml = parse(el_economista_open)

# EL ECONOMISTA Headlines
el_economista_headlines = list(map(lambda x: x.findtext('title'), el_economista_xml.findall('./channel/item')))

# Filtering - 'Santander'
santander_news = list(filter(lambda x: 'Santander' in x, el_economista_headlines))

print(santander_news)