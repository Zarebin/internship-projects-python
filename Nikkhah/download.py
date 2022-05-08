
import concurrent.futures
import urllib.request
import time
from insta_crawler import *


def download(url, filename):
    urllib.request.urlretrieve(url, filename)


def Main():

    session_id = "?????"
    file = "temp.txt"
    output = "out.txt"
    crawler = Crawler(file, output, session_id)

    urls, filenames = crawler.run()

    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     executor.map(download, urls, filenames)


if __name__ == '__main__':
    start_time = time.time()
    Main()
    print("--- %s seconds ---" %
          (time.time() - start_time))
