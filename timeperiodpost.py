from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

# Use parameters to save diffrent metadata
L = instaloader.Instaloader(download_pictures=True,download_videos=False,download_comments=False,save_metadata=True)

# Login
username = input("Enter your username: ")
L.interactive_login(username=username)

# User Query
search = input("Enter Hashtag: ")
limit = int(input("How many posts to download: "))

# Hashtag object
hashtags = instaloader.Hashtag.from_name(L.context, search).get_posts()

# Download Period
SINCE = datetime(2021, 5, 1)
UNTIL = datetime(2021, 3, 1)

no_of_downloads = 0
for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, hashtags)):
    if no_of_downloads == limit:
        break
    print(post.date)
    L.download_post(post, "#"+search)
    no_of_downloads += 1