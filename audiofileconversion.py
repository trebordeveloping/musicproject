import os
from pydub import AudioSegment
import ffmpeg
import shutil

def convert_m4a_to_mp3(input_dir):

    m4a_files = [] # list of m4a files in input directory

    for file in os.listdir(input_dir): # loop through input directory

        if file.endswith(".m4a"): # choose m4a files

            file_path = os.path.join(input_dir, file) # save file path of file
            file_modtime = os.path.getmtime(file_path) # find time modified of file
            m4a_files.append((file, file_path, file_modtime)) # save information in list
        
    m4a_files.sort(key=lambda x:x[2]) # sort with respect to time modified
    new_dir = os.path.join(input_dir, "m4a") # new directory for m4a files
    os.makedirs(new_dir, exist_ok=True) # create it if it doesn't already exist
        
    for file, old_file_path, _ in m4a_files:
        # move to m4a directory
        new_file_path = os.path.join(new_dir, file)
        shutil.move(old_file_path, new_file_path)
        # convert to mp3
        audio = AudioSegment.from_file(new_file_path, format="m4a")
        audio.export(old_file_path[:-4]+".mp3", format="mp3")

