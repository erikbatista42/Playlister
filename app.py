from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

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
    playlist_id = playlists.insert_one(playlist).inserted_id
    return redirect(url_for("playlists_show",playlist_id=playlist_id))

@app.route("/playlists/<playlist_id>")
def playlists_show(playlist_id):
    # show a single playlist
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_show.html', playlist=playlist)
if __name__ == '__main__':
    app.run(debug=True)