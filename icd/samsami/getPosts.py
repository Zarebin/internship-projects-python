import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from kafka import KafkaProducer


def get_all_publisher_id():
    with open('pub_ids.txt') as f:
        lines = f.readlines()

    lines = [s.replace("\n", "") for s in lines]
    lines = [s for s in lines if s != ""]
    lines = list(set(lines))
    return lines


def get_json_posts_by_pub_id(pub_id: str, page_token=""):
    querystring = {"query_hash": "69cba40317214236af40e7efa697781d",
                   "variables": "{\"id\":\"" + pub_id + "\",\"first\":50,\"after\":\"" + page_token + "\"}"}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return json.loads(response.text)


def get_all_posts_by_id(pub_id: str):
    page_token = ""
    post_count = 0
    has_next_page = True
    print(pub_id)
    while has_next_page:
        response = get_json_posts_by_pub_id(pub_id,page_token)
        response = response["data"]["user"]["edge_owner_to_timeline_media"]
        has_next_page = response["page_info"]["has_next_page"]
        page_token = response["page_info"]["end_cursor"]
        edges= response["edges"]

        for edge in edges:
            post_count += 1
            data = {
                    'id': pub_id,
                    'post_count': post_count,
                    'url': edge['node']['display_url']
            }
            producer.send('quickstart-events', value=data)

    print(f"id: {pub_id} , post_count:{post_count}")


if __name__ == "__main__":
    # Connect to Kafka as producer
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))


    publisher_ids = get_all_publisher_id()
    start = time.time()

    with ThreadPoolExecutor(1) as executor:
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'cookie': 'mid=Ym1IKgALAAGL0dnch3IjDnh87s93; ig_did=AC580E9D-CDCB-4426-AE68-870833FB5404; csrftoken=HakG2y577wSrcvIcsHzPN8OcqDDscY04; ds_user_id=52951481931; sessionid=52951481931%3AqH099i6yC1cEcu%3A7; rur="LDC\05452951481931\0541682865412:01f7f87e0ad07e322d4e19be600d64484c0976ce8d062a2a6ed25accbabd79258e3e28d2'
        }
        url = "https://www.instagram.com/graphql/query/"
        for result in executor.map(get_all_posts_by_id, publisher_ids[:1]):
            print(result)

    print(time.time()-start)
