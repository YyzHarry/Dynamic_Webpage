#encoding=utf-8
import requests
import re
import sqlite3
import os
import time

pattern_image = re.compile('<div class="scenery_image_detail">.*?<img src="(.*?)" alt="(.*?)">' , re.S)

def init_sqlite():
    db_name = "image.db"
    if os.path.exists(db_name):
        conn = sqlite3.connect(db_name)
    else:
        conn = sqlite3.connect(db_name)
        conn.execute('''CREATE TABLE IMAGE
                (ID INT PRIMARY KEY NOT NULL,
                URL TEXT NOT NULL,
                NAME TEXT NOT NULL,
                LOCATION TEXT NOT NULL,
                IMAGE_TIME INT NOT NULL);''')
    return conn

def download_image(url, name):
    r = requests.get(url, timeout = 5.)
    f = open('image/'+name, 'wb')
    f.write(r.content)
    return True

def get_image(count):
    base_url = "https://tianqi.moji.com/liveview/picture/"
    url = base_url + str(count)
    r = requests.get(url, timeout = 5.)
    content = r.text

    items = re.findall(pattern_image, content)
    if len(items)==0:
        return None, None
    else:
        item = items[0]
        name = item[0].split('/')[-1]
        #print name
        res = download_image(item[0], name)
        if res==None:
            return None, None
        #url image_name location
        return item[0], name, item[1]

def sql_write(conn, index, url, image_time, name, location):
    res = conn.execute('''INSERT INTO IMAGE (ID, URL, NAME, IMAGE_TIME, LOCATION) 
            VALUES(%d,'%s',%d,'%s','%s')'''%(index, url, int(image_time), name, location))
    conn.commit()
    #print "========"
    #print res

def run(begin_index, end_index):
    conn = init_sqlite()
    for i in range(begin_index, end_index):
        time.sleep(1)
        try:
            url, name, location = get_image(i)
            if url == None:
                #print "url is None"
                continue
            image_time = name[:11]
            sql_write(conn, i, url, image_time, name, location)
            print "success:",i , url, image_time, name, location
        except Exception, e:
            print "fail:", i
            pass

if __name__=="__main__":
    run(70147765 ,70147768)

