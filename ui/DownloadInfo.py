from io import BytesIO

import customtkinter as ctk
import requests
from PIL import ImageTk, Image


class DownloadInfo(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']

        self.pack_thumbnail("LINKHERE")

    def pack_thumbnail(self, url):
        img_data = requests.get(url).content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        self.thumbnail = ctk.CTkLabel(self, image=img)
        self.thumbnail.pack()
