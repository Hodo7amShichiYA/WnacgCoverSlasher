# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class CoverslasherPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print("into def 01")
        for (image_url, image_name) in zip(item["image_urls"], item["image_names"]):
            print(image_name, image_url)
            yield scrapy.Request(url=image_url, meta={"image_name": image_name})

    def file_path(self, request, response=None, info=None):
        print("into def 02")
        image_name = request.meta["image_name"]
        print(image_name)
        return '%s.jpg' %image_name
