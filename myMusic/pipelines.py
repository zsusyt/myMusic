# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from myMusic.Models import Album, Song, db_connect, create_table
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen_img = set()
        self.ids_seen_title = set()

    def process_item(self, item, spider):
        if item["imgSrc"] in self.ids_seen_img:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item["imgSrc"])
            return item

class MymusicPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        if 'isAlbum' in item:
            album = Album()
            album.imgSrc = item["imgSrc"]
            album.titleCn = item["titleCn"]
            album.titleEn = item["titleEn"]
            try:
                session.add(album)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
                DropItem("Album should be input once")
        else:
            song = Song()
            song.subTitle = item["subTitle"]
            song.lowUrl = item["lowUrl"]
            song.highUrl = item["highUrl"]
            try:
                session.add(song)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
            return item

# class MymusicPipeline(object):
#     def __init__(self):
#         """
#         Initializes database connection and sessionmaker.
#         Creates deals table.
#         """