
from instagramy import InstagramUser
import requests
import time


path = r"C:/Users/PicoNet/Desktop/insta/posts/{}"


class Crawler():

    def __init__(self, file, output, session_id):
        self.file = file
        self.output = output
        self.session_id = session_id

    def run(self):
        with open(self.file, "r") as file:
            username_lines = file.readlines()
            ids = []
            for line in username_lines:
                try:
                    user = InstagramUser(
                        line.strip(), sessionid=self.session_id)

                    posts = user.posts

                    for i in posts:
                        current_post = posts[posts.index(i)]

                        post_id = current_post[6]
                        ids.append(post_id)
                        # print(post_id)

                except:
                    pass
            return ids


if __name__ == '__main__':
    start_time = time.time()
    session_id = "??????"
    file = "temp.txt"
    output = "out.txt"
    crawler = Crawler(file, output, session_id)

    ids = crawler.run()
    print("***********--- %s seconds ---***********" %
          (time.time() - start_time))

    for id in ids:
        response = requests.get(
            "https://www.instagram.com/p/{}/?__a=1".format(id))

        with open('out.txt', 'a') as file:
            r = "*****"+str(ids.index(id))+" ***** "+response.text
            file.writelines(r)
            file.write(str(response))
