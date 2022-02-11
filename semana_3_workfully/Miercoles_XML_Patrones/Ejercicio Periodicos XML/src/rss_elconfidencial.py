

from urllib.request import urlopen
from xml.etree.ElementTree import parse

confidencial_url = 'https://rss.elconfidencial.com/mercados/'

# EL CONFIDENCIAL
confidencial_open = urlopen(confidencial_url)
confidencial_xml = parse(confidencial_open)

# CONFIDENCIAL HEADLINES
confidencial_headlines = list(map(lambda item: item.text, confidencial_xml.iter('{http://www.w3.org/2005/Atom}title')))

# Filtering 'bitcoin'
for headline in confidencial_headlines:
    if 'bitcoin' in headline:
        print(headline)
