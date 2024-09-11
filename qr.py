import qrcode

data = "https://super-duper-rotary-phone-r4g5qrjqr4r53xqqv-8501.app.github.dev/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")
img.show()
