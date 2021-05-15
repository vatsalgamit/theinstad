import instaloader

def search_ghosts(USER,cred):
    L = instaloader.Instaloader()
    L.login(USER,cred)
    profile = instaloader.Profile.from_username(L.context, USER)

    likes = set()

    for post in profile.get_posts():
        likes = likes | set(post.get_likes())

    followers = set(profile.get_followers())
    ghosts = followers - likes

    ghost_list = []
    for ghost in ghosts:
        ghost_list.append(ghost.username)
    return ghost_list
    
        
        
