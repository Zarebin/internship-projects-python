Step1:
If you want to get id from publisher_id:
1- Put your publisher names in publisher_name.txt
2- Run getUserID.py
3- The results will store in pub_ids.txt

Step2:
Get Posts by publisher_id and send to store in kafka:
1- Make a topic in kafka and name it 'quickstart-events'
2- Run Zookeeper and Kafka 
3- Run getPosts.py and consumer.py in separate terminals