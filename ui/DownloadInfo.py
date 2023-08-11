import customtkinter as ctk

from ui.ImageManipulation import get_resized_thumbnail


class DownloadInfo(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']

        self.pack_thumbnail(
            "https://www.youtube.com/watch?v=wWltASCJO-U")

    def pack_thumbnail(self, url):
        img = get_resized_thumbnail(url, self.WIDTH)
        self.thumbnail = ctk.CTkLabel(self, image=img, width=self.WIDTH, height=self.WIDTH * 9 / 16)
        self.thumbnail.pack()
