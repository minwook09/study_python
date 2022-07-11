import numpy as np
import tensorflow as tf
import pandas as pd

data=pd.read_csv('gpascore.csv')
#print(data.isnull().sum()) #빈칸 세주기
#data.fillna(100)#빈칸 채우기
data=data.dropna()

y데이터 = data['admit'].values
x데이터 = []
for i, rows in data.iterrows():
    x데이터.append([rows['gre'],rows['gpa'],rows['rank']])

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'), #숫자는 노드
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(x데이터), np.array(y데이터), epochs=1000) #epochs 몇번 학습할래?

#예측
pred = model.predict([[750,3.70,3],[450,2.8,1]])
print(pred)

#딥러닝 성능향상은 연구과정 실험이 최고다.