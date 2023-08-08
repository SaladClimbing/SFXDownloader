import customtkinter as ctk

from downloader import download


# --------------------- Selector Panel ---------------------
class SelectorPanel(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']

        self.pack_search()

    def pack_search(self):
        self.search_box = ctk.CTkEntry(self, height=25, width=200, font=('Helvetica', 18, 'bold'),
                                       placeholder_text="Insert Link Here")
        self.search_box.pack(padx=100, pady=5)

        self.search_button = ctk.CTkButton(self, height=25, width=200, text="Search", font=('Helvetica', 18, 'bold'),
                                           command=self.download) \
            .pack(padx=100, pady=5)

    def download(self):
        download(self.search_box.get(), False)