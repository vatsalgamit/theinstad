from flask import Flask,render_template,request, redirect
from igpost import *
from ghostfollowers import search_ghosts

app = Flask(__name__)


@app.route('/downloadposts', methods=["GET", "POST"])
def wimsgdemo():
    if request.method == "POST":        
        USER=request.form.get('uname')
        cred=request.form.get('password')
        print('-'*100)
        print(f"Username:{USER}, Password:{cred}")
        print('-'*100)
        post_number=request.form.get('nopo')
        if USER !=None and cred !=None and post_number!=None:
            postDownload(USER,cred,post_number)
            return render_template("index.html")
    return render_template("vatsal.html")

@app.route('/', methods=["GET","POST"])
def searchghosts():
    if request.method == "POST":        
        USER=request.form.get('uname')
        cred=request.form.get('password')
        print('-'*100)
        print(f"Username:{USER}, Password:{cred}")
        print('-'*100)
        if USER !=None and cred !=None:
            Ghosts = search_ghosts(USER,cred)
            return render_template("ghostlist.html",len = len(Ghosts),Ghosts=Ghosts)
    return render_template("ghost.html")
    
if __name__ == '__main__':
    app.run(host='localhost',port='5051',debug=True)


