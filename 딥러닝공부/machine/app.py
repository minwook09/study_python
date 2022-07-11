import tensorflow as tf

텐서 = tf.constant([3.0,4.0,5], tf.float32) #tf.cast datatype바꿀 수
텐서2 = tf.constant([6,7,8])
텐서3 = tf.constant([[1,2],[3,4]])
텐서4 = tf.constant([[2,3],[3,4]])

#print(tf.matmul(텐서3,텐서4)) #행렬곱 AB dot

텐서5 = tf.zeros([2,2,3])  #tensor 의 shape
#print(텐서) #실수 float

w = tf.Variable(1.0) #weight값 변수이기때문에 variables
w.assign(2) #값 변경
print(w.numpy())#실제 숫자 return