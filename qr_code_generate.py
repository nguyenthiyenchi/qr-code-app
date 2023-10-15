import tkinter as tk
from tkinter import font, filedialog
import tkinter.font as font
import qrcode
from PIL import Image, ImageTk
from io import BytesIO

# 💻 WINDOW 💻
# function to change size
def change_window_size(width, height):
    window.geometry(f"{width}x{height}")
# function to set window in center of screen
def center_window(window):   
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("360x200")
window.configure(bg='#330044')
window.resizable(False, False)

# some designs
familyFont = font.Font(family='Consolas')
bgColor = '#330044'


# 🗻 TOP PANEL 🗻
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
entry = tk.Entry(top_panel, textvariable=entry_text, borderwidth=5, relief="flat", width=40, fg="#8a51ab")
entry.insert(0, "Enter a link")
entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", restore_placeholder)
entry.pack(pady=(10, 20))

# function to generate QR codes 
def generate_qr_code():
    text = entry.get()  # retrieve and the text entered by the user in a variable
    
    change_window_size(360, 450)
    center_window(window)

    # bottom panel contains QR Code
    bottom_panel = tk.Frame(window, bg=bgColor, width=360, height=240)
    bottom_panel.pack(fill=tk.BOTH, expand=True)
    bottom_panel.place(x=0, y=165, relwidth=1, relheight=1)
    
    qr_code_label = tk.Label(bottom_panel, bg=bgColor)
    qr_code_label.pack(pady=10)

    # button to download the QR code image
    download_btn = tk.Button(bottom_panel, text="Download QR Code", command=save_qr_code, fg="#d4c0f1", bg="#260033", activebackground="#d4c0f1", borderwidth=5, relief="flat")
    download_btn.pack(pady=10)

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
    
# generate-btn
generate_btn = tk.Button(top_panel, text="Generate QR Code", command=generate_qr_code, bg='#9665dd', fg=bgColor, borderwidth=5, relief="flat", activebackground=bgColor)
generate_btn.pack(pady=(10, 0))

# 🌪 BOTTOM PANEL 🌪
# function to save qr code with name qr_code.img
def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        # Check if the generate_qr_code function has generated an image
        if hasattr(generate_qr_code, 'img'):
            img_byte_array = BytesIO()
            generate_qr_code.img.save(img_byte_array, format='PNG')
            with open(file_path, 'wb') as f:
                f.write(img_byte_array.getvalue())
            print(f"Image saved to {file_path}")
        else:
            print("No image to save. Generate a QR code first.")

        download_successfully()

success_panel = None

# function to notify download successfully
def download_successfully():
    global success_panel
    success_panel = tk.Frame(window, bg=bgColor, width=360, height=240)
    success_panel.pack(fill=tk.BOTH, expand=True)
    success_panel.place(x=0, y=175, relwidth=1, relheight=1)

    notification_label = tk.Label(success_panel, text="Your QR Code has been downloaded successfully. 🎉🎉", width=20, height=5, fg="#d4c0f1", bg="#260033", font=(familyFont, 16), wraplength=200)
    notification_label.pack(padx=20, pady=20)
    
    close_success = tk.Button(success_panel, text="Return to QR Code", command=close_success_panel, fg="#d4c0f1", bg="#260033", activebackground="#d4c0f1", borderwidth=5, relief="flat")
    close_success.pack(pady=10)

def close_success_panel():
    global success_panel
    success_panel.place_forget()

center_window(window)

# start the app
window.mainloop()
