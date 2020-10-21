import os
import sys
import subprocess
from scenedetect import VideoManager
from scenedetect import SceneManager
from scenedetect.detectors import ContentDetector

folders = os.listdir("./name")
threshold = int(sys.argv[1]) if len(sys.argv) > 1 else 35

for folder in folders:
    folder_path = f"{os.getcwd()}/name/{folder}"
    video_file_path = f"{folder_path}/video.mp4"
    print(video_file_path);
    command = f"scenedetect --input {video_file_path} --output {folder_path} detect-content --threshold {threshold} list-scenes save-images"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
