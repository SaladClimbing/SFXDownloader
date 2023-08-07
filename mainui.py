import customtkinter as ctk


# --------------------- Window ---------------------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.WIDTH = 800
        self.HEIGHT = 600

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.overrideredirect(True)

        self.navbar = NavBar(root=self, width=self.WIDTH, height=self.HEIGHT / 10)
        self.navbar.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


# --------------------- NavBar ---------------------
class NavBar(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.button = ctk.CTkButton(self.root, text="Quit", command=self.root.quit)
        self.button.grid(row=0, column=0, padx=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
