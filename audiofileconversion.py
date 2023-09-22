import os
from pydub import AudioSegment
import ffmpeg

input_directory = "D:\\rober\Music\Bruno Mars\[2012] Unorthodox Juxebox"
output_directory = "D:\\rober\Music\Bruno Mars\[2012] Unorthodox Jukebox\mp3files"
os.makedirs(output_directory, exist_ok=True)

def convert_m4a_to_mp3(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="mp3")

files = []

for file_name in os.listdir(input_directory):
    if file_name.endswith(".m4a"):
        input_file_path = os.path.join(input_directory, file_name)
        modification_time = os.path.getmtime(input_file_path)
        files.append((file_name, input_file_path, modification_time))

print("Sorting with respect to time modified...", end=" ")
files.sort(key=lambda x: x[2])
print("Done")
print("Converting to " + output_directory + "\n")

for file_name, input_file_path, _ in files:

    output_file_path = os.path.join(output_directory, os.path.basename(file_name).replace(".m4a", ".mp3"))

    print(f" - Converting: {file_name}...", end=" ")

    try:
        convert_m4a_to_mp3(input_file_path, output_file_path)
        print("Done")

    except Exception as e:
        print(f"Error converting {file_name}: {str(e)}")


