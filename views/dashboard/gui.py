from pathlib import Path
from tkinter import Frame, Canvas, PhotoImage, Entry, Button
import tkinter as tk
import pytesseract
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
IMAGES_PATH = ASSETS_PATH / Path("./pic")
IMAGES_LIST = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png"]


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_pic(path: str) -> Path:
    return IMAGES_PATH / Path(path)

def dashboard():
    Dashboard()


class Dashboard(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.CURRENT_IMAGE = 0
        self.image = []
        
        for i in range(len(IMAGES_LIST)):
            self.image.append(ImageTk.PhotoImage(Image.open(relative_to_pic(IMAGES_LIST[self.CURRENT_IMAGE + i]))))

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

        # Handling ROI =======
        self.canvas.bind("<ButtonPress-1>", self.start_selecting)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selecting)

        self.ocr_output = None
        self.rectangles = []
        self.selection_rectangle = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        # ====================

        self.canvas.place(x=0, y=0)

        self.entry_bg_1 = self.canvas.create_image(300, 210, image=self.image[self.CURRENT_IMAGE])
        entry_1 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_1.place(x=607.0, y=30.0 + 2, width=120.0, height=0)

        self.canvas.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(667.0, 70.0, image=self.canvas.entry_image_2)
        entry_2 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_2.place(x=607.0, y=30.0 + 2, width=120.0, height=0)

        self.canvas.create_text(
            608.0,
            45.0,
            anchor="nw",
            text="Recognized Digit",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.ocr_output_entry = self.canvas.create_text(
            666.0,
            63.0,
            anchor="n",
            text=self.ocr_output,
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_btn_press,
            relief="flat",
        )
        button_1.place(x=594.0, y=125.0, width=144.0, height=36.0)

        self.canvas.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(683.0, 298.0, image=self.canvas.image_image_1)

    def handle_btn_press(self):
        self.CURRENT_IMAGE = (self.CURRENT_IMAGE + 1) % len(IMAGES_LIST)
        self.canvas.itemconfig(self.entry_bg_1, image=self.image[self.CURRENT_IMAGE])
        for rect in self.rectangles:
            self.canvas.delete(rect)
        self.ocr_output = ""
        self.canvas.itemconfig(self.ocr_output_entry, text=self.ocr_output)

    def start_selecting(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.selection_rectangle = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")
        self.rectangles.append(self.selection_rectangle)
        self.ocr_output = ""
        self.canvas.itemconfig(self.ocr_output_entry, text=self.ocr_output)

    def update_selection(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.canvas.coords(self.selection_rectangle, self.start_x, self.start_y, self.end_x, self.end_y)

    def end_selecting(self, event):
        if self.start_x is not None and self.start_y is not None and self.end_x is not None and self.end_y is not None:
            x1 = min(self.start_x - 15, self.end_x - 10)
            y1 = min(self.start_y - 15, self.end_y - 10)
            x2 = max(self.start_x - 15, self.end_x - 10)
            y2 = max(self.start_y - 15, self.end_y - 10)
            roi_image = ImageTk.getimage(self.image[self.CURRENT_IMAGE]).crop((x1, y1, x2, y2))
            
            self.ocr_output = pytesseract.image_to_string(roi_image, config="--psm 10 outputbase digits")[:-1]

            self.canvas.itemconfig(self.ocr_output_entry, text=self.ocr_output)