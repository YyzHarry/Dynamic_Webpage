#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import logging
import asyncio
from .data import add_city
from .scrape import scrape_parse, scrape_aqi_new, async_scrape_parse


logger = logging.getLogger(__name__)

major_cities = ('北京 上海 天津 重庆 杭州 哈尔滨 长春 沈阳 石家庄 太原 西安 济南 '
                '乌鲁木齐 拉萨 西宁 兰州 银川 郑州 南京 武汉 合肥 福州 南昌 长沙 '
                '贵阳 成都 广州 昆明 南宁 深圳')

cities = """
鞍山  安阳
保定  宝鸡  包头  北海  北京  本溪  滨州
沧州  长春  常德  长沙  常熟  长治  常州  潮州  承德  成都 赤峰  重庆
大连  丹东  大庆  大同  德阳  德州  东莞  东营
鄂尔多斯
佛山  抚顺  富阳  福州
广州  桂林  贵阳
哈尔滨  海口  海门  邯郸  杭州  合肥  衡水  河源  菏泽  淮安 呼和浩特  惠州  葫芦岛  湖州
江门  江阴  胶南  胶州  焦作  嘉兴  嘉峪关  揭阳  吉林  即墨 济南  金昌  荆州  金华  济宁  金坛  锦州  九江  句容
开封  克拉玛依  库尔勒  昆明  昆山
莱芜  莱西  莱州  廊坊  兰州  拉萨  连云港  聊城  临安  临汾 临沂  丽水  柳州  溧阳  洛阳  泸州
马鞍山  茂名  梅州  绵阳  牡丹江
南昌  南充  南京  南宁  南通  宁波
盘锦  攀枝花  蓬莱  平顶山  平度
青岛  清远  秦皇岛  齐齐哈尔  泉州  曲靖  衢州
日照  荣成  乳山
三门峡  三亚  上海  汕头  汕尾  韶关  绍兴  沈阳  深圳  石家庄 石嘴山  寿光  宿迁  苏州
泰安  太仓  太原  台州  泰州  唐山  天津  铜川
瓦房店  潍坊  威海  渭南  文登  温州  武汉  芜湖  吴江  乌鲁木齐 无锡
厦门  西安  湘潭  咸阳  邢台  西宁  徐州
延安  盐城  阳江  阳泉  扬州  烟台  宜宾  宜昌  银川  营口 义乌  宜兴  岳阳  云浮  玉溪
枣庄  张家港  张家界  张家口  章丘  湛江  肇庆  招远  郑州  镇江 中山  舟山  珠海  诸暨  株洲  淄博  自贡  遵义
"""


def dbcity_init():

    list_city = major_cities.split()
    # list_city = cities.split()
    for c in list_city:
        add_city(c)

    return list_city


def gen_year_month():

    year = ['2014', '2015', '2016']
    month = ['{:0>2}'.format(i) for i in range(1, 13)]
    result = ['201312']
    for y in year:
        for m in month:
            result.append(y + m)

    return result


def collect_one_city(city):

    for month in gen_year_month():
        scrape_parse(city=city, month=month)


def collect_one_city_new(city):

    scrape_aqi_new(city, gen_year_month())


def collect_all():

    for city in major_cities.split():
        collect_one_city_async(city)


def collect_one_city_async(city):

    logger.info("start to collect %s", city)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
            *(async_scrape_parse(city, m) for m in gen_year_month())
        )
    )
