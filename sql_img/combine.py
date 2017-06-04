#encoding=utf-8
import sqlite3
import time

aqi_db = sqlite3.connect("database_aqi.sqlite")
image_db = sqlite3.connect("image.db")

aqi_cursor = aqi_db.cursor()
image_cursor = image_db.cursor()

#get city
aqi_cursor.execute("SELECT * FROM CITY;")
city = aqi_cursor.fetchall()
citys = []
city_index = {}
for i,j in enumerate(city):
    citys.append(j[1])
    city_index[j[1]] = i+1

#print citys

#get his aqi
his_aqi_index = {}
aqi_cursor.execute("SELECT date_aqi, avgAQI, pm2_5, city FROM AQI;")  
his_aqi = aqi_cursor.fetchall()
for i in his_aqi:
    his_aqi_index[i[0]+str(i[3])] = i[1]

#get image
image_cursor.execute("SELECT NAME, LOCATION, IMAGE_TIME FROM IMAGE;")  
images = image_cursor.fetchall()

def write_result(conn, id, aqi, image):
    res = conn.execute('''INSERT INTO AQIIMAGE (ID, IMAGE, AQI) 
            VALUES(%d, '%s', %d)'''%(id, image, aqi))
    conn.commit()
    print aqi, image

db_name = "aqi_image.db"
conn = sqlite3.connect(db_name)
conn.execute('''CREATE TABLE AQIIMAGE
        (ID PRIMARY KEY NOT NULL,
        IMAGE NOT NULL,
        AQI INT NOT NULL);''')


count = 0
for image in images:
    location = image[1]
    image_time = image[0]
    image_time = int(image_time)/10
    image_time = time.localtime(image_time)
    image_time = time.strftime("%Y-%m-%d",image_time)
    for i in citys:
        if i in location:
            index = image_time+str(city_index[i])
            if index in his_aqi_index:
                aqi = his_aqi_index[index]
                write_result(conn, count, aqi, image[2])
                count += 1
            break

