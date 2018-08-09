import scrapy
from scrapy import Request


class TicketsSpider(scrapy.Spider):
    name = 'tickets'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://newyork.craigslist.org/d/tickets/search/tia']

    def parse(self, response):
        tickets = response.xpath('//p[@class="result-info"]')

        for ticket in tickets:
            relative_url = ticket.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            
            title = ticket.xpath('a/text()').extract_first()
            price = ticket.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract_first("")      
            
            yield {'Title': title, 'Price': price}

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)

        yield Request(absolute_next_url, callback=self.parse)


    """def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        price = response.meta.get('Price')

        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract())

        #date = response.xpath('span[@class="attrgroup"]/span[@class="otherpostings"]/text()').extract_first("")
        #venue = response.xpath('//p[@class="attrgroup"]/span/b/text()')[1].extract()

        yield{'Title': title, 'Price': price, 'Description': description}"""
 