from threading import Thread

import customtkinter as ctk
from pytube import YouTube

from downloader import download


# --------------------- Selector Panel ---------------------
class SelectorPanel(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']

        self.pack_search()
        self.pack_options()
        self.pack_download()

    # <editor-fold desc="Packing Widgets"

    def pack_search(self):
        self.search_box = ctk.CTkEntry(self, height=25, width=200, font=('Helvetica', 18, 'bold'),
                                       placeholder_text="Insert Link Here")
        self.search_box.pack(padx=100, pady=5)

        self.search_button = ctk.CTkButton(self, height=25, width=200, text="Search", font=('Helvetica', 18, 'bold'))
        self.search_button.pack(padx=100, pady=5)

    def pack_options(self):
        self.keep_video = ctk.CTkCheckBox(self, height=25, width=200, font=('Helvetica', 18, 'bold'),
                                          text="Keep video file")
        self.keep_video.pack(padx=100, pady=25)

    def pack_download(self):
        self.download_button = ctk.CTkButton(self, height=25, width=200, font=('Helvetica', 18, 'bold'),
                                             text="Download", command=self.download)
        self.download_button.pack(padx=100, pady=50)

    # </editor-fold>

    # <editor-fold desc="Functionality">

    def download(self):
        download_thread = Thread(target=download, args=(self.search_box.get(), False))
        download_thread.start()

    def search(self):
        try:
            self.video = YouTube(self.search_box.get())
        except:
            return None
        return YouTube.thumbnail_url

    # </editor-fold>
