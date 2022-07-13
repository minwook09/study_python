import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


(trainX,trainY), (testX,testY) = tf.keras.datasets.fashion_mnist.load_data()

#print(trainX[0])
#print(trainX.shape)

trainX = trainX/ 255.0 #0~255를 0~1로 압축해서 넣음 다 255로 나눔
testX = testX/ 255.0

trainX = trainX.reshape((trainX.shape[0],28,28,1))
testX = testX.reshape((testX.shape[0],28,28,1))

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal','Shirt','Sneaker', 'Bag', 'Ankleboot']

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3), padding="same", activation='relu', input_shape=(28,28,1)), #이미지 복사본 갯수, (커널사이즈)
    tf.keras.layers.MaxPooling2D((2,2)), #pooling 크기
    #tf.keras.layers.Dense(128,input_shape=(28,28) ,activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
])
model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer='adam', metrics=['accuracy']) #sparse아닐때 원핫인코딩 1 : [0,1,0,0]
model.fit(trainX,trainY,validation_data=(testX,testY) ,epochs=5)

#score = model.evaluate(testX,testY) #컴퓨터 첨보는거 
#print(score)

#그래서 val accuracy가 높은 방향으로 가는 것을 연구

