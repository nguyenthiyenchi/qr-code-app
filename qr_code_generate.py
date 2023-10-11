import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from io import BytesIO

# function to generate QR codes 
def generate_qr_code():
    text = entry.get()  # retrieve and the text entered by the user in a variable

    qr = qrcode.QRCode(
        version = 1,
        error_connection = qrcode.constants.ERROR_CORRECT_L,    # 'qrcode.constants.ERROR_CORRECT_L' 
                                                                # indicates that the error correction level 
                                                                # is set to "L," which is the lowest error correction level
        box_size = 10, 
        border = 4
    )

    qr.add_data(text)
    qr.make(fit = True)

    # set color and size (width, height) for qr code image
    img = qr.make_image(fill_color = "", back_color = "")
    img = img.resize((200, 200), Image.ANTIALIAS)

    photo = ImageTk.PhotoImage(img)
    qr_code_label.config(image = photo)
    qr_code_label.image = photo

    generate_qr_code.img = img  # store image

def save_qr_code():

def main():
    window = tk.Tk()

if __name__ == "__main__":
    main()
