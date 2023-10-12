import tkinter as tk
from tkinter import font
import tkinter.font as font
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


window = tk.Tk()
window.title("QR Code Generator")
window.geometry("360x450")
window.configure(bg='#330044')
window.resizable(False, False)

# some designs
familyFont = font.Font(family='Consolas')
bgColor = '#330044'

# top panel contains an input bar
top_panel = tk.Frame(window, bg=bgColor)
top_panel.pack(fill=tk.BOTH, expand=True)

# define a custom font with a specific font size for label
font_label = font.Font(family=familyFont, size=16)
label = tk.Label(top_panel, text="QR CODE GENERATOR", fg='#9665dd', bg=bgColor, font=font_label)
label.pack(pady=(20, 10))

# the Entry content
entry_text = tk.StringVar()

# function to clear the placeholder and set the text color
def clear_placeholder(event):
    if entry_text.get() == "Enter a link":
        entry_text.set("")
        entry.config(fg="#4b0082")

# function to restore the placeholder if the Entry is empty
def restore_placeholder(event):
    if not entry_text.get():
        entry_text.set("Enter a link")
        entry.config(fg="#4b0082")

# input
entry = tk.Entry(top_panel, textvariable=entry_text, width=40, fg="#8a51ab")
entry.insert(0, "Enter a link")
entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", restore_placeholder)
entry.pack(pady=(10, 20))

# generate-btn
generate_btn = tk.Button(top_panel, text="Generate QR Code", command=generate_qr_code, bg='#9665dd', fg=bgColor, borderwidth=0, relief="flat", activebackground='#9665dd')
generate_btn.pack(pady=10)

# bottom panel contains QR Code
bottom_panel = tk.Frame(window, bg=bgColor)
bottom_panel.pack(fill=tk.BOTH, expand=True)

qr_code_label = tk.Label(bottom_panel, bg=bgColor)
qr_code_label.pack(pady=10)

# button to download the QR code image
download_btn = tk.Button(bottom_panel, text="Download QR Code", command=save_qr_code, fg="#d4c0f1", bg="#260033", borderwidth=0, relief="flat")
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
