import tkinter as tk
from tkinter import simpledialog, ttk
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle, Ellipse, Rectangle
from textblob import TextBlob
import spacy
import numpy as np

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# List of predefined background colors
background_colors = ['#F0E68C', '#FFD700', '#FF6347', '#4682B4', '#5F9EA0', '#DDA0DD', '#F08080', '#B0C4DE']

def analyze_text_and_generate_shape(text):
    # Analyze sentiment using TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Use spaCy for additional text processing (e.g., part-of-speech tagging)
    doc = nlp(text)

    # Determine color based on sentiment polarity
    if sentiment > 0.75:
        color = '#FFFF00'  # yellow
    elif sentiment > 0.5:
        color = '#FFA500'  # orange
    elif sentiment > 0.25:
        color = '#90EE90'  # light green
    elif sentiment > 0:
        color = '#008000'  # green
    elif sentiment > -0.25:
        color = '#ADD8E6'  # light blue
    elif sentiment > -0.5:
        color = '#0000FF'  # blue
    elif sentiment > -0.75:
        color = '#800080'  # purple
    else:
        color = '#00008B'  # dark blue

    # Determine shape based on sentiment score
    if sentiment > 0.75:
        shape = 'star'
    elif sentiment > 0.5:
        shape = 'hexagon'
    elif sentiment > 0.25:
        shape = 'pentagon'
    elif sentiment > 0:
        shape = 'triangle'
    elif sentiment > -0.25:
        shape = 'square'
    elif sentiment > -0.5:
        shape = 'diamond'
    elif sentiment > -0.75:
        shape = 'ellipse'
    else:
        shape = 'circle'

    # Determine size based on the absolute value of sentiment polarity
    if abs(sentiment) > 0.75:
        size = 3
    elif abs(sentiment) > 0.5:
        size = 2
    else:
        size = 1

    # Select a background color different from the shape's color
    background_color = np.random.choice([bg for bg in background_colors if bg != color])

    return color, shape, size, background_color

def draw_shape(color, shape, size, background_color):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(background_color)
    ax.set_aspect('equal')
    ax.axis('off')

    if shape == 'triangle':
        polygon = RegularPolygon((0.5, 0.5), numVertices=3, radius=size*0.1, color=color)
    elif shape == 'star':
        polygon = RegularPolygon((0.5, 0.5), numVertices=5, radius=size*0.1, color=color, orientation=np.pi/10)
    elif shape == 'square':
        polygon = RegularPolygon((0.5, 0.5), numVertices=4, radius=size*0.1, color=color)
    elif shape == 'circle':
        polygon = Circle((0.5, 0.5), radius=size*0.1, color=color)
    elif shape == 'ellipse':
        polygon = Ellipse((0.5, 0.5), width=size*0.2, height=size*0.1, color=color)
    elif shape == 'pentagon':
        polygon = RegularPolygon((0.5, 0.5), numVertices=5, radius=size*0.1, color=color)
    elif shape == 'diamond':
        polygon = RegularPolygon((0.5, 0.5), numVertices=4, radius=size*0.1, color=color, orientation=np.pi/4)
    elif shape == 'hexagon':
        polygon = RegularPolygon((0.5, 0.5), numVertices=6, radius=size*0.1, color=color)
    elif shape == 'rectangle':
        polygon = Rectangle((0.4, 0.4), width=size*0.2, height=size*0.1, color=color)

    ax.add_patch(polygon)
    plt.show()

def on_generate_button_click():
    text = simpledialog.askstring("Input", "Describe your mood and characteristics:", parent=root)
    if text:
        color, shape, size, background_color = analyze_text_and_generate_shape(text)
        draw_shape(color, shape, size, background_color)
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Mood Shape Generator")

# Set the main window size and center it
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Create a frame for the content
frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# Add a title label
title_label = ttk.Label(frame, text="Mood Shape Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(0, 10))

# Add a description label
description_label = ttk.Label(frame, text="Enter your mood and characteristics to generate a unique shape.")
description_label.pack(pady=(0, 20))

# Create a button to generate shape
generate_button = ttk.Button(frame, text="Generate Shape", command=on_generate_button_click)
generate_button.pack()

# Apply some styling to the ttk widgets
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.configure("TFrame", background="#eee")
style.configure("TLabel", background="#eee")

# Start the GUI event loop
root.mainloop()
