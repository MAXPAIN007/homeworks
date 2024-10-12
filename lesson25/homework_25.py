# parsing
from lxml import html
import requests

url = 'https://example.com'
response = requests.get(url)
html_content = response.content

tree = html.fromstring(html_content)

title = tree.findtext('.//title')
print("Заголовок сторінки:", title)

links = tree.xpath('//a/text()')
for link in links:
    print("Посилання:", link)