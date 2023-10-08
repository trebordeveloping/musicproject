from authorisation import get_auth_header
from requests import get
import json
import csv
import os
from PIL import Image # url to image
from io import BytesIO # url to image
from pydub import AudioSegment # audio file type conversion

def path_friendly(name):

    name = name.replace("\\", " ").replace("/", " ")
    name = name.replace("<", " ").replace(">", " ")
    name = name.replace(":", " ").replace("*", " ").replace("?", " ").replace("\"", " ").replace("|", " ")
    return name

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result

def get_album_tracks(token, album_id, limit=20):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks?limit={limit}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result

def fetch_album_info(token, artist_name, artist_path, album):
    album_id = album["id"]
    album_name = album["name"]
    album_year = album["release_date"][:4]
    album_date = album["release_date"]
    album_tracks = get_album_tracks(token, album_id, album["total_tracks"])
    album_cover = album["images"][0]["url"]

    album_path = f"{artist_path}\[{album_year}] {path_friendly(album_name)}"
    os.makedirs(album_path, exist_ok=True)
    album_filename = f"{artist_name} · [{album_year}] {path_friendly(album_name)}"
    
    url_to_image(album_cover, f"{album_path}\{album_filename} (Album Cover)")

    with open(f"{album_path}\{album_filename}.csv", "w") as output_csv:

        for i, track in enumerate(album_tracks):
            track_name = track["name"]
            track_title = track["name"]
            track_disc = track["disc_number"]
            track_num = track["track_number"]
            track_artists = "/".join([artist["name"] for artist in track["artists"]])
            track_comment = track["external_urls"]["spotify"]
            idx = "0"+str(i+1) if i<9 else str(i+1)

            track_filename = f"{idx}. {path_friendly(track_name)} - {artist_name} · {path_friendly(album_name)} [{album_year}]"

            output_csv.write(",".join([track_filename, track_name, track_artists, artist_name, album_name, str(track_num), str(track_disc), album_date, track_comment]))
            output_csv.write("\n")

def url_to_image(image_url, image_path, message=False):

    try:

        # Send an HTTP GET request to download the image
        response = get(image_url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # read the image data from the response content
            image_data = response.content

            # create a PIL Image object from the image data
            img = Image.open(BytesIO(image_data))

            # save the image to the local file
            img.save(image_path + ".jpg")

            if message:
                print(f"Image downloaded and saved as {image_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_m4a_to_mp3(input_file_path, output_file_path):
    audio = AudioSegment.from_file(input_file_path, format="m4a")
    audio.export(output_file_path, format="mp3")

def artist_check(artist):

    with open("artist album info\\artists.txt", "r") as input_file:
        for line in input_file:
            if line.strip() == artist:
                return True
    
    return False