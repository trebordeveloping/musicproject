from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json

from authorisation import get_token
from functions import (
    search_for_artist,
    get_songs_by_artist,
    get_albums_by_artist,
    get_album_tracks,
    fetch_album_info
)

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

token = get_token()

with open("artists.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file]

output_files = []

for artist_name in input_data:

    print(artist_name)

    result = search_for_artist(token, artist_name)
    artist_id = result["id"]
    songs = get_songs_by_artist(token, artist_id)
    albums = get_albums_by_artist(token, artist_id)

    artist_path = f"outputs\{artist_name}"
    os.makedirs(artist_path, exist_ok=True)
    toptracks_filename = f"{artist_name} - TOP TRACKS"

    print("Fetching top tracks...",end=" ")

    with open(f"{artist_path}\{toptracks_filename}.txt", "w") as output_file:

        output_file.write(toptracks_filename + "\n\n")
                           
        for idx, song in enumerate(songs):
            name = song["name"]
            output_file.write(f"{idx + 1}. {name}\n")

    print("Done\nFetching albums...",end=" ")

    for album in albums:
        fetch_album_info(token, artist_name, album)         

    print("Done")
    print()