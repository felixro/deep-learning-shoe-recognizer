#!/usr/bin/env python

import os

from fastai.vision.all import *
from tkinter import *
from PIL import ImageTk, Image

shoe_brands = {
    'allbirds': 'ALLBIRDS',
    'jimmychoo': 'JIMMY CHOO',
    'manolo_blahnik': 'MANOLO BLAHNIK'
}

def determine_valid_brand(filename):
    """Attemps to determine the brand name based on the provided filename.

    Args:
      filename: the filename to determine the shoe brand of based on its name.

    Returns:
      The brand name.
    """
    for brand_file_name, brand_name in shoe_brands.items():
        if os.path.basename(filename).startswith(brand_file_name):
            return brand_name
    return 'UNKNOWN BRAND'

def next_image(prediction_msg, actual_msg):
    """Helper method to update the UI so that the next image can be shown.

    Args:
      prediction_msg: the UI widget containing the prediction message of the current image.
      actual_msg: the UI widget containing the actual/valid show brand of the current image.
    """
    prediction_msg.destroy()
    actual_msg.destroy()
    blocking_var.set(1)

def predict_image(image, canvas):
    """Predicts the brand of the provided image and shows the prediction on the provided canvas.

    Args:
      image: the image to predict the brand for.
      canvas: the canvas used to show the prediction in text form
    """
    (brand, _, _) = learner.predict(image)
    sanitized_brand = brand.upper().replace("_", " ")
    actual_brand = determine_valid_brand(image)

    bg_color = 'lightgreen' if sanitized_brand == actual_brand else 'red'
    prediction_msg = Message(canvas, text = 'AI prediction:\t <{}>'.format(sanitized_brand))
    prediction_msg.config(bg = bg_color, width = 400, font = ('times', 20, 'italic'))
    canvas.create_window(50, 420, anchor=NW, window=prediction_msg)

    actual_msg = Message(canvas, text = 'Actual:\t\t <{}>'.format(actual_brand))
    actual_msg.config(width = 400, font = ('times', 20, 'italic'))
    canvas.create_window(50, 460, anchor=NW, window=actual_msg)

    next_button = Button(canvas, text = "Next Image", fg="red", command = lambda:next_image(prediction_msg, actual_msg))
    next_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    canvas.create_window(220, 20, anchor=NW, window=next_button)

learner = load_learner('export.pkl')

root = Tk()
blocking_var = IntVar()

canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
directory = 'images/shoes'

for filename in os.listdir(directory):
    filepath = '{}/{}'.format(directory, filename)

    predict_button = Button(canvas, text = "AI Prediction", fg="red", command = lambda f=filepath:predict_image(f, canvas))
    predict_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    canvas.create_window(100, 20, anchor=NW, window=predict_button)

    img = ImageTk.PhotoImage(Image.open(filepath))  
    canvas.create_image(20, 80, anchor=NW, image=img)

    predict_button.wait_variable(blocking_var)
    blocking_var.set(0)
