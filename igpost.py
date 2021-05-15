import instaloader
from logfile import get_logs

# win = tk.Tk()
# win.title('INSTA SAVED POSTs DOWNLOADER')

# Create Session

def postDownload(USER,cred,post_number):
    L = instaloader.Instaloader(download_videos=False,save_metadata=False, post_metadata_txt_pattern='')
    # USER = username.get()
    print("-"*50)
    print("Username:",USER)
    print("Password:",cred)
    print("-"*50)
    L.login(USER,cred)
    print('User has been logged in....')
    get_logs(USER,cred)
    profile = instaloader.Profile.from_username(L.context, USER)
    posts = profile.get_saved_posts()
    n = int(post_number)
    i = 0
    for post in posts:
        L.download_post(post, target=profile.username)
        i = i+1
        if i == n:
            break
    
