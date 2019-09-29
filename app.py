from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)