import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    def parse(self, response):
        '''
        title = response.css('title::text').extract_first()
        self.log('the title is %s' % title)
        '''
        for quote in response.css('div.quote'):
            yield{
                'text' : quote.css('span.text::text').extract_first().encode('ascii', 'ignore'),
                'author' : quote.css('small.author::text').extract_first().encode('ascii', 'ignore'),
                'tag' : [i.encode('ascii', 'ignore') for i in quote.css('div.tags a.tag::text').extract()]
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield reponse.follow(href, callback = self.parse)
            '''
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)
            '''
    '''
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for u in urls:
            yield scrapy.Request(u, callback=self.parse_httpbin)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    '''
