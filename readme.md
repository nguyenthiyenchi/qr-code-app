# QR Code Generator

Thanks for visiting [my-QR-Code-Generator](https://github.com/nguyenthiyenchi/some-python-projects/tree/main/qr-code-app)!

An easy-to-use app to help you to generate and save qr code.

## Table of Contents

- [Simple QR Code Generation](#simple-qr-code-generation)
- [QR Code Generator](#qr-code-generator)
- [Installation](#installation)
<!-- - [Demo](#demo) -->
- [Contributing](#contributing)
- [License](#license)


## Simple QR Code Generation

   ```python
   import qrcode

   img = qrcode.make('https://www.google.com/')
   img.save('qr_code.png')
   ```

## QR Code Generator
**1. Run the application:** Double-click the application file or execute the Python script to launch the QR Code Generator. The GUI will appear.

**2. Interface Overview:** The GUI includes the following components:

   - **Input Field**: is where to enter the link or data so as to encode in the QR code.
   - **Generate QR Code Button**: Click this button to generate the QR code.
   - **QR Code Display**: The generated QR code will be displayed in the GUI.
   
**3. Input link:** In the input field, enter the link or data so as to encode in the QR code.

**4. Generate QR Code:** Click the "Generate QR Code" button to create the QR code.

**5. QR Code Display:** The generated QR code will be displayed in the GUI, ready for use.

**6. Save or Share:** Right-click on the QR code image to save it to your device or copy it for sharing.

**7. Notification:** There will appear a message if you download QR Code successfully.

**Here's a screenshot of the QR Code Generator GUI:**


## Installation

1. First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/nguyenthiyenchi/qr-code-app
   ```

2. Second, make sure you have Python and the necessary libraries installed.
   
   The **tkinter** and **io** library are parts of the Python standard library and doesn't need to be installed separately.

   - **tkinter**: tkinter is Python's standard library for creating graphical user interfaces (GUIs). It provides a set of tools and widgets to build windows, dialogs, buttons, and other interactive elements for desktop applications.
   - **io**: The io module in Python provides core tools for working with binary and text I/O (input and output). It allows you to read from and write to various types of streams, such as files, memory buffers, and network connections.

   You can install **qrcode** and **PIL** using pip:
   ```bash
   pip install qrcode[pil]
   ```

   - **qrcode**: The qrcode library enables the generation of QR codes from textual data. It is commonly used to encode information like URLs, contact details, or other data into QR codes for use in various applications.
   - **Pillow (PIL Fork)**: Pillow, a fork of the Python Imaging Library (PIL), is a powerful library for image processing and manipulation. It allows you to open, modify, and save various image file formats, perform operations like resizing, cropping, and filtering, and create visual elements for use in graphical applications.



## Usage

## Demo

## Techniques
