import qrcode

Data="https://www.google.com/"

qr=qrcode.make(data=Data)

qr.save('my_qrcode.png')


print('qrcode is creat ✅')
