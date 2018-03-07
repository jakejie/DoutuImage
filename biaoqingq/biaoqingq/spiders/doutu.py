# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from biaoqingq.items import BiaoqingqItem
# md5加密
import hashlib

m = hashlib.md5()


class BiaoqingSpider(CrawlSpider):
    name = 'doutu'
    allowed_domains = ['doutula.com']
    start_urls = ['http://www.doutula.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'ch/'), follow=True),
        Rule(LinkExtractor(allow=r'photo/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        item = BiaoqingqItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # video = response.xpath('//*[@id="threadVideo"]/@src').extract()
        # print(video)
        # if len(video) == 0:
        image = response.xpath(
            '//*[@id="detail"]/div/div[2]/li/div[3]/div/div/div/div[1]/table/tbody/tr[1]/td/img/@src').extract()
        print(image)
        if len(image) == 1:
            item["image_url"] = image[0]

        m.update(item["image_url"].encode("utf8"))
        item["md5_name"] = m.hexdigest()

        name = response.xpath('//*[@id="detail"]/div/div[2]/li/div[2]/h1/a/text()').extract()
        if name:
            print(name)
            item["name"] = name[0]
        return item
