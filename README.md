# Morron and Photos backend
## Includes timelapse de un morrón, pepper bell
Una web en Flask que recibe hasta 3 fotos de un bot de Telegram y las muestra.
También tiene una sección para ver una planta en vivo.

Copyright 2024 Ramiro Iván Ríos.

# Pasos para reproducir
## Backend web
- update & upgrade!
- crear entorno virtual
- pip install flask
- pip install opencv-python
- python threephotos.py
- a gozar.

## Raspberry pi zero w: THE ELDER FEAR
- me encontré con esta joyita: https://forums.raspberrypi.com/viewtopic.php?t=323247 
--- básicamente: rpi0w tiene ARM6 de 32 bits. Y es OBSOLETO para opencv.
--- comentario aparte: hay que tener empatía chicos, la pedagogía no funciona a las piñas, eso no es pedagogía, eso es programación condicional.
- voy a optar por tan solo:
--- enviar la imágen al backend web
--- procesar la imágen en el backend... No se puede con una cuenta gratis XD porque tiene 500mb de espacio y OpenCV ocupa más de eso.

## Opción 3, el salvador de siempre: JAVASCRIPT
- voy a rotar la imágen con un poco de magia de JS CSS HTML y esas yerbas.
- por el momento actual, la idea es desplegar un archivo python como servicio.
- el servicio saca una foto cada X tiempo
- guarda la foto y la sube al backend web.

- update & upgrade!
- crear entorno virtual
- pip install requests
- crontab en el raspberry: 0-59/3 13 * * * /usr/bin/python /home/ra/ojoalaji/python_service/ojoalaji.py