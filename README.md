# DoutuImage
爬取各种表情包 斗图等图片信息 保存了图片地址到MySQL数据表  在网站需要使用该图片的时候 可以直接调用图片地址 不占用自己服务器空间


1.使用scrapy爬虫框架  

2.在pipeline中 使用了SQL alchemy数据表操作库

3.爬虫包括 https://www.biaoqing.com/|http://www.doutula.com/|https://www.52doutu.cn/ 三个网站的图片爬取 都是使用的全站爬虫 并且没有使用代理IP 

4.建议在使用的过程中 使用代理IP爬  并且适当降低爬取速度啊
