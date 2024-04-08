import lxml.html
import requests

time_response = requests.get('https://www.utctime.net/')
html_tree = lxml.html.document_fromstring(time_response.text)
list_of_matches = html_tree.xpath('//*[@id="time2"]')
print(list_of_matches[0].text)
