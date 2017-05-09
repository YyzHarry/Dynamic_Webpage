#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import date
from pony.orm import Database, db_session, PrimaryKey, Required, Optional, Set
import logging


logger = logging.getLogger(__name__)
db = Database()


class City(db.Entity):

    id = PrimaryKey(int, auto=True)
    ch_name = Required(str)
    en_name = Optional(str)
    province = Optional(str)
    coordinates = Optional(str)
    a_q_is = Set('AQI')


class AQI(db.Entity):

    id = PrimaryKey(int, auto=True)
    date_aqi = Required(date)
    avgAQI = Required(int)
    minAQI = Required(int)
    maxAQI = Required(int)
    severitylevel = Required(int)
    pm2_5 = Required(float)
    pm10 = Required(float)
    so2 = Required(float)
    co = Required(float)
    no2 = Required(float)
    o3 = Required(float)
    ranking = Required(int)
    city = Required(City)

db.bind("sqlite", '../data/database_aqi.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def add_city(ch_name, en_name='', province='', coordinates=''):

    try:
        City(ch_name=ch_name, en_name=en_name, province=province,
            coordinates=coordinates)
    except Exception as E:
        logger.error("{}. \n {}".format(
            E, [ch_name, en_name, province, coordinates]))


@db_session
def add_aqi(date_aqi, avgAQI, minAQI, maxAQI, severitylevel, pm2_5, pm10, so2,
            co, no2, o3, ranking, city):

    try:
        AQI(date_aqi=date_aqi, avgAQI=avgAQI, minAQI=minAQI, maxAQI=maxAQI,
            severitylevel=severitylevel, pm2_5=pm2_5, pm10=pm10, so2=so2,
            co=co, no2=no2, o3=o3, ranking=ranking, city=city)
    except Exception as E:
        logger.error("{}. \n {}".format(E, [date_aqi, avgAQI, minAQI, maxAQI,
                severitylevel, pm2_5, pm10, so2, co, no2, o3, ranking, city]))


@db_session
def get_city(city=''):
    return City.get(ch_name=city).id
