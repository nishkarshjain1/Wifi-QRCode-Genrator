import qrcode
from datetime import datetime

now = datetime.now()
timestamp = round(datetime.timestamp(now))

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
ssid= 'Wifi name'
security = 'WPA'
password = 'Password'
data=f'WIFI:S:{ssid};T:{security};P:{password};;'
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr"+str(timestamp)+".png")
