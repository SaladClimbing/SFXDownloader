import customtkinter as ctk

from ui.DownloadInfo import DownloadInfo
from ui.NavBar import NavBar
from ui.SelectorPanel import SelectorPanel


# --------------------- Window ---------------------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()  # Initialize the window

        # Dimensions
        self.WIDTH = 800
        self.HEIGHT = 600

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Disable the toolbar and change to green theme
        self.overrideredirect(True)
        ctk.set_default_color_theme("green")

        # Sections setup
        self.navbar_height = self.HEIGHT / 20
        self.navbar = NavBar(root=self, width=self.WIDTH, height=self.navbar_height, fg_color="#1f1b1b",
                             border_width=2)
        self.navbar.pack(side=ctk.TOP)

        self.selector_panel = SelectorPanel(root=self, width=self.WIDTH / 2, height=self.HEIGHT - self.navbar_height,
                                            fg_color="#242424")
        self.selector_panel.pack(side=ctk.LEFT)

        self.DownloadInfo = DownloadInfo(root=self, width=200, height=200)
        self.DownloadInfo.pack(side=ctk.RIGHT)


if __name__ == "__main__":
    app = App()
    app.mainloop()
