class CrawlerItem(scrapy.Item):
    app_name = scrapy.Field()
    apk_path = scrapy.Field()
    app_hash = scrapy.Field()
    permissions = scrapy.Field()