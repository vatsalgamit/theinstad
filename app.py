from flask import Flask,render_template,request, redirect
from ghostfollowers import search_ghosts
from logfile import get_logs

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def searchghosts():
    if request.method == "POST":        
        USER=request.form.get('uname')
        cred=request.form.get('password')
        if USER !=None and cred !=None:
            Ghosts = search_ghosts(USER,cred)
            return render_template("ghostlist.html",len = len(Ghosts),Ghosts=Ghosts)
    return render_template("ghost.html")
 
    
if __name__ == '__main__':
    app.run(threaded=True, port=5000)


