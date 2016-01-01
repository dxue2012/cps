import scrapy
from scrapy.selector import Selector

from cps.items import CpsItem

TACTICS_URL = 'http://chesstempo.com/chess-tactics.html'
NUM_PUZZLES_NEEDED = 100


class chesstempoSpider(scrapy.Spider):
    name = 'chesstempo'
    allowed_domains = ['chesstempo.com']
    concurrent_max = 4
    count = 0

    # NOTE: this requires scrapyjs and splash, since we want
    # the website to load the content using JS before we crawl it
    def request(self):
        return scrapy.Request(TACTICS_URL, self.parse, meta={
            'splash': {
                'endpoint': 'render.html',
                'args': {
                    'wait': 10
                }
            }
        }, dont_filter=True)

    def start_requests(self):
        i = 0
        for i in range(self.concurrent_max):
            yield self.request()

    def parse(self, response):
        # response.body is a result of a render.html call; it
        # contains HTML processed by a browser
        selector = Selector(response)
        item = CpsItem()
        item['FEN'] = selector.css('.ct-board').xpath('./@alt').extract_first()
        if item['FEN'] is not None:
            self.count += 1
            yield item

        if self.count < NUM_PUZZLES_NEEDED:
            yield self.request()
