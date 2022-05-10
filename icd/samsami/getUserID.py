from concurrent.futures import ThreadPoolExecutor
import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'cookie': 'mid=Ym1IKgALAAGL0dnch3IjDnh87s93; ig_did=AC580E9D-CDCB-4426-AE68-870833FB5404; csrftoken=HakG2y577wSrcvIcsHzPN8OcqDDscY04; ds_user_id=52951481931; sessionid=52951481931%3AqH099i6yC1cEcu%3A7; rur="LDC\05452951481931\0541682865412:01f7f87e0ad07e322d4e19be600d64484c0976ce8d062a2a6ed25accbabd79258e3e28d2'
}

url = "https://www.instagram.com/web/search/topsearch/"


def store_user_id(user_id: str):
    with open("pub_ids.txt", "a") as f:
        f.write(user_id+"\n")


def get_user_id(username: str):
    querystring = {"query": f"{username}"}
    response = requests.request(
        "GET", url,  headers=headers, params=querystring)
    response = json.loads(response.text)
    return response["users"][0]["user"]["pk"]


def get_publisher_names():
    with open('publisher_name.txt') as f:
        lines = f.readlines()
        lines = [s.replace("\n", "") for s in lines]
        lines = [s for s in lines if s != ""]
        lines = list(set(lines))
        return lines


if __name__ == '__main__':

    pub_names = get_publisher_names()

    with ThreadPoolExecutor(1) as executor:
        for result in executor.map(get_user_id, pub_names):
            store_user_id(result)


