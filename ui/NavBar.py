import customtkinter as ctk


# --------------------- NavBar ---------------------
class NavBar(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.HEIGHT = kwargs['height']
        self.WIDTH = kwargs['width']

        self.pack_title()
        self.pack_buttons()
        self.bind("<Map>", self.frame_mapped)

    def pack_title(self):
        self.title = ctk.CTkLabel(self, text="SFXDownloader", font=('Helvetica', 18, 'bold'),
                                  height=self.HEIGHT, width=self.WIDTH - 2 * self.HEIGHT, anchor="w", padx=10)
        self.title.pack(side=ctk.LEFT)

        self.title.bind("<ButtonPress-1>", self.start_move)
        self.title.bind("<ButtonRelease-1>", self.stop_move)
        self.title.bind("<B1-Motion>", self.do_move)

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

    # Both frame_mapped and minimize were found here:
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

    # Moveable window found here:
    # https://stackoverflow.com/questions/4055267/tkinter-mouse-drag-a-window-without-borders-eg-overridedirect1
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
