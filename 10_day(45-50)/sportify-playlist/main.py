import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import oauth2

SPOTIPY_CLIENT_ID = 'Your key'
SPOTIPY_CLIENT_SECRET = 'Your secret key'
SPOTIPY_REDIRECT_URI = 'http://example.com'

sp_oauth = oauth2.SpotifyOAuth(
    SPOTIPY_CLIENT_ID, 
    SPOTIPY_CLIENT_SECRET,
    SPOTIPY_REDIRECT_URI, 
    scope="playlist-modify-private", 
    show_dialog=True,
    # cache_path="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/10_day(45-50)/sportify-playlist/.cache"
    )

#------------------------ Get the access token ------------------------#

# ad = sp_oauth.get_access_token(as_dict=False)
# print(ad)

#------------------------ Get the access token ------------------------#

header = {
    "Authorization": "Bearer your_key"
}

sp = spotipy.Spotify(auth=header, oauth_manager=sp_oauth)
user_id = sp.current_user()["id"]
scrap_day = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

#------------------------ get 100 billboard songs of the day ------------------------#

URL = f"https://www.billboard.com/charts/hot-100/{scrap_day}/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_titles = soup.select(selector="li #title-of-a-story")
with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/10_day(45-50)/sportify-playlist/songs.txt", mode="w", encoding="utf-8") as f:
    for song in song_titles:
        f.write(f"{song.getText().strip()}\n")

#------------------------ add songs from the list_song to the playlist ------------------------#

with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/10_day(45-50)/sportify-playlist/songs.txt", mode="r", encoding="utf-8") as f:
    song_names = f.read().splitlines() # Readlines without endline

song_uris = []
year = scrap_day.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{scrap_day} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)