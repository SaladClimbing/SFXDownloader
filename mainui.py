import customtkinter as ctk


# --------------------- Window ---------------------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.WIDTH = 800
        self.HEIGHT = 600

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.overrideredirect(True)
        ctk.set_default_color_theme("green")

        self.navbar = NavBar(root=self, width=self.WIDTH, height=self.HEIGHT / 10, fg_color="#1f1b1b")  # #242424
        self.navbar.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
        self.navbar.columnconfigure(0, weight=1)


# --------------------- NavBar ---------------------
class NavBar(ctk.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.root = root

        self.title = ctk.CTkLabel(self.root, text="SFXDownloader", font=('Helvetica', 18, 'bold'),
                                  height=self.root.HEIGHT / 10, width=600,
                                  bg_color="#1f1b1b")
        self.title.grid(row=0, column=0, padx=0, sticky=ctk.W + ctk.E)

        self.button = ctk.CTkButton(self.root, text="X", font=('Helvetica', 18, 'bold'), command=self.root.quit,
                                    fg_color="#1f1b1b", hover_color="darkred", height=self.root.HEIGHT / 10,
                                    width=self.root.HEIGHT / 10)
        self.button.grid(row=0, column=1, padx=0, sticky=ctk.W)


if __name__ == "__main__":
    app = App()
    app.mainloop()
