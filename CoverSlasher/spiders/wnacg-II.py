import scrapy
from CoverSlasher.items import CoverslasherItem
class wnacg2(scrapy.Spider):
    name = "wnacg2"  # 定义蜘蛛名
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        }
        for i in range(2, 50):
            url1 = "https://www.wnacg.org/photos-index-page-%s-aid-70413.html" % i
            yield scrapy.Request(
                url=url1,
                headers=headers,
                callback=self.parse_cover,
            )
    def parse_cover(self, response):
        TempLinks = response.xpath('//a[starts-with(@href,"/photos-view-id")]/@href').extract()
        urllinks = ["https://www.wnacg.org"+i for i in TempLinks]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        }
        for urllink in urllinks:
            yield scrapy.Request(
                url=urllink,
                headers=headers,
                callback=self.parse_page,
            )
    def parse_page(self, response):
        item = CoverslasherItem()
        TempImgUrls = response.xpath('//img/@src').extract()[2]
        item['image_urls'] = ["https:" + TempImgUrls]
        TempImgName = response.xpath('//div/h1/text()').extract()[0]
        ImgName = TempImgName.split("\n")
        ImgName = ImgName[1]
        item['image_names'] = [ImgName]
        yield item


