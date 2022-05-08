
from instagramy import InstagramUser
from datetime import datetime
import wget
import threading
import os


path = r"C:/Users/PicoNet/Desktop/instaCrawler/posts/"


class AsyncDownload(threading.Thread):

    def __init__(self, url, path):

        threading.Thread.__init__(self)
        self.url = url
        self.path = path

    def run(self):

        wget.download(self.url, self.path)

        print("Finished background download")


class Crawler():

    def __init__(self, file, output, session_id):
        self.file = file
        self.output = output
        self.session_id = session_id

    def run(self):
        urls = []
        filenames = []
        with open(self.file, "r") as file:
            username_lines = file.readlines()
            for line in username_lines:
                try:
                    user = InstagramUser(
                        line.strip(), sessionid=self.session_id)

                    posts = user.posts

                    for i in posts:
                        current_post = posts[posts.index(i)]
                        likes = current_post[0]
                        comments = current_post[1]
                        caption = current_post[2]
                        timestamp = current_post[4]
                        date = datetime.fromtimestamp(timestamp).date()
                        time = datetime.fromtimestamp(timestamp).time()
                        try:
                            location = current_post[5]['slug']
                        except:
                            location = current_post[5]

                        post_id = current_post[6]
                        url = current_post[9]

                        if current_post[3] == True:
                            filename = str(date)+'.mp4'
                            # filename = line.strip() + post_id+'.mp4'
                        else:
                            filename = str(date)+'.jpg'
                            # filename = line.strip() + post_id+'.jpg'

                        urls.append(url)
                        each_page_path = os.path.join(path, line.strip())
                        my_path = os.makedirs(each_page_path)
                        fullfilename = os.path.join(my_path, filename)
                        filenames.append(fullfilename)
                        print(post_id, likes, comments, date, location, time)
                except:
                    pass
        return urls, filenames
