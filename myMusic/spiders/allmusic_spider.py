import scrapy
from myMusic.items import AlbumItem, SongItem
import re
import json

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
        for music in response.css('ul.musiclist li'):
            item = AlbumItem()
            item['imgSrc'] = music.css('div.imgbox a img::attr(src)').get()
            item['titleCn'] = music.css('div.conbox h1 a::text').get()
            item['titleEn'] = music.css('div.conbox h2 a::text').get()
            item['isAlbum'] = True
            url = music.css('div.conbox h1 a::attr(href)').get()
            yield item

            request = scrapy.Request(url, callback=self.parse_detail)
            request.meta['item'] = item
            yield request


    def parse_detail(self, response):
        pre_item = response.meta['item']

        mid = response.xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[1]/div/div/script[3]/text()').get()
        midNoSpace = re.sub(r'\s*', '', mid)
        result = json.loads(re.search(r'\[.*\]', midNoSpace).group())

        for title_id in result:
            request = scrapy.Request("http://vdn.apps.cntv.cn/api/getIpadVideoInfo.do?pid=" + title_id, callback=self.parse_song)
            request.meta['pre_item'] = pre_item
            yield request


    def parse_song(self, response):
        pre_item = response.meta['pre_item']

        mid = response.body.decode()
        midSecond = re.search(r'{.*}', mid).group()
        result = json.loads(midSecond)
        item = SongItem()
        item['lowUrl'] = result['video']['lowChapters'][0]['url']
        item['highUrl'] = result['video']['chapters'][0]['url']
        item['subTitle'] = result['title']
        item['imgSrc'] = pre_item['imgSrc']
        return item


