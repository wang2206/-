import re
import scrapy
from ..items import Qd09TongrenItem_01
class TongrenSpider(scrapy.Spider):
    name = 'tongren_01'
    allowed_domains = []
    start_urls = [f'https://www.tongrenquan.org/tags-150-{page}.html' for page in range(0,52)]
    def parse(self, response):
        divs=response.css('.box div>.bk')
        for i in divs:
            link=i.css('a::attr(href)').get()
            link='https://www.tongrenquan.org'+link
            yield scrapy.Request(url=link,callback=self.parse_link)
    def parse_link(self,response):
        title=response.css('.clearfix .infos h1::text').get()
        span=response.css('.clearfix .infos .date span::text').get()
        lis=response.css('.book_list  .clearfix>li')
        for i in lis:
            link=i.css('a::attr(href)').get()
            link='https://www.tongrenquan.org'+link
            yield scrapy.Request(url=link,callback=self.parse_text,meta={'title':title,'span':span})
    def parse_text(self,response):
        title=response.meta['title']
        span=response.meta['span']
        h1 = response.xpath('//div[@class="read_chapterName tc"]/h1/text()').extract_first()
        text = response.xpath('//div[@class="read_chapterDetail"]/p/text()').extract()
        text = '\n'.join(text)
        yield Qd09TongrenItem_01(title=title,span=span, h1=h1,text=text)
