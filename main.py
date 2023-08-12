import argparse
import os
import ssl
from os import remove as delFile

from moviepy.editor import VideoFileClip
from pytube import YouTube


def main():
    ssl._create_default_https_context = ssl._create_stdlib_context

    parser = argparse.ArgumentParser(
        prog="SFXDownloader",
        description="Downloads youtube videos and saves them as mp3 files")
    parser.add_argument("link", type=str, help="The YouTube link to download")
    parser.add_argument("-k", "--keep", action="store_true", help="Keep the mp4 file with the mp3")
    args = parser.parse_args()

    # Downloads file
    yt = YouTube(args.link)
    yt.streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download()

    # Converts mp4 to mp3
    filename, ext = os.path.splitext(f'{yt.title}.mp4')
    clip = VideoFileClip(f'{yt.title}.mp4')
    clip.audio.write_audiofile(f'{filename}.mp3')

    # Deletes mp4
    if not args.keep:
        delFile(f'{yt.title}.mp4')


if __name__ == "__main__":
    main()
