import requests
from flask import Flask,request,render_template,redirect
import json

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

genres = {
	"rock": [ "queen"],
	"alternative rock": ["arctic monkeys"],
	"pop": [ "tarkan"],
	"blues": [ "robert johnson"],
	"country": ["johnny cash"],
	"electronic": ["daft punk"],
	"jazz": [ "miles davis"],
	"r&b": [ "sam cooke"],
	"rap": ["eminem"],
	"reggae": ["bob marley"]
}
ids = {
    "queen":"1dfeR4HaWDbWqFHLkxsg1d",
    "arctic monkeys":"7Ln80lUS6He07XvHI8qqHH",
    "tarkan":"2yMN0IP20GOaN6q0p0zL5k",
    "robert johnson" : "0f8MDDzIc6M4uH1xH0o0gy",
    "johnny cash" : "6kACVPfCOnqzgfEF5ryl0x",
    "daft punk" : "4tZwfgrHOc3mvqYlEYSvVi",
    "miles davis" : "0kbYTNQb4Pb1rPbbaF0pT4",
    "sam cooke" : "6hnWRPzGGKiapVX1UCdEAC",
    "eminem" : "7dGJo4pcD2V6oG8kP0tJRR",
    "bob marley" : "6BH2lormtpjy3X9DyrGHVj"
}

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        option = request.form['options']
        inputValue = request.form["inputValue"]

        if (option == "genre"):
            return redirect('/tracks/' + inputValue)
        else:
            return redirect('/tracks/byName/' + inputValue)

    else:
        return render_template("index.html")

@app.route('/tracks/<genre>')
def getTracksByGenre(genre):
    artists=genres[genre]

    print(genre , artists)
    tracks = []
    for artist in artists:
        artist_id = ids[artist]
        artistTracks = search(artist_id)
        tracks.append(artistTracks.json())
    print(tracks)
    return render_template("TrackList.html",tracks = tracks)

@app.route('/tracks/byName/<name>')
def getTracksByName(name):

    tracks = []
    artist_id = ids[name]
    artistTracks = search(artist_id)
    tracks.append(artistTracks.json())
    print(tracks)
    return render_template("TrackList.html",tracks = tracks)



def search(artist_id):
    CLIENT_ID = 'da1889f39c9a4b9a83f125337a1042f3'
    CLIENT_SECRET = '04731c3b39724b6980ef8298386ebeef'

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    BASE_URL = 'https://api.spotify.com/v1/'

    tracks = requests.get(BASE_URL + 'artists/' + artist_id + '/top-tracks', headers=headers,
                          params={'limit': 10,'country':'US'})

    return tracks
