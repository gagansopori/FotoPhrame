''' 
This is digital photo-frame that uses a facial recognition algorithm to manipulate your photos to fit
the display you're portraying them on.
@author: Gagan Sopori
TODO:
 - Add logic to read screen res & make frames in accordance with it
 - Resize photos to the screen in use & save them as a copy somewhere
 - Dynamically Create Text size according to screen res
 - Do Some Face Detection based cropping & Text Adjustment
'''

from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import urllib.request, json
import requests
import random
import os


class PhotoFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # create the frame
        self.frame = Frame(self, bg='black')
        self.frame.pack(side='top', anchor='n', fill='both', expand=YES)  #fill = x,y | expand = resize

        # Not packing the label in the constructor
        self.photoLabel = Label(self.frame, bg='black')

    # This method will retrieve the photos from the directory &
    # prepare to send them to the registered display.
    # @param directory_address
    def process_photos(photoCanvas, directory_address):

        valid_filenames = []

        # Validating .png format for subject photos.
        for file in os.listdir(directory_address):
            if file.endswith(".png"):
                flag = photoCanvas.prepare_photo(directory_address + file)
                if (flag == True):
                    valid_filenames.append(file)
            elif file.endswith(".jpg" or ".jpeg" or ".JPEG" or ".JPG"):
                img = Image.open(directory_address + file)
                image_name = file.split(".")
                new_imagename = image_name[0] + ".png"
                img.save(directory_address + new_imagename)
                img.close()
                flag = photoCanvas.prepare_photo(directory_address + file)
                if (flag == True):
                    valid_filenames.append(file)
            else:
                print("Not sure what to do with this file: %s" % (file))

        # Prepare photos to be displayed.
        photoCanvas.display_photos(directory_address, valid_filenames)

    # This method applies ML based algorithms to photo editing techniques -
    # cropping and/or resizing the photos & tailor them acoording to the display.
    def prepare_photo(photoCanvas, file_addr):

        img = Image.open(file_addr)
        width, height = img.size
        if (width == height):
            flag = True
        elif (width != height):
            # Face Recognition based cropping goes here - Rev. 2 feature
            print(
                "2. %s is not yet ready for this display & we are working on fixing that in the next update." % (file))
            flag = False

        return True

    def display_photos(photoCanvas, directory_addr, valid_filenames):

        file_addr = random.choice(valid_filenames)
        file_name = directory_addr + file_addr

        # This will have whatever name is decided - location/Date/Name etc.
        media_text = file_addr.split('.')
        # print("File Name : %s" %(file_addr))
        img_obj = (photoCanvas.create_label(file_name, media_text[0]))

        photoCanvas.photo = ImageTk.PhotoImage(img_obj)
        photoCanvas.photoLabel.config(image=photoCanvas.photo)
        photoCanvas.photoLabel.image = photoCanvas.photo
        photoCanvas.photoLabel.pack(side=TOP, anchor=NE, fill=BOTH, expand=YES)

        # Recursive call
        photoCanvas.photoLabel.after(10000, photoCanvas.display_photos, directory_addr, valid_filenames)

    def create_label(photoCanvas, file_address, media_name):

        img = Image.open(file_address).convert('RGBA')
        img_w, img_h = img.size

        # Init Font
        font_size = int(img_h / 8)
        photoCanvas.fnt = ImageFont.truetype('D:/zz2/Oswald.ttf', font_size)  # TODO: Not hardcode directory here

        txt = Image.new('RGBA', img.size, (0, 0, 0, 80))  # the last 4 are (Red, Green, Blue, Transparency)
        drwng_kntxt = ImageDraw.Draw(txt)

        # Text-wrapping logic
        text_w, text_h = drwng_kntxt.textsize(media_name.upper(), font=photoCanvas.fnt)
        vertical_padding = int(text_h / 10)
        # print(text_w)
        # print(text_h)

        # Draw Text over the image
        drwng_kntxt.text(((img_w - text_w) / 2, (img_h - text_h - vertical_padding)),
                         media_name.upper(), font=photoCanvas.fnt, fill=(255, 255, 255, 255), padx=5)

        final_media = Image.alpha_composite(img, txt)
        # final_media.save("D:/zz3/written.png")
        img.close()

        return final_media

# def get_exif(photoCanvas, file_addr):

# 	img = Image.open(file_addr)
# 	img.verify()
# 	exif_data = img._getexif()


if __name__ == '__main__':
    root = Tk()
    root.title('FotoPhrame')
    FotoObject = PhotoFrame(root)
    FotoObject.process_photos("D:/zz3/")

    FotoObject.config(bg='black')
    FotoObject.pack(side=TOP, fill=BOTH, expand=YES)

    root.mainloop()
