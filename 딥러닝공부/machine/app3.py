import tensorflow as tf

train_x = [1,2,3,4,5,6,7]
train_y = [3,5,7,9,11,13,15]

#예측_y = train_x * a + b

a = tf.Variable(0.1)
b = tf.Variable(0.1)

def 손실함수(a,b):
    예측_y = train_x * a + b #행렬 연산처럼 리스트 각각 연산
    return tf.keras.losses.mse(train_y, 예측_y)

opt = tf.keras.optimizers.Adam(learning_rate=0.01) #실험적으로  러닝레이트

for i in range(3000):
    opt.minimize(lambda:손실함수(a,b), var_list=[a,b])
    print(a.numpy(),b.numpy())

#생각해보니 이건 딥러닝 아님 히든 레이어가 읎어요

