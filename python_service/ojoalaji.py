# Ramiro Iván Ríos copyright 2024

import subprocess
import requests

print("Creando carpeta con subprocess...")
subprocess.run(['mkdir','photos_morron'])
print("Fin.")

print("Sacando foto con subp.")
IMAGE_NAME = 'test_morron'
IMAGE_FILE = IMAGE_NAME + '.jpg'
IMAGE_FINAL = 'morron.jpg'

subprocess.run(['rpicam-still','-o', IMAGE_FILE])
print(" - Foto tomada. -")

print("- Subiendo la imágen a ramirorios.pythonanywhere.com -")
url = r'http://ramirorios.pythonanywhere.com/post_pepper_morron'
my_morron = {'morron_image': ( IMAGE_FILE, open(IMAGE_FILE, 'rb'), 'multipart/form-data')}
response = requests.post(url, files=my_morron)
print(response.json)

print('- Fin. -')