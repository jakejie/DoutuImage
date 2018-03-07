# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import Column, String, create_engine, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 数据库连接信息
db_host = '********'
db_user = 'root'
db_pawd = 'roottoor'
db_name = 'music'
db_port = 3306

# 创建对象的基类:
Base = declarative_base()


class Biaoqing(Base):
    __tablename__ = 'biaoqing'
    # 表结构
    id = Column(Integer, unique=True, primary_key=True)
    image_url = Column(String(1024))
    md5_name = Column(String(1024))
    name = Column(String(1024))


class BiaoqingqPipeline(object):
    def __init__(self):
        # pass
        # 初始化数据库连接,:
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def process_item(self, item, spider):
        info = Biaoqing(
            image_url=item["image_url"],
            md5_name=item["md5_name"],
            name=item["name"]
        )
        self.session.add(info)
        self.session.commit()
        return item


class Dele():
    def __init__(self):
        # pass
        # 初始化数据库连接,:
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def delete_other(self):
        info = self.session.query(Biaoqing).filter(
            image_url="https://www.52doutu.cn/static/images/others/loading.gif"
        ).all()
        self.session.delete(info)
        self.session.commit()


if __name__ == "__main__":
    # engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
    #                        .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
    # Base.metadata.create_all(engine)
    de = Dele()
    de.delete_other()
