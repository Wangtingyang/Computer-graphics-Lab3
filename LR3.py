from tkinter import *

import cv2
from PIL import ImageTk, Image
import numpy as np


class MainSolution:
    def __init__(self):
        self.image = cv2.imread("chameleon.jpg")
        self.imgray = None
        self.trsh1 = None
        self.trsh2 = None

    def original(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def filter(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        img = np.array(img)
        img = cv2.pyrMeanShiftFiltering(img, sp=15, sr=50)
        img = Image.fromarray(img)
        return ImageTk.PhotoImage(img)

    def local_threshold(self):
        img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (300, 300))
        _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return ImageTk.PhotoImage(Image.fromarray(img))

    def adaptive_threshold(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        threshold_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
        return ImageTk.PhotoImage(Image.fromarray(threshold_img))

    def gaussian_filter(self):
        img = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (300, 300))
        img = cv2.GaussianBlur(img, (5, 5), 0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return ImageTk.PhotoImage(image=Image.fromarray(img))

    def bilateral_filter(self):
        img = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (300, 300))
        img = cv2.bilateralFilter(img, 9, 75, 75)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return ImageTk.PhotoImage(image=Image.fromarray(img))

    def opening(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        kernel = np.ones((5, 5), np.uint8)
        closing = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        img = Image.fromarray(closing)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def closing(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        kernel = np.ones((5, 5), np.uint8)
        closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        img = Image.fromarray(closing)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)


class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing")
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.master.configure(background="white")

        self.solution = MainSolution()

        self.frame = Frame(self.master, bg="white")
        self.frame.pack()

        self.label = Label(self.frame, text="Image Processing", font=("Arial", 20), bg="white")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.button1 = Button(self.frame, text="Original", font=("Arial", 12), bg="white",
                              command=self.original_image)
        self.button1.grid(row=1, column=0, pady=10)

        self.button2 = Button(self.frame, text="Mean shift filter", font=("Arial", 12), bg="white", command=self.filt)
        self.button2.grid(row=1, column=1, pady=10)

        self.button3 = Button(self.frame, text="Local threshold", font=("Arial", 12), bg="white",
                              command=self.local_threshold)
        self.button3.grid(row=2, column=0, pady=10)

        self.button4 = Button(self.frame, text="Adaptive threshold", font=("Arial", 12), bg="white",
                              command=self.adaptive_threshold)
        self.button4.grid(row=2, column=1, pady=10)

        self.button5 = Button(self.frame, text="Gaussian filter", font=("Arial", 12), bg="white",
                              command=self.gaussian_filter)
        self.button5.grid(row=3, column=0, pady=10)

        self.button6 = Button(self.frame, text="Bilateral filter", font=("Arial", 12), bg="white",
                              command=self.bilateral_filter)
        self.button6.grid(row=3, column=1, pady=10)

        self.button11 = Button(self.frame, text="Opening", font=("Arial", 12), bg="white", command=self.opening)
        self.button11.grid(row=6, column=0, pady=10)

        self.button12 = Button(self.frame, text="Closing", font=("Arial", 12), bg="white", command=self.closing)
        self.button12.grid(row=6, column=1, pady=10)

        self.button13 = Button(self.frame, text="Exit", font=("Arial", 12), bg="white", command=self.exit)
        self.button13.grid(row=7, column=0, columnspan=2, pady=10)

        self.label1 = Label(self.frame, text="Original", font=("Arial", 12), bg="white")
        self.label1.grid(row=7, column=0, pady=10)

        self.label2 = Label(self.frame, text="Processed", font=("Arial", 12), bg="white")
        self.label2.grid(row=7, column=1, pady=10)

        self.image1 = self.solution.original()
        self.label3 = Label(self.frame, image=self.image1, bg="white")
        self.label3.grid(row=8, column=0, pady=10)

        self.image2 = self.solution.original()
        self.label4 = Label(self.frame, image=self.image2, bg="white")
        self.label4.grid(row=8, column=1, pady=10)

    def original_image(self):
        self.image1 = self.solution.original()
        self.label3.configure(image=self.image1)
        self.label3.image = self.image1

    def filt(self):
        self.image2 = self.solution.filter()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def local_threshold(self):
        self.image1 = self.solution.local_threshold()
        self.label4.configure(image=self.image1)
        self.label4.image = self.image1

    def adaptive_threshold(self):
        self.image2 = self.solution.adaptive_threshold()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def gaussian_filter(self):
        self.image2 = self.solution.gaussian_filter()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def bilateral_filter(self):
        self.image2 = self.solution.bilateral_filter()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def opening(self):
        self.image2 = self.solution.opening()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def closing(self):
        self.image2 = self.solution.closing()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def exit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("ImageProcessing")
    root.geometry("800x600")
    root.resizable(False, False)
    app = MainApp(root)
    root.mainloop()
