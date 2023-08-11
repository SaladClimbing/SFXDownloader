from io import BytesIO
from logging import error

import requests
from PIL import Image, ImageTk

from downloader import search


def get_resized_thumbnail(url, width):
    try:
        thumbnail_url = search(url)
    except:
        error("URL not found as YouTube")

    img_data = requests.get(thumbnail_url).content
    image_opened = Image.open(BytesIO(img_data))
    resized_image = image_opened.resize((int(width), int(width * 9 / 16)))
    img = ImageTk.PhotoImage(resized_image)
    return img
