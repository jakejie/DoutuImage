# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from biaoqingq.items import BiaoqingqItem
# md5加密
import hashlib

m = hashlib.md5()


class BiaoqingSpider(CrawlSpider):
    name = '52doutu'
    allowed_domains = ['52doutu.cn']
    start_urls = ['https://www.52doutu.cn/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'52doutu'), follow=True),
        Rule(LinkExtractor(allow=r'pic'), follow=True),
        Rule(LinkExtractor(allow=r'/m/'), follow=True),
        Rule(LinkExtractor(allow=r'/rand/'), follow=True),
        Rule(LinkExtractor(allow=r'i/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        item = BiaoqingqItem()
        image = response.xpath(
            '//*[@id="target-img"]/@data-original').extract()
        print(image)
        if len(image) == 1:
            item["image_url"] = image[0]

        m.update(item["image_url"].encode("utf8"))
        item["md5_name"] = m.hexdigest()

        name = response.xpath('/html/body/div[4]/div/div[2]/p[1]/text()').extract()
        if name:
            print(name)
            item["name"] = name[0]
        return item
        # return i


# import requests,time
# from lxml import etree
# from biaoqingq.pipelines import BiaoqingqPipeline
#
# if __name__ == "__main__":
#     pro = BiaoqingqPipeline()
#
#     for i in range(1, 342):
#         # for i in range(1, 2):
#         url = "https://www.52doutu.cn/pic/{}/".format(i)
#         response = requests.get(url)
#         time.sleep(10)
#         tree = etree.HTML(response.text)
#         image_list = tree.xpath('/html/body/div[4]/div/a')
#         for image in image_list:
#             item = {}
#             detail_url = image.xpath('@href')
#             print(detail_url)
#             # res = requests.get(detail_url[0])
#             # names = etree.HTML(res.text)
#             # name = names.xpath('/html/body/div[4]/div/div[1]/h2/text()')
#             #
#             # image_url = image.xpath('div/img/@data-original')
#             #
#             # print(name, image_url)
#             # item["image_url"] = image_url[0]
#             # m.update(item["image_url"].encode("utf8"))
#             # item["md5_name"] = m.hexdigest()
#             # item["name"] = name[0]
#             # pro.process_item(item, "")
