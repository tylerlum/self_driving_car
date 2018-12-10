import socketio
import eventlet
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

sio = socketio.Server()
app = Flask(__name__) #'__main__'
speed_limit = 10

def img_preprocess(img):
    """Preprocess image with cropping, YUV, Gaussian blur, resize, normalize"""
    img = img[60:135, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

## Every loop, set steering angle based on image
@sio.on('telemetry')
def telemetry(sid, data):
    ## Prepare image
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image])

    ## Set throttle based on current speed
    speed = float(data['speed'])
    throttle = 1.0 - speed / speed_limit

    ## Predict steering angle
    steering_angle = float(model.predict(image))
    print('{} {} {}'.format(steering_angle, throttle, speed))
    send_control(steering_angle, throttle)

## On startup, set speed to 0
@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0, 0)

## Set steering angle and throttle
def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })

if __name__ == '__main__':
    model = load_model('models/model5.h5')
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
