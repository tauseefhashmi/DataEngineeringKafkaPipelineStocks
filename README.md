# DataEngineeringKafkaPipelineStocks This is Apache Kafka Data Pipeline which takes in the stock data from Alphavanatage Web Api and fetches the data into the MySQL Database.
You first need to install Kafak into your system and run the following commands.
STEP 1: To Start Zookeeper
C:\kafka\bin\windows>zookeeper-server-start.bat C:\kafka\config\zookeeper.properties

STEP 2:To start Kafka Broker
C:\kafka>.\bin\windows\kafka-server-start.bat C:kafka\config\server.properties

Step 3:To Create topic
C:\kafka\bin\windows>kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

STep 4:Start Producer
C:\kafka\bin\windows>kafka-console-producer.bat --broker-list localhost:9092 --topic DE9

To create consumer
C:\kafka-2.12\bin\windows>kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic DE9 --from-beginning
