#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
import json
from pyquery import PyQuery as pq
import re

#pyquery allows you to make jquery queries on xml documents. The API is as much as possible the similar to jquery. pyquery uses lxml for fast xml and html manipulation.
#jQuery is a lightweight, "write less, do more", JavaScript library. The purpose of jQuery is to make it much easier to use JavaScript on your website.

#The crawler is divided into two parts, the first part gets the image link, and the second part saves the image locally 


#Get web page source code:

url = 'https://www.instagram.com/mehmooni.series/'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'cookie': 'mid=YmGL3gAEAAFNhVdZFnOPU6Ki6ybr; ig_did=99E292E6-889D-4BF8-9D26-9541953C8507; csrftoken=edk8DLMprGcJRCm3Lp2dkb79Iyfm4TJq; ds_user_id=2295717511; sessionid=2295717511:9oWJJmzQowaSrp:11; shbid="2187\0542295717511\0541683479519:01f72aacb892942735f6d62a94edf5e0e9cca06f325395e933fe6db5220c002a21e5116c"; shbts="1651943519\0542295717511\0541683479519:01f7f96de28e3220d6dc246f43f246f76b7cd0761bc300cc26f44b9690e8fb200eaf4d09"; rur="NAO\0542295717511\0541683486807:01f7a03c6e0c9d4cc9b1742a2aa7ac1c7839b8a31cfeb066ad3d8c18d108a9ef04cd9086"'
}

def get_urls(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:    
            print('request error status code：', response.status_code)        
    except Exception as e:
        print(e)
        return None
html = get_urls(url)
print(html)


# In[9]:


# get the photo url of a account (the first 12 one)
urls = []
doc = pq(html)
items = doc('script[type="text/javascript"]').items()

for item in items:
    if item.text().strip().startswith('window._sharedData'):
        js_data = json.loads(item.text()[21:-1])
        edges = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
        for edge in edges:
            url = edge['node']['display_url']
            print(url)
            urls.append(url)


# In[10]:


query_hash: '69cba40317214236af40e7efa697781d'
variables : {"id":"52097267763","first":12,"after":"QVFDSkZIY09uWnpycHNpb3BMdFJOdkk2ckk3UWNvT2I2M2sxMGVkdXF4Z0VCVnhxMzM5dXVTSDgzZ1dQaVBnVDFoOWdsaEV0UGxvd3VOdDZMdDNOekoxdA=="}


# In[12]:


urls = []
user_id = re.findall('"profilePage_([0-9]+)"', html, re.S)[0]
print('user_id：' + user_id)
doc = pq(html)
items = doc('script[type="text/javascript"]').items()
for item in items:
    if item.text().strip().startswith('window._sharedData'):
        js_data = json.loads(item.text()[21:-1])
        edges = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
        page_info = js_data["entry_data"]["ProfilePage"][1]["graphql"]["user"]["edge_owner_to_timeline_media"]['page_info']
        cursor = page_info['end_cursor']
        flag = page_info['has_next_page']
        for edge in edges:
            if edge['node']['display_url']:
                display_url = edge['node']['display_url']
                print(display_url)
                urls.append(display_url)
        print(cursor)


# In[7]:


import requests
while True:
    user_id = 2295717511
    cursor = "QVFCU0RLRGhiTjhKVXpFbXpDWGZRcHBkS0lxb2tWdVE3T3lIeDl4TXQ2TGd1R3ZMZGUtLUxOOEtKOEdxQTJYZTNxcHdFTmFCZ3VpMzgtc1NkbGpwb2VkeA=="
    uri = 'https://www.instagram.com/graphql/query/?query hash=69cba40317214236af40e7efa697781d'
    url = uri.format(user_id=user_id, cursor=cursor)
    print(url)
    url1= requests.get(url, headers= headers)
    text= url1.text
    js_data = get_json(url)
#     js_data = json.loads(text)
    infos = js_data['data']['user']['edge_owner_to_timeline_media']['edges']
    cursor = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    flag = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
    for info in infos:
        if info['node']['is_video']:
            video_url = info['node']['video_url']
            if video_url:
                print(video_url)
                urls.append(video_url)
        else:
            if info['node']['display_url']:
                display_url = info['node']['display_url']
                print(display_url)
                urls.append(display_url)
    print(cursor, True)
    # time.sleep(4 + float(random.randint(1, 800))/200)    # if count > 2000, turn on
return urls


# In[ ]:




