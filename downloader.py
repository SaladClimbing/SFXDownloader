import ssl
import subprocess
from os import remove as delFile

from pytube import YouTube


def download(link: str, keep: bool):
    ssl._create_default_https_context = ssl._create_stdlib_context

    # Downloads file
    yt = YouTube(link)
    yt.streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download()

    # Converts mp4 to mp3
    subprocess.run(f'ffmpeg -i "{yt.title}.mp4" "{yt.title}.mp3"', shell=True)

    # Deletes mp4
    if not keep:
        delFile(f'{yt.title}.mp4')
