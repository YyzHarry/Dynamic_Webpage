#!/usr/bin/python

import cgi
import urllib
import urllib2
import os
import random
import sqlite3
import sys
import cPickle as pkl
import re
import requests

reload(sys)
sys.setdefaultencoding("utf8")

def get_aqi(lat,lng):
    host = 'http://aliv2.data.moji.com'
    path = '/whapi/json/aliweather/briefaqi'

    method = 'POST'
    appcode = 'b090a50982d84d4ca9e4e68f517f100a'
    querys = ''
    bodys = {}
    url = host + path

    bodys['lat'] = lat
    bodys['lon'] = lng
    bodys['token'] = 'b87cea6abc73f77148534e03adff4d09'
    post_data = urllib.urlencode(bodys)
    request = urllib2.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)

    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    try:
        #print "abcd"
        response = urllib2.urlopen(request)
        content = response.read()
        content = eval(content)
        #print content
        return content["data"]["aqi"]["value"]
    except Exception,e:
        #print Exception,e
        #print lat, lng
        #print "fail to get aqi"
        return None

def get_files(path_name):
    for parent, dirnames, filenames in os.walk(path_name):
        return filenames

def get_image_by_aqi(aqi):
    
    image_db = sqlite3.connect("aqi_image.db")
    image_cursor = image_db.cursor()
    image_cursor.execute("select IMAGE from AQIIMAGE order by abs(AQI-%s) limit 0,1;"%(aqi))  
    images = image_cursor.fetchall()
    return "http://t.eecser.com/image/"+images[0][0]
    '''
    files = get_files("/home/fzx/apache/install/htdocs/image")
    files_count = len(files)
    chose = random.randint(0, files_count-1)
    return files[chose]
    '''
def get_image_by_location(location):
    location = location.decode("utf-8")
    location2url = pkl.load(open("location2url.pkl","rb"))
    if location in location2url:
        url = location2url[location]
        res = requests.get(url)
        res = res.text
        pattern = re.compile('data-original="(.*?)"')
        items = re.findall(pattern, res)
        result = []
        for item in items:
            result.append(item)
        return result[0]
    else:
        return None

#print "Content-type:text/html\r\n"  
'''
form = cgi.FieldStorage()
lat = form.getvalue('lat')
lng = form.getvalue('lng')
province=form.getvalue('province')
city=form.getvalue('city')
district=form.getvalue('district')
street=form.getvalue('street')
streetNumber=form.getvalue('streetNumber')
'''

lat = float(sys.argv[1])
lng = float(sys.argv[2])
district = sys.argv[3]
province = "unknow"
city = "unknow"
street = "unknow"
streetNumber = "unknow"



for i in range(3):
    aqi = get_aqi(lat, lng)
    if aqi!=None:
        break

#print "BBBB"
if aqi==None:
    aqi = "fail"
    image = "fail"
else:
    #image = get_image_by_aqi(aqi)
    image = get_image_by_location(str(district))
    if image == None:
        image = get_image_by_aqi(aqi)
    aqi = str(aqi)

'''
print province
print city
print district
print street
print streetNumber
'''
try:
    print '{"aqi":"'+aqi+'", "image":"'+image+'", "province":"'+str(province)+'", "city":"'+str(city)+'", "district":"'+str(district)+'", "street":"'+str(street)+'", "streetNumber":"'+str(streetNumber)+'"}'
except Exception,e:
    print e
#print '{"aqi":"'+aqi+'", "image":"'+image+'"}'
