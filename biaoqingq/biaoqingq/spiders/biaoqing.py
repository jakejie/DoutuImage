# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from biaoqingq.items import BiaoqingqItem
# md5加密
import hashlib

m = hashlib.md5()


class BiaoqingSpider(CrawlSpider):
    name = 'biaoqing'
    allowed_domains = ['biaoqing.com']
    start_urls = ['https://www.biaoqing.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'ch/'), follow=True),
        Rule(LinkExtractor(allow=r'thread/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        item = BiaoqingqItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        video = response.xpath('//*[@id="threadVideo"]/@src').extract()
        print(video)
        if len(video) == 0:
            image = response.xpath(
                '//*[@id="thread"]/div[2]/section/div/div[2]/div[1]/div[2]/span/div[1]/span/a/img/@src').extract()
            print(image)
            if len(image) == 1:
                item["image_url"] = image[0]
        else:
            item["image_url"] = video[0]
        m.update(item["image_url"].encode("utf8"))
        item["md5_name"] = m.hexdigest()
        item["name"] = "表情大全"
        return item
