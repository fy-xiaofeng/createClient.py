import os
import base64

with open('icon.ico', 'rb') as f:
    img_data = base64.b64encode(f.read())
with open('icon.py', 'w+') as f:
    f.write('img=%s' % img_data)

