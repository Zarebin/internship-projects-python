
def download_media(user_id, cl):
    media_count = cl.user_info(user_id).media_count
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
