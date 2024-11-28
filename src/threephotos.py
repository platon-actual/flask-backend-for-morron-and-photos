# Ramiro Iván Ríos (2024)

from flask import Flask, request, render_template, redirect, url_for
import os, shutil

IMAGES_FOLDER = 'static/downloads/images/'

NAME_IMAGE_1 = 'la_imagen_1.jpg'
NAME_IMAGE_2 = 'la_imagen_2.jpg'
NAME_IMAGE_3 = 'la_imagen_3.jpg'

app = Flask(__name__)

@app.route('/')
def show_images():
    # return render_template('index.html', images=[NAME_IMAGE_1, NAME_IMAGE_2, NAME_IMAGE_3])
    return render_template('live_plants.html')

@app.route('/threephotosbot')
def show_threephotos():
    return render_template('threephotos.html', images=[NAME_IMAGE_1, NAME_IMAGE_2, NAME_IMAGE_3])

@app.route('/ojoalaji')
def show_morron_albahaca():
    return render_template('live_plants.html')
    

@app.route('/post_image', methods=['POST'])
def upload_image():
    image = request.files['image_input']
    print (image.content_type)    
    move_images(image)
    
    # return url_for('show_images')
    return redirect('/')

@app.route('/post_pepper_morron', methods=['POST'])
def get_morron_image():
    morron_image = request.files['morron_image']
    save_image("morron.jpg", morron_image)
    return redirect('/')

@app.route('/test')
def test():
    destination_path = os.path.join(app.root_path, IMAGES_FOLDER + "la_imagen2.jpg")
    if(os.path.exists(destination_path)):
        print('- holi- EXISTE')
        return '<h1> existe</h1>'
    else:
        print('- chau - NO EXISTE')
        return '<h1> no existe</h1>'
    
def image_exists(filename):
    destination_path = os.path.join(app.root_path, IMAGES_FOLDER + filename)
    # Si existe la imagen 'filename' entonces devuelvo Verdadero. Sino, por defecto devuelve False.
    if( os.path.exists(destination_path) ):
        return True;
    return False;

def save_image(name, file):
    destination_path = os.path.join(app.root_path, IMAGES_FOLDER + name)
    file.save(destination_path)

def copy_image(origin, destination):
    origin_path = os.path.join(app.root_path, IMAGES_FOLDER + origin)
    destination_path = os.path.join(app.root_path, IMAGES_FOLDER + destination)
    shutil.copy(origin_path, destination_path)

def move_images(new_image):
    # Si hay al menos 2 imágenes:
    if image_exists(NAME_IMAGE_2):
        copy_image(NAME_IMAGE_2, NAME_IMAGE_3)
        copy_image(NAME_IMAGE_1, NAME_IMAGE_2)
        save_image(NAME_IMAGE_1, new_image)
    else:
        if not image_exists(NAME_IMAGE_1):
            save_image(NAME_IMAGE_1, new_image)
        else:
            copy_image(NAME_IMAGE_1, NAME_IMAGE_2)
            save_image(NAME_IMAGE_1, new_image)

def check_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

if __name__ == '__main__':
    # Crear carpetas download/images si no existe:
    check_directory(os.path.join(app.root_path, IMAGES_FOLDER))
    app.run(debug=True, host='0.0.0.0', port=4000)
    # app.run()