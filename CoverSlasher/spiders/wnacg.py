import scrapy
from CoverSlasher.items import CoverslasherItem
class wnacg(scrapy.Spider):
    name = "wnacg"  # 定义蜘蛛名
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        }
        tag = '風的工房'
        for i in range(1, 73):
            url1 = "https://www.wnacg.com/albums-index-page-%s-sname-%s.html" % (i, tag)
            print("正在爬取"+url1)
            yield scrapy.Request(
                url=url1,
                headers=headers,
                callback=self.parse_cover,
            )
    def parse_cover(self, response):
        item = CoverslasherItem()
        TempCoverUrls = response.xpath('//img/@src').extract()[1:]
        item['image_urls'] = ["https:"+i for i in TempCoverUrls]
        item['image_names'] = response.xpath('//img/@alt').extract()[1:]
        print(item)
        yield item

