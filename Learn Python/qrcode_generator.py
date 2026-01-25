import qrcode

def generate_qr_code(text, filename):
    try:
        # Add .png if user doesn't write extension
        if not filename.endswith(".png"):
            filename = filename + ".png"

        # Generate QR Code
        image_qrcode = qrcode.make(text)
        image_qrcode.save(filename)

        print("✅ QR Code generated successfully!")
        print("📁 File saved as:", filename)

    except Exception as e:
        print("❌ Error:", e)


# ---- User Input ----
text = input("Enter the text to convert into QR code: ")

if text.strip() == "":
    print("❌ Text cannot be empty!")
else:
    filename = input("Enter the file name to save the QR code: ")
    generate_qr_code(text, filename)
