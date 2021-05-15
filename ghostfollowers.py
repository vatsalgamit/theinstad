import instaloader

# L = instaloader.Instaloader()

# USER = input('Enter Username: ')
# PROFILE = USER

# # Load session previously saved with `instaloader -l USERNAME`:
# L.interactive_login(USER)

# profile = instaloader.Profile.from_username(L.context, PROFILE)

# likes = set()
# print("Fetching likes of all posts of profile {}.".format(profile.username))
# for post in profile.get_posts():
#     print(post)
#     likes = likes | set(post.get_likes())

# print("Fetching followers of profile {}.".format(profile.username))
# followers = set(profile.get_followers())

# ghosts = followers - likes

# print("Storing ghosts into file.")
# # with open("inactive-users.txt", 'w') as f:
# #     for ghost in ghosts:
# #         print(ghost.username, file=f)

# ghost_list = []
# for ghost in ghosts:
#     ghost_list.append(ghost.username)
    
# print(ghost_list)


# Function to get followers

def search_ghosts(USER,cred):
    L = instaloader.Instaloader()
    L.login(USER,cred)
    profile = instaloader.Profile.from_username(L.context, USER)

    likes = set()
    print("Fetching likes of all posts of profile {}.".format(profile.username))
    for post in profile.get_posts():
        print(post)
        likes = likes | set(post.get_likes())

    print("Fetching followers of profile {}.".format(profile.username))
    followers = set(profile.get_followers())

    ghosts = followers - likes

    print("Storing ghosts into file.")
    # with open("inactive-users.txt", 'w') as f:
    #     for ghost in ghosts:
    #         print(ghost.username, file=f)

    ghost_list = []
    for ghost in ghosts:
        ghost_list.append(ghost.username)
        
    print(ghost_list)
    return ghost_list
    
        
        
