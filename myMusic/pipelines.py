# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from myMusic.Models import MusicDB, db_connect, create_table

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
        musicdb = MusicDB()
        musicdb.imgSrc = item["imgSrc"]
        musicdb.titleCn = item["titleCn"]
        musicdb.titleEn = item["titleEn"]
        musicdb.url = item["url"]

        try:
            session.add(musicdb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
