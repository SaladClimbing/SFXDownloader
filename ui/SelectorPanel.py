import customtkinter as ctk


class SelectorPanel(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(self, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']
