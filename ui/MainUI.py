import customtkinter as ctk

from ui.NavBar import NavBar
from ui.SelectorPanel import SelectorPanel


# --------------------- Window ---------------------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.WIDTH = 800
        self.HEIGHT = 600

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.overrideredirect(True)
        ctk.set_default_color_theme("green")

        self.navbar = NavBar(root=self, width=self.WIDTH, height=self.HEIGHT / 20, fg_color="#1f1b1b",
                             border_width=2)
        self.navbar.pack(side=ctk.TOP)

        self.selector_panel = SelectorPanel(root=self, width=self.WIDTH / 2, height=self.HEIGHT - self.HEIGHT / 20)
        self.selector_panel.pack(side=ctk.LEFT)


if __name__ == "__main__":
    app = App()
    app.mainloop()
