from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


client = MongoClient()
db = client.Playlister
playlists = db.playlists
    # mock array of objects
# playlists = [
#     { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
#     {'title': 'Favorite Music', 'description': ["Better not", "No fun"]}
# ]

app = Flask(__name__)
@app.route("/")
def playlists_index():
    # show all playlists
    return render_template("playlists_index.html", playlists=playlists.find())

@app.route("/playlists/new")
def playlist_new():
    return render_template("playlists_new.html")

@app.route("/playlists", methods=["POST"])
def playlist_submit():
    # submit a new playlist 
    print(request.form.to_dict())
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    return redirect(url_for("playlists_index"))

if __name__ == '__main__':
    app.run(debug=True)