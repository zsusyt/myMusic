import scrapy
from myMusic.items import MymusicItem

class AllMusicSpider(scrapy.Spider):
    name = "allmusic"

    start_urls = [
        'http://ncpa-classic.cntv.cn/gdyysx/1/index.shtml',
        # 'http://ncpa-classic.cntv.cn/gdyysx/2/index.shtml',
        # 'http://ncpa-classic.cntv.cn/gdyysx/3/index.shtml',
        # 'http://ncpa-classic.cntv.cn/gdyysx/4/index.shtml',
        # 'http://ncpa-classic.cntv.cn/gdyysx/5/index.shtml',
        # 'http://ncpa-classic.cntv.cn/gdyysx/6/index.shtml',
        # 'http://ncpa-classic.cntv.cn/gdyysx/7/index.shtml',
    ]

    def parse(self, response):
        item = MymusicItem()

        for music in response.css('ul.musiclist li'):
            item['imgSrc'] = music.css('div.imgbox a img::attr(src)').get()
            item['title'] = {
                'ch': music.css('div.conbox h1 a::text').get(),
                'en': music.css('div.conbox h2 a::text').get()
            }
            item['url'] = music.css('div.conbox h1 a::attr(href)').get()
            yield item

        # for a in response.css('li.next a'):
            #     yield response.follow(a, callback=self.parse)