import cv2
import numpy as np
import requests
import os

# URL dari gambar
url = 'https://i.ibb.co/LZ9QtBx/photo-2022-05-14-19-06-30.jpg'

# Mengunduh gambar dari URL
response = requests.get(url)
image_array = np.array(bytearray(response.content), dtype=np.uint8)

# Mengkonversi array byte ke format gambar OpenCV
gambar = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# Menampilkan gambar
cv2.imshow('Gambar', gambar)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Membersihkan terminal setelah menampilkan gambar
if os.name == 'nt':  # untuk Windows
    os.system('cls')
else:  # untuk Mac dan Linux
    os.system('clear')



