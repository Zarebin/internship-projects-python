from instagrapi import Client
import time
from downloadFile import download_media

def download_media(user_id, cl):
    media_count = cl.user_info(user_id).media_count
    print(media_count)
    medias = cl.user_medias(user_id, media_count)
    for media in medias:
 
        if media.media_type == 1:
            cl.photo_download(media.pk, './medias')
        elif media.media_type == 2 and media.product_type == 'feed':
            cl.video_download(media.pk, './medias')
        elif media.media_type == 2 and media.product_type == 'igtv':
            cl.igtv_download(media.pk, './medias')
        elif media.media_type == 2 and media.product_type == 'clips':
            cl.clip_download(media.pk, './medias')
        elif media.media_type == 8:
            cl.album_download(media.pk, './medias')


f = open("account.txt", "r")

ACCOUNT_USERNAME = f.readline().replace(" ", "")
ACCOUNT_PASSWORD = f.readline().replace(" ", "")

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
session_id = cl.sessionid


root_username = "google"
user_id = cl.user_id_from_username(root_username)



###########################################################
#estimate execution time for crawling instagram's posts
#########################################################

start = time.time()
media_count = cl.user_info(user_id).media_count
medias = cl.user_medias(user_id, media_count)
end = time.time()
print(str(end-start))
print(media_count)

