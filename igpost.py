import instaloader
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import messagebox
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
    print('Download Successful')
    # messagebox.showinfo("Status","Posts Saved Successfully")

# img = Image.open('ig.png')
# resized_img = img.resize((150,100),Image.ANTIALIAS)
# img = ImageTk.PhotoImage(resized_img)

# image = tk.Label(win,image=img)
# image.grid(row=0,column=1)

# label = tk.Label(win,text = 'Enter Username: ')
# label.grid(row = 2,column=0)
# username = tk.Entry(win,width=40)
# username.grid(row=2,column=1)


# label = tk.Label(win,text = 'Enter Password: ')
# label.grid(row = 3,column=0)
# cred = tk.Entry(win,width=40,show = "*")
# cred.grid(row=3,column=1)

# label = tk.Label(win,text = 'How many posts?: ')
# label.grid(row = 6,column=0)
# post_number = tk.Entry(win,width=40)
# post_number.grid(row=6,column=1,pady=20)

# btn = tk.Button(win,text = 'Download',command = postDownload)
# btn.grid(row = 7,column=1,pady=20)
# win.mainloop()
