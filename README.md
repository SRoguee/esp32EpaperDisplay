This is a project I am working on that will display images or information while sitting on my desk like a dynamic photo frame.

It works by having the esp32 wake from deepsleep to connect to my home server, authenticate itself through caddy basic auth and
request an image from a list of greyscale binary files and then display it on a 16 level grayscale epaper screen and going back to sleep
until the next request.

The esp32 does not store any image locally by default unless you add a microsd card. It requests images from the server which when an 
image is uploaded will crop and scale the image to fit the screen before converting it to a 4 bit binary file.

Users may upload images through a self hosted webpage which accepts only image files and upon recieving a post signal triggers a flask
method to save the file to a directory which is watched by a systemd service for changes so that any new images can be converted by converter.py.
