import json
import requests

url = "https://www.instagram.com/graphql/query/"

header = {'cookie': 'mid=YcW3oAALAAHb-3X8gcUbKqsCpGVL; ig_did=1BB905EB-ECDC-4EDE-BA5D-2C3B713D3A3A; ig_nrcb=1; shbid=2703\0545999925105\0541683390517:01f77af3c771bcb5a840371728a27bb510fd1f9d5e67540cff14e494cabd9adb4cb9dff0;ds_user_id=5999925105; sessionid=5999925105%3ActYwaXHe2V8YDR%3A10; csrftoken=5B8ROM80IdAokhi7IPQs8Y7lMxDdeREJ; rur=ASH\0545999925105\0541683566331:01f70db36cd25592ebc9155f1e0222f0d9116744d743d441173f1adf3cfe21fc027a39dd'}
querystring = {"query_hash": "69cba40317214236af40e7efa697781d",
               "variables": "{\"id\":\"1434739621\",\"first\":50,\"after\":\"""\"}"}


def generate_querystring(end_cursor):
    querystring = {"query_hash": "69cba40317214236af40e7efa697781d",
                   "variables": "{\"id\":\"1434739621\",\"first\":50,\"after\":\""+end_cursor+"\"}"}
    return querystring


def request(querystring):
    response = requests.request(
        "GET", url, headers=header, params=querystring)
    response = json.loads(response.text)
    return response


response = request(querystring)

next_page = response['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
while next_page:
    end_cursor = response['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    querstring = generate_querystring(end_cursor)
    posts = response['data']['user']['edge_owner_to_timeline_media']['edges']
    for post in posts:
        print(post["node"]["display_url"])
    response = request(querstring)
    next_page = response['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
