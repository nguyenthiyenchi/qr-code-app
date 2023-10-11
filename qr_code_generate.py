import tkinter as tk
from tkinter import font
import qrcode
from PIL import Image, ImageTk
from io import BytesIO

# function to generate QR codes 
def generate_qr_code():
    text = entry.get()  # retrieve and the text entered by the user in a variable

    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,      # 'qrcode.constants.ERROR_CORRECT_L' 
                                                                # indicates that the error correction level 
                                                                # is set to "L," which is the lowest error correction level
        box_size = 10, 
        border = 4
    )
    qr.add_data(text)
    qr.make(fit = True)

    # set color and size (width, height) for qr code image
    img = qr.make_image(fill_color="#d4c0f1cc", back_color="#260033cc")
    img = img.resize((200, 200), Image.ANTIALIAS)

    photo = ImageTk.PhotoImage(img)
    qr_code_label.config(image = photo)
    qr_code_label.image = photo

    generate_qr_code.img = img  # store image

# function to save qr code with name qr_code.img
def save_qr_code():
    if hasattr(generate_qr_code, 'img'):
        img_byte_array = BytesIO()
        generate_qr_code.img.save(img_byte_array, format='PNG')
        with open('qr_code.png', 'wb') as f:
            f.write(img_byte_array.getvalue())

# def main():
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("400x450")
window.configure(bg='#330044')
window.resizable(False, False)

# window.config(fg="rgb(150, 101, 221)", bg="rgb(51, 0, 68)")

# top panel contains an input bar
top_panel = tk.Frame(window, bg='#330044')
top_panel.pack(fill=tk.BOTH, expand=True)

# Define a custom font with a specific font size
font_label = font.Font(family="Consolas", size=16)
label = tk.Label(top_panel, text="QR CODE GENERATOR", fg='#9665dd', bg='#330044', font=font_label)
label.pack(pady = 20)

entry = tk.Entry(top_panel)
entry.pack(pady = 10)

generate_btn = tk.Button(top_panel, text="Generate QR Code", command=generate_qr_code)
generate_btn.pack(pady = 10)

# bottom panel contains QR Code
bottom_panel = tk.Frame(window, bg='#330044')
bottom_panel.pack(fill=tk.BOTH, expand=True)

qr_code_label = tk.Label(bottom_panel, bg='#330044')
qr_code_label.pack(pady=10)

# button to download the QR code image
download_btn = tk.Button(bottom_panel, text="Download QR Code", command=save_qr_code)
download_btn.pack(pady=10)

# Center the main window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# start the app
window.mainloop()

# if __name__ == "__main__":
#     main()
