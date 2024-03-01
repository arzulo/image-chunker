import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import shutil
import time


# PARAMETERS 
# ---------------------------------------------------
# Images will be split into max CHUNK_SIZE x CHUNK_SIZE 
CHUNK_SIZE = 2048


# DO NOT CHANGE BELOW THIS LINE
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------

# Sub function to help with the file selection
def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        return file_path
    else:
        print("No file selected.")
        return None

# Sub function to do the actual file splitting
def split_image(image_path, chunk_size):
    image = Image.open(image_path)
    width, height = image.size
    chunks = []
    # Current implementation will make ALL chunks have the defined size. 
    # So even if the final chunk doesn't fill out the remaining portion of the image, 
    # it will still be the defined chunk size with transparency leftover
    for y in range(0, height, chunk_size):
        for x in range(0, width, chunk_size):
            box = (x, y, x + chunk_size, y + chunk_size)
            chunk = image.crop(box)
            chunks.append(chunk)
    return chunks

# Sub function to aid in deleting existing folders
def try_to_rmtree(can_still_retry, path_to_delete):
    if can_still_retry:
        try:
            if os.path.isdir(path_to_delete):
                shutil.rmtree(path_to_delete)
        except:
            try_to_rmtree(can_still_retry -1, path_to_delete)

def main():

    # Figure out file and path names
    image_path = select_image()
    image_dir_path = os.path.dirname(image_path)
    base_name = os.path.basename(image_path).split('.')
    base_image_name = base_name[0]
    image_ext = base_name[1]
    chunks_folder = f"{base_image_name}_chunks";
    chunks_path = f"{image_dir_path}/{chunks_folder}"

    # Check if the dir exists, if so delete it
    if os.path.isdir(chunks_path):
        try:
            # Sometimes there are weird race conditions with deleting it... just try multiple times till it works with a sleep time
            try_to_rmtree(10, chunks_path)
            os.rmdir(chunks_path)
            # Give some time to remove, jank but oh well.
            time.sleep(1)
        except OSError as e:
            print(f"Error removing directory - {e.filename} - {e.strerror}")
    
    # Make it 
    os.mkdir(chunks_path)

    if image_path:
        chunks = split_image(image_path, CHUNK_SIZE)

        for i, chunk in enumerate(chunks):
            chunk.save(f"{chunks_path}/chunk_{i}.{image_ext}")
        
        print("Image successfully split into chunks.")
        os.startfile(chunks_path)


if __name__ == "__main__":
    main()
