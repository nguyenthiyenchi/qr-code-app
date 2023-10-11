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