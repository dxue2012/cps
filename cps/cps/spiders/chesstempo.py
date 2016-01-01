import scrapy
from scrapy.selector import Selector

from cps.items import CpsItem

class chesstempoSpider(scrapy.Spider):
    name = 'chesstempo'
    tactics_url = 'http://chesstempo.com/chess-tactics.html'
    start_urls = [tactics_url]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {
                        'wait': 5
                    }
                }
            })

    def parse(self, response):
        # response.body is a result of a render.html call; it
        # contains HTML processed by a browser
        selector = Selector(response)
        item = CpsItem()
        item['FEN'] = selector.css('.ct-board').xpath('./@alt').extract_first()
        return item
