from bs4 import BeautifulSoup as BS
import requests
import config


class DreamParser:

    def __init__(self, start):
        self.dream_index = start

    def get_next_dream_html(self):
        response = requests.get(config.URL.format(self.dream_index))
        response.encoding = 'utf-8'
        if response.ok:
            return response.text
        return None

    def get_dream(self, html):
        html_tree = BS(html, "lxml")
        dream_content = html_tree.find("td", id="content")
        dream_title = dream_content.find("h1", class_="hr").text

        dream_data = {
            'id': str(self.dream_index),
            'letter': dream_title[0],
            'title': dream_title,
            'group': dream_content.find("p", class_="smalltxt").find("a").text,
            'context': dream_content.find("div", id="hypercontext").find('p').text
        }

        self.dream_index += 1

        return dream_data
