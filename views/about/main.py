from pathlib import Path

from tkinter import Frame, Canvas, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about():
    About()


class About(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            36.0,
            43.0,
            anchor="nw",
            text="DigitReco was created by",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(191.0, 26.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(340.0, 205.0, image=self.image_image_2)

        self.canvas.create_text(
            70.0,
            121.0,
            anchor="nw",
            text="Developer",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )

        self.canvas.create_text(
            70.0,
            145.0,
            anchor="nw",
            text="Maryam Saeidmehr",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(570.0, 160.0, image=self.image_image_3)

        self.canvas.create_rectangle(
            70.0, 197.0, 169.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.canvas.create_text(
            197.0,
            352.0,
            anchor="nw",
            text="© 2024-23 Maryam Saeidmehr, All rights reserved",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            246.0,
            372.0,
            anchor="nw",
            text="Open sourced under the MIT license",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            70.0,
            207.0,
            anchor="nw",
            text="A coding-addict, entusiastic developer, and a passionate learner,",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            70.0,
            223.0,
            anchor="nw",
            text="Maryam likes to bring perfection to anything she’s doing. She’s",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            70.0,
            239.0,
            anchor="nw",
            text="also a passionate researcher.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
