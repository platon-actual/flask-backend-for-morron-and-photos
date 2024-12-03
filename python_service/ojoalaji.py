# Ramiro Iván Ríos copyright 2024

import subprocess
import requests
import os

print("Creando carpeta con subprocess...")
subprocess.run(['mkdir','photos_morron'])
print("Fin.")

print("Sacando foto con subp.")

CURRENT_DIR = os.getcwd()
IMAGE_NAME = 'test_morron'
IMAGE_FILE = IMAGE_NAME + '.jpg'
IMAGE_FINAL = os.path.join(CURRENT_DIR, IMAGE_FILE)

subprocess.run(['rpicam-still','-o', IMAGE_FINAL])
print(" - Foto tomada. -")

# Rotar la imágen 90 grados:
# non_rotated_image = cv2.imread(IMAGE_FILE)
# rotated_image = cv2.rotate(non_rotated_image, cv2.ROTATE_90_CLOCKWISE)

# Guardar la imágen final
# cv2.imwrite(IMAGE_FINAL, rotated_image)

print("Subiendo la imágen a ramirorios.pythonanywhere.com...")
# subo la imagen al backend:
# url = 'https://ramirorios.pythonanywhere.com/post_morron_image'
url = r'http://ramirorios.pythonanywhere.com/post_pepper_morron'
# my_morron = {'morron_image': ( IMAGE_FILE, open(IMAGE_FILE, 'rb'), 'multipart/form-data' )}
my_morron = {'morron_image': open(IMAGE_FINAL, 'rb')}
response = requests.post(url, files=my_morron)

print(response.json)

print('El dir actual es: ' + os.getcwd())
print('- Fin. -')
