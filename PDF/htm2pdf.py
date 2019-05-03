# coding:utf-8

import requests
from bs4 import BeautifulSoup
import pdfkit
# https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
# https://wkhtmltopdf.org/downloads.html
# pip install pdfkit
URL = 'http://www.huaxiaozhuan.com/'


class Converter(object):
    def __init__(self, url):
        self.url = url
    
    def get_url_list(self):
        """
        get directory
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html5lib")
        uls = soup.find_all(name='ul')
        urls = [self.url]
        for ul in uls:
            path = ul.li.a
            if path:
                url = f"{self.url}{path.get('href')}"
                print(url)
                urls.append(url)
        return urls
    
    def parse_url_to_html(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html5lib")
        body = soup.find(class_="typora-export")
        html = str(body).encode()
        file_name = url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(html)
        return file_name

    def save_pdf(self, htmls):
        """
        html --> pdf
        """
        options = {
            'page-size': 'Letter',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ]
        }
        # from_file
        print(htmls)
        pdfkit.from_url(htmls, 'test.pdf', options=None)

def main():
    c = Converter(URL)
    urls = c.get_url_list()
    # fs = []
    # for url in urls[:1]:
    #     fn = c.parse_url_to_html(url)
    #     fs.append(fn)
    c.save_pdf(urls[:2])

if __name__ == '__main__':
    main()