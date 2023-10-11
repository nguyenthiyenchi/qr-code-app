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

# function to save qr code with name qr_code.img
def save_qr_code():
    if hasattr(generate_qr_code, 'img'):
        img_byte_array = BytesIO()
        generate_qr_code.img.save(img_byte_array, format = 'PNG')
        with open('qr_code.png', 'wb') as f:
            f.write(img_byte_array.getvalue())

def main():
    window = tk.Tk()
    window.title("QR Code Generator")
    window.geometry("400x450")

    # top panel contains an input bar
    top_panel = tk.Frame(window)
    top_panel.pack(fill = tk.BOTH, expand = True)

    label = tk.Label(top_panel, text = "Enter a link ...")
    label.pack(pady = 10)

    entry = tk.Entry(top_panel)
    entry.pack(pady = 10)

    generate_button = tk.Button(top_panel, text = "Generate QR Code", command = generate_qr_code)
    generate_button.pack(pady = 10)

if __name__ == "__main__":
    main()
