import os.path
import ssl
from os import remove as delFile

from moviepy.editor import VideoFileClip
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

    convert_video_to_audio(f'{yt.title}.mp4')

    # Deletes mp4
    if not keep:
        delFile(f'{yt.title}.mp4')


def convert_video_to_audio(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f'{filename}.{output_ext}')


def search(url):
    video = YouTube(url)
    return video.thumbnail_url
