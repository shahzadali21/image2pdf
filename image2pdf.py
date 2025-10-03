import os
from PIL import Image
import matplotlib.pyplot as plt

# Change this to your image folder path
FOLDER_IMG = r"/Users/.../Desktop/images"

def main():
    # Supported image extensions
    valid_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tif', '.tiff', '.webp'}

    # Loop through files in folder
    for file in os.listdir(FOLDER_IMG):
        name, ext = os.path.splitext(file)
        if ext.lower() in valid_exts:
            img_path = os.path.join(FOLDER_IMG, file)

            # Open image
            img = Image.open(img_path)

            # Export directly to PDF with 1200 DPI
            imname = os.path.join(FOLDER_IMG, f"{name}.pdf")
            plt.imshow(img)
            plt.axis('off')
            plt.savefig(imname, dpi=1200, bbox_inches='tight', pad_inches=0)
            plt.close()

            print(f"Converted: {file} → {name}.pdf")

if __name__ == "__main__":
    main()
