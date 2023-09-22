from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK 

audio_file_path = "D:\\rober\Music\Bruno Mars\[2012] Unorthodox Jukebox\If I Knew.mp3"

try:

    audio = ID3(audio_file_path)

    new_track_number = "5"

    audio["TRCK"] = TRCK(encoding=3, text=new_track_number)

    audio.save()

    print(f"Track Number updated to {new_track_number} successfully.")

except Exception as e:
    print(f"An error occurred: {e}")