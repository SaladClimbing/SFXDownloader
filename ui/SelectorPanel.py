import tkinter as tk
from datetime import timedelta
from threading import Thread

import customtkinter as ctk
from pytube import YouTube

from downloader import download, search
from ui.ImageManipulation import get_resized_thumbnail


# --------------------- Selector Panel ---------------------
class SelectorPanel(ctk.CTkFrame):
    def __init__(self, root, download_info, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root
        self.download_info = download_info

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

        self.search_button = ctk.CTkButton(self, height=25, width=200, text="Search", font=('Helvetica', 18, 'bold'),
                                           command=self.search_button_clicked)
        self.search_button.pack(padx=100, pady=5)

    def pack_options(self):
        self.keep_video = ctk.CTkCheckBox(self, height=25, width=200, font=('Helvetica', 18, 'bold'),
                                          text="Keep video file", state=tk.DISABLED)
        self.keep_video.pack(padx=100, pady=25)

    def pack_download(self):
        self.download_button = ctk.CTkButton(self, height=25, width=200, font=('Helvetica', 18, 'bold'),
                                             text="Download", state=tk.DISABLED, command=self.download)
        self.download_button.pack(padx=100, pady=50)

    # </editor-fold>

    # <editor-fold desc="Functionality">

    def download(self):
        download_thread = Thread(target=download, args=(self.search_box.get(), False))
        download_thread.start()

    def search_button_clicked(self):
        url = self.search_box.get()
        self.change_thumbnail(url)
        self.video = YouTube(url)
        self.change_details(self.video)
        self.enable_buttons()

    def change_thumbnail(self, url):
        self.download_info.thumbnail.configure(image=get_resized_thumbnail(search(url), self.download_info.WIDTH))

    def change_details(self, video: YouTube):
        self.download_info.title_label.configure(text=f"Title: {video.title}")
        self.download_info.author_label.configure(text=f"Author: {video.author}")
        self.download_info.time_label.configure(text=f"Duration: {str(timedelta(seconds=video.length))}")

    def enable_buttons(self):
        self.keep_video.configure(state=tk.NORMAL)
        self.download_button.configure(state=tk.NORMAL)

    # </editor-fold>
