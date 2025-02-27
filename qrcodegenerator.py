import qrcode
import image
import time

qr = qrcode.QRCode(
    version = 15, #version of qr code (the higher the number, the bigger the code image)
    box_size = 10, #size of the box encapsulating the qrcode
    border = 5 #white part of the image -- border in all 4 sides
)

data = input("Input text or links: ")

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img_name = input("Input the filename of the qrcode: ")
img.save(img_name + ".png")

print("Your QRCode is ready! It is saved in the same folder this program is saved!")
time.sleep(15)