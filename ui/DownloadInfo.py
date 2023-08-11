import customtkinter as ctk

from ui.ImageManipulation import get_resized_thumbnail


class DownloadInfo(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']

        self.pack_thumbnail(
            "")
        self.pack_details()

    def pack_thumbnail(self, url):
        img = get_resized_thumbnail(url, self.WIDTH)
        self.thumbnail = ctk.CTkLabel(self, image=img, width=self.WIDTH - 25, height=(self.WIDTH - 25) * 9 / 16,
                                      text="")
        self.thumbnail.pack(padx=25, pady=10)

    def pack_details(self):
        self.line_frame = ctk.CTkFrame(self, width=2, height=100, bg_color="white")
        self.line_frame.pack(padx=(25, 5), side=ctk.LEFT)

        self.title_label = ctk.CTkLabel(self, width=self.WIDTH - 25, font=('Helvetica', 18, 'bold'), justify="left",
                                        anchor="w", text="Title: ")
        self.title_label.pack()
        self.author_label = ctk.CTkLabel(self, width=self.WIDTH - 25, font=('Helvetica', 18, 'bold'), justify="left",
                                         anchor="w", text="Author: ")
        self.author_label.pack()
        self.time_label = ctk.CTkLabel(self, width=self.WIDTH - 25, font=('Helvetica', 18, 'bold'), justify="left",
                                       anchor="w", text="Duration: ")
        self.time_label.pack()
