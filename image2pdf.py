import os
from tkinter import Tk, filedialog
from PIL import Image
import matplotlib.pyplot as plt

# Hide root tkinter window
Tk().withdraw()

# Ask user to select a folder
print("Select the input image folder:")
folder_img = filedialog.askdirectory()

# Define allowed image extensions
valid_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tif', '.tiff', '.webp'}

# Loop through files in folder
for file in os.listdir(folder_img):
    name, ext = os.path.splitext(file)
    if ext.lower() in valid_exts:
        img_path = os.path.join(folder_img, file)

        # Read image
        img = Image.open(img_path)

        # Show image (like MATLAB imshow)
        plt.imshow(img)
        plt.axis('off')
        plt.show(block=False)
        plt.pause(1)  # show for 1 second

        # Export to PDF with 1200 DPI
        imname = os.path.join(folder_img, f"{name}.pdf")
        plt.savefig(imname, dpi=1200, bbox_inches='tight', pad_inches=0)
        plt.close()
