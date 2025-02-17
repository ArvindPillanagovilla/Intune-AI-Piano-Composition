import os
import subprocess

# Path to MuseScore executable (update this to the actual path where MuseScore is installed)
musescore_path = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"

# Path to the .mid file you want to open
mid_file_path = r"C:\Users\adith\Downloads\Intune-AI music composition\mel.mid"

# Use subprocess to open MuseScore with the specified .mid file
def open_musescore(mid_file_path):
    try:
        # Launch MuseScore with the .mid file as an argument
        subprocess.run([musescore_path, mid_file_path], check=True)
        print(f"Opening {mid_file_path} in MuseScore.")
    except Exception as e:
        print(f"Error opening MuseScore: {e}")

# Call the function to open the .mid file in MuseScore
open_musescore(mid_file_path)
