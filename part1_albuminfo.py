# PUBLIC LIBRARIES
import os

# LOCAL FILES
from authorisation import get_token
from functions import (
    search_for_artist,
    get_albums_by_artist,
    fetch_album_info
)

# STEP 1: Take artists as input.

with open("artists.txt", "r") as input_file:
    artists_list = [line.strip() for line in input_file]

# STEP 2: Collect information on albums.

token = get_token()

for i in range(len(artists_list)):

    artist = artists_list[i].split(",")
    if len(artist)>1:
        print(f"{artist[0]}: done")
        continue
    else:
        print(f"{artist[0]}: fetching...")
        artist=artist[0]

    result = search_for_artist(token, artist)
    artist_id = result["id"]
    artist = result["name"]
    artist_albums = get_albums_by_artist(token, artist_id)

    artist_path = f"D:\\rober\Music\{artist}"
    os.makedirs(artist_path, exist_ok=True) # create dir if it doesn't exist yet
    
# STEP 3: Store in files (txt/csv).

    for album in artist_albums:
        fetch_album_info(token, artist, artist_path, album)

    # mark artist as done
    artists_list[i] += ",done"
    print(" "*len(artist) + f"  done ({len(artist_albums)} albums)\n")

# STEP 4: Update input file

    with open("artists.txt", "w") as output_file:

        for line in artists_list:
            output_file.write(line + "\n")
