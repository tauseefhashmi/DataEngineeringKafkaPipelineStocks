from kafka import KafkaProducer
import json
import urllib.request
import time

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey="+"N8IIJ8FGB7NS1CSM8"
print(url)
contents = urllib.request.urlopen(url).read()
json_data = json.loads(contents)
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('DE9', json.dumps(json_data).encode('utf-8'))
producer.flush()
producer.send('DE9', ("CLOSE").encode('utf-8'))
producer.flush()
print("CLOSE 1")
