import pytube
import os
import re
videos = ["https://www.youtube.com/watch?v=4ZIZbFItiKc"]
for url in videos:
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        folder = f"./luca/{re.sub(r'[^A-Za-z0-9]', '', video.title)}"
        if os.path.isdir(folder):
            print(url)
            continue
        os.mkdir(folder)
        video.download(folder)
        os.rename(f"{folder}/{video.title}.mp4", f"{folder}/video.mp4")
    except Exception as e:
        print("fallito " + url)
        exit
