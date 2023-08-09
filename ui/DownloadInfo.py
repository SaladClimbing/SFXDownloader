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

        self.pack_thumbnail(
            "https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1280,h_720/https://blog.snappa.com/wp-content/uploads/2019/01/YouTube-Thumbnail-Dimensions.jpg")

    def pack_thumbnail(self, url):
        img_data = requests.get(url).content
        unedited_img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        img = unedited_img.resize((self.WIDTH, self.HEIGHT * 9 / 16))  # TODO FIX RESIZE
        self.thumbnail = ctk.CTkLabel(self, image=img, width=self.WIDTH, height=self.WIDTH * 9 / 16)
        self.thumbnail.pack()
