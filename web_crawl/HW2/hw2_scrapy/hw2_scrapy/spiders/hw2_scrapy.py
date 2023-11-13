from scrapy.spiders import Spider
from bs4 import BeautifulSoup

class hw2_scrapy(Spider):
    name = 'hw2_scrapy'
    start_urls = ['https://www.aa.ntnu.edu.tw/zh_tw/News?category%5B%5D=6331b9713817848ea26d27b5&category%5B%5D=6331b9713817848ea26d27b6&category%5B%5D=6331b9713817848ea26d27b7&category%5B%5D=6331b9713817848ea26d27b8&category%5B%5D=6331ed7b381784be12bdd622&tags%5B%5D=all']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h3', class_='sitemenu-title').text

        print(title)

        rows = response.css('table#DataTables_Table_0 tbody tr')

        for row in rows:
            unit = row.css('td.i-annc__author dtr-control::text').get()
            post_date = row.css('td.i-annc__postdate span::text').get()
            title = row.css('td.i-annc__content a::text').get()
            view_count = row.css('td.i-annc__view-count::text').get()

            yield {
                'Unit': unit,
                'Post Date': post_date.strip(),
                'Title': title.strip(),
                'View Count': view_count
            }
