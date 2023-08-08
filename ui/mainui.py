import customtkinter as ctk

from ui.NavBar import NavBar


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


if __name__ == "__main__":
    app = App()
    app.mainloop()
