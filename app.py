from __future__ import division, print_function
import sys
import os
import cv2
import re
import numpy as np
import tensorflow as tf
import keras 
from keras.models import load_model
from keras.preprocessing import image
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import statistics as st
from mtcnn import MTCNN
#import dlib
import keyboard 
import nltk
import flask
from flask import Flask
from flask import render_template, request,jsonify
from chat import get_response


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index1.html")


# @app.route("/",methods=["GET"])
# def index_get():
#     return render_template("base.html")
# @app.route("/predict", methods = ['GET', 'POST'])
# def base():
#     return render_template("base.html")
    
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)



# DLIB 
# @app.route('/camera', methods=['GET', 'POST'])
# def camera():
#     i = 0
#     GR_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
#     model = tf.keras.models.load_model('final_model.h5')
#     detector = dlib.get_frontal_face_detector()
#     output = []
#     cap = cv2.VideoCapture(0)
    
#     while (i <= 30):
#         ret, img = cap.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = detector(gray)
        
#         for face in faces:
#             x, y, w, h = face.left(), face.top(), face.width(), face.height()
#             face_img = img[y:y+h, x:x+w]

#             resized = cv2.resize(face_img, (224, 224))
#             reshaped = resized.reshape(1, 224, 224, 3) / 255
#             predictions = model.predict(reshaped)

#             max_index = np.argmax(predictions[0])

#             emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'neutral', 'surprise')
#             predicted_emotion = emotions[max_index]
#             output.append(predicted_emotion)

#             cv2.rectangle(img, (x, y), (x + w, y + h), GR_dict[1], 2)
#             cv2.rectangle(img, (x, y - 40), (x + w, y), GR_dict[1], -1)
#             cv2.putText(img, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
#         i = i + 1

#         cv2.imshow('LIVE', img)
#         key = cv2.waitKey(1)
#         if key == 27:
#             cap.release()
#             cv2.destroyAllWindows()
#             break

#     print(output)
#     cap.release()
#     cv2.destroyAllWindows()
#     final_output1 = st.mode(output)
#     return render_template("buttons.html", final_output=final_output1)
# DLIB ENDS



# MTCNN
@app.route('/camera', methods=['GET', 'POST'])
def camera():
    i = 0
    GR_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
    model = tf.keras.models.load_model('kagglemodel.h5')
    detector = MTCNN()
    
    output = []
    cap = cv2.VideoCapture(0)
    
    while (i <= 30):
        ret, img = cap.read()
        faces = detector.detect_faces(img)

        for face in faces:
            x, y, w, h = face['box']
            face_img = img[y:y + h, x:x + w]

            resized = cv2.resize(face_img, (48, 48))
            reshaped = resized.reshape(1, 48, 48, 3) / 255
            predictions = model.predict(reshaped)

            max_index = np.argmax(predictions[0])

            emotions = ('angry', 'disgust', 'fear', 'happy', 'neutral', 'surprise', 'sad')
            predicted_emotion = emotions[max_index]
            output.append(predicted_emotion)

            cv2.rectangle(img, (x, y), (x + w, y + h), GR_dict[1], 2)
            cv2.rectangle(img, (x, y - 40), (x + w, y), GR_dict[1], -1)
            cv2.putText(img, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        i = i + 1

        cv2.imshow('LIVE', img)
        key = cv2.waitKey(1)
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
        
        # Add this section to check for Ctrl + Q
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    
    
    
    print(output)
    cap.release()
    cv2.destroyAllWindows()
    final_output1 = st.mode(output)
    return render_template("buttons.html", final_output=final_output1)
#     MTCNN ENDS
# @app.route('/templates', methods = ['GET','POST'])
# def buttons():
#     return render_template("base.html")

@app.route('/templates/buttons', methods = ['GET','POST'])
def buttons():
    return render_template("buttons.html")

@app.route('/movies/surprise', methods = ['GET', 'POST'])
def moviesSurprise():
    return render_template("moviesSurprise.html")

@app.route('/movies/angry', methods = ['GET', 'POST'])
def moviesAngry():
    return render_template("moviesAngry.html")

@app.route('/movies/sad', methods = ['GET', 'POST'])
def moviesSad():
    return render_template("moviesSad.html")

@app.route('/movies/disgust', methods = ['GET', 'POST'])
def moviesDisgust():
    return render_template("moviesDisgust.html")

@app.route('/movies/happy', methods = ['GET', 'POST'])
def moviesHappy():
    return render_template("moviesHappy.html")

@app.route('/movies/fear', methods = ['GET', 'POST'])
def moviesFear():
    return render_template("moviesFear.html")

@app.route('/movies/neutral', methods = ['GET', 'POST'])
def moviesNeutral():
    return render_template("moviesNeutral.html")

@app.route('/songs/surprise', methods = ['GET', 'POST'])
def songsSurprise():
    return render_template("songsSurprise.html")

@app.route('/songs/angry', methods = ['GET', 'POST'])
def songsAngry():
    return render_template("songsAngry.html")

@app.route('/songs/sad', methods = ['GET', 'POST'])
def songsSad():
    return render_template("songsSad.html")

@app.route('/songs/disgust', methods = ['GET', 'POST'])
def songsDisgust():
    return render_template("songsDisgust.html")

@app.route('/songs/happy', methods = ['GET', 'POST'])
def songsHappy():
    return render_template("songsHappy.html")

@app.route('/songs/happy/happy_don', methods=['GET', 'POST'])
def happy_don():
    return render_template("happy_don.html")

@app.route('/songs/happy/happy_ainvayi', methods=['GET', 'POST'])
def happy_ainvayi():
    return render_template("happy_ainvayi.html")

@app.route('/songs/fear', methods = ['GET', 'POST'])
def songsFear():
    return render_template("songsFear.html")

@app.route('/songs/neutral', methods = ['GET', 'POST'])
def songsNeutral():
    return render_template("songsSad.html")

@app.route('/templates/join_page', methods = ['GET', 'POST'])
def join():
    return render_template("join_page.html")

@app.route('/templates/contacts', methods = ['GET', 'POST'])
def contacts():
    return render_template("base.html")


# @app.route('/templates/', methods = ['GET', 'POST'])
# def contacts():
#     return render_template("base.html")

    
if __name__ == "__main__":
    app.run(debug=True)

# HARCASCADE
# @app.route('/camera', methods = ['GET', 'POST'])
# def camera():
#     i=0

#     GR_dict={0:(0,255,0),1:(0,0,255)}
#     model = tf.keras.models.load_model('final_model.h5')
#     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#     output=[]
#     cap = cv2.VideoCapture(0)
#     while (i<=30):
#         ret, img = cap.read()
#         faces = face_cascade.detectMultiScale(img,1.05,5)

#         for x,y,w,h in faces:

#             face_img = img[y:y+h,x:x+w] 

#             resized = cv2.resize(face_img,(224,224))
#             reshaped=resized.reshape(1,224,224,3)/255
#             predictions = model.predict(reshaped)

#             max_index = np.argmax(predictions[0])

#             emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'neutral', 'surprise')
#             predicted_emotion = emotions[max_index]
#             output.append(predicted_emotion)
            
            
            
#             cv2.rectangle(img,(x,y),(x+w,y+h),GR_dict[1],2)
#             cv2.rectangle(img,(x,y-40),(x+w,y),GR_dict[1],-1)
#             cv2.putText(img, predicted_emotion, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
#         i = i+1

#         cv2.imshow('LIVE', img)
#         key = cv2.waitKey(1)
#         if key == 27: 
#             cap.release()
#             cv2.destroyAllWindows()
#             break
#     print(output)
#     cap.release()
#     cv2.destroyAllWindows()
#     final_output1 = st.mode(output)
#     return render_template("buttons.html",final_output=final_output1)
# HARCASCADE END     