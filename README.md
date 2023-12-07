# Emotion-based-music-recommendation-system-using-facial-recognition

## Overview
This project implements an Emotion Recognition and Entertainment Recommendation System using deep learning and facial expression analysis. The system captures facial expressions through a webcam, predicts the emotion, and recommends movies or songs based on the detected emotion.

## Features
### Emotion Recognition:

Utilizes pre-trained deep learning models (MTCNN, TensorFlow/Keras) to detect facial expressions.
Classifies emotions into categories such as angry, disgust, fear, happy, sad, neutral, and surprise.

### Entertainment Recommendations:

Recommends both Hindi and English songs based on the detected emotion.
Provides a user-friendly interface for interacting with the system.

### Web Application:

Developed using Flask, a web framework in Python.

### Requirements
Python 3.x
Flask
OpenCV
TensorFlow
Keras
MTCNN

## Abstract 
Systems for making music recommendations have been around for a while, but choosing from the large range of available music can be difficult for many people. Humans frequently use their facial expressions to convey their messages more effectively. Keeping this in mind, we propose a new method of music recommendation in which a person's sentiment is detected from their webcam-captured facial expression. When a user's facial expressions are picked up by the system, it extracts facial landmarks that can be used to categorize the user's emotional state. Once the emotion has been determined, the user will be presented with a list of songs that most accurately reflect their current mood. Following the user's selection of one song, other tracks in the same genre or style will be suggested. The system's overall goal is to effectively identify facial emotion and make song recommendations. 

## Methodology
Our project is trained on an MTCNN (Multi-Task Cascaded Convolutional Networks) model using the FER (Facial Emotion Recognition) updated dataset, with a goal to classify facial expressions into distinct emotion categories, including sadness, happiness, neutrality, surprise, fear, and anger. In this project, we address the crucial task of robust emotion recognition from facial images, catering to real-world applications where nuanced and complex emotions are prevalent. We have leveraged deep learning techniques to capture subtle features in facial expressions and successfully classify them into multiple emotional states. The project encompasses data preprocessing, model training, validation, and testing phases, and it underscores the challenges of handling diverse expressions, variations in lighting, and demographic factors. The accuracy and reliability of our MTCNN-based emotion recognition model position it as a valuable tool for applications spanning human-computer interaction, sentiment analysis, and personalized content recommendation. 

## Dataset used 
FER 2013 updated dataset


