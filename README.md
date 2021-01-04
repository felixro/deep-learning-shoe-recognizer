# Deep Learning Shoe Recognizer
Python app that utilizes a trained AI model in order to categorize shoe brands. 

## Introduction
As part of my own learning about artificial intelligence, deep learning and neural network, I created this simply Python UI (using tkinter) app to make use of an already trained model to recognize shoe brands.
The actual trained model was built by following the book [Deep Learning for Coders with fastai & PyTorch!](https://course.fast.ai/).

## Requirements
- Python 3+
- Python modules:
  - tkinter
  - https://github.com/fastai/fastai

## Usage
You can simply start the app by running
```
python shoe-recognizer.py
```
which will open a window looking similar to the following:

<img src="/images/examples/example_ui.png" width="400">

Go ahead and guess yourself: at this moment, the only types of shoes the AI recognizes are *Jimmy Choo*, *Allbirds* and *Manolo Blahnik*. Once you have made your guess, press the *AI Prediction* button to see what the AI predicted as well as the actual answer. Click on "Next Image" to try another shoe:

<img src="/images/examples/example_ui_predicted.png" width="400">
