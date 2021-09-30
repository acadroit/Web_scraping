import requests
from bs4 import BeautifulSoup
import html5lib
import lxml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import cred
import pprint

date = input("Which year's song you want to listen to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/"+ date).text
parse=BeautifulSoup(response,"lxml")
#print(parse.prettify())
# print(parse.title.string)


# here, I am fetching all the anchor links
# link=[links.get("href") for links in parse.find_all('a')]
# print(link)


# Here I am fetching all the song names 
song= parse.find_all("span",class_="chart-element__information__song")
song_name=[value.get_text() for value in song]


#Below code is used to authorize with spotify
scope="playlist-modify-private"

#Here I am authenticating
spotify_ = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url,scope=scope))
user_id = spotify_.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_name:
    result = spotify_.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = spotify_.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
spotify_.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
