from kafka.admin import KafkaAdminClient, NewTopic
import json
from kafka import KafkaConsumer
import pymysql    #for connection to MySQL Database
import time

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

db = pymysql.connect("localhost", "root", "password", "de9")    #connection to MySQL Database
cursor = db.cursor()

KafkaConsumer(consumer_timeout_ms=1000)
consumer = KafkaConsumer("DE9", bootstrap_servers=['localhost:9092'], group_id=None
                          ,
                          auto_offset_reset='earliest'
)

cursor.execute("truncate table DE9.Currency")

for msg in consumer:
    #print(msg)
    if msg.value.decode('utf8') == "CLOSE":
        consumer.close()
        break
    else:
        tmp = json.loads(msg.value.decode('utf8')).get('Time Series (Daily)')
        metadata = json.loads(msg.value.decode('utf8')).get('Meta Data')
        Information = metadata.get('1. Information')
        Symbol = metadata.get('2. Symbol')
        LastRefreshed = metadata.get('3. Last Refreshed')
        OutputSize = metadata.get('4. Output Size')
        Timezone = metadata.get('5. Time Zone')
        Open = "1. open"
        High ="2. high"
        Low ="3. low"
        Close ="4. close"
        Volume ="5. volume"
        #print(metadata)                    #for checking purpose
        #print(First,Second,LastRefreshed,OutputSize,Timezone)      #for checking purpose
        keyss = tmp.keys()
        
        
    for f in keyss:
        sql = "Insert into Currency values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (Information,Symbol,LastRefreshed,OutputSize,Timezone,tmp[f].get(Open),tmp[f].get(High),tmp[f].get(Low),tmp[f].get(Close),tmp[f].get(Volume))
        cursor.execute(sql, val)
        db.commit()
        print("Inserted")                 #for checking whether the values are inserted into database MYSQL or not
