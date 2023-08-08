import customtkinter as ctk


# --------------------- NavBar ---------------------
class NavBar(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']

        self.title = ctk.CTkLabel(self, text="SFXDownloader", font=('Helvetica', 18, 'bold'),
                                  height=self.HEIGHT, width=self.WIDTH - 2 * self.HEIGHT, anchor="w", padx=10)
        self.title.pack(side=ctk.LEFT)
        self.pack_buttons()
        self.bind("<Map>", self.frame_mapped)

    def pack_buttons(self):
        self.quit_button = ctk.CTkButton(self, text=" × ", font=('Helvetica', 18, 'bold'), command=self.root.quit,
                                         fg_color="#1f1b1b", hover_color="darkred", height=self.HEIGHT,
                                         width=self.HEIGHT) \
            .pack(side=ctk.RIGHT)  # Yes the width is supposed to be height
        self.min_button = ctk.CTkButton(self, text=" 🗕 ", font=('Helvetica', 18, 'bold'),
                                        command=self.minimize,
                                        fg_color="#1f1b1b", hover_color="darkred", height=self.HEIGHT,
                                        width=self.HEIGHT) \
            .pack(side=ctk.RIGHT)

    # https://stackoverflow.com/questions/29186327/tclerror-cant-iconify-override-redirect-flag-is-set
    def frame_mapped(self, e):
        self.root.update_idletasks()
        self.root.overrideredirect(True)
        self.root.state('normal')

    def minimize(self):
        self.root.update_idletasks()
        self.root.overrideredirect(False)
        # root.state('withdrawn')
        self.root.state('iconic')
