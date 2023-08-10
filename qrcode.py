import qrcode

data = 'Don\'t forget to subscribe'

img = qrcode.make(data)

img.save('C:/Users/saigi/OneDrive/Desktop/python projects/photos/qrcode.png')
