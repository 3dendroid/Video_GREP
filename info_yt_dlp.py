# Program to get info about youtube video
import json

import yt_dlp

URL = 'https://www.youtube.com/watch?v=1psQmdieFsU&ab_channel=DorothyGale'

# See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ydl.sanitize_info makes the info json-serializable
    print(json.dumps(ydl.sanitize_info(info)))
