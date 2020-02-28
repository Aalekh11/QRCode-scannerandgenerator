import qrcode

img=qrcode.make('www.google.com')

print(type(img))

img.save('qr.png')
