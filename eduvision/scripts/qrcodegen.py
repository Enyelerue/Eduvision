import qrcode

# Data to encode
data = "d"

# Create QR code
qr = qrcode.QRCode(
    version=5,  # Controls size (1 = 21x21, up to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box in pixels
    border=4,     # Border in boxes
)
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcodes/d.png")
print("QR code saved as qrcode.png")
