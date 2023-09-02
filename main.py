import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Logic and functions of the app
def open_image():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        image = Image.open(file_path)
        image.show()

def add_watermark():
    if 'image' in globals():
        watermark_text = watermark_entry.get()
        if watermark_text:
            img_with_watermark = image.copy()
            draw = ImageDraw.Draw(img_with_watermark)
            width, height = img_with_watermark.size
            font = ImageFont.truetype("arial.ttf", 20)
            text_width, text_height = draw.textsize(watermark_text, font)
            x = width - text_width - 10
            y = height - text_height - 10
            draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)
            img_with_watermark.show()
        else:
            status_label.config(text="Watermark text is empty.")
    else:
        status_label.config(text="Open an image first.")

# Creates the GUI of the app
root = tk.Tk()
root.title("Image Watermarking App")

# Button that opens images
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Entry for watermark text
watermark_entry = tk.Entry(root, width=30)
watermark_entry.pack()

# Button to add watermark
add_button = tk.Button(root, text="Add Watermark", command=add_watermark)
add_button.pack()

# Label to display status messages
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
