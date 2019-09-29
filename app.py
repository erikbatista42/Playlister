from flask import Flask, render_template


# mock array of objects
playlists = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]

app = Flask(__name__)
@app.route("/")
def playlists_index():
    # show all playlists
    return render_template("playlists_index.html", playlists=playlists)


if __name__ == '__main__':
    app.run(debug=True)