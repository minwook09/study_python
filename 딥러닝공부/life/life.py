from random import shuffle
import pandas as pd

data = pd.read_csv('train.csv')

평균 = data['Age'].mean()
최빈값 = data['Embarked'].mode()

data['Age'].fillna(value = 30, inplace=True)
data['Embarked'].fillna(value='S', inplace=True)

#print(data.isnull().sum())

import tensorflow as tf

정답 = data.pop('Survived')
ds = tf.data.Dataset.from_tensor_slices( (dict(data), 정답))

feature_column = []

#숫자 Fare, SibSp Parch : numeric column
#뭉퉁그려서 집어넣을꺼  'Age' : bucketized column
#종류몇개 없는 카테고리화해서 집어넣을것(원핫인코딩) Sex Embarked Pclass : indicator column
#종류가 넘 많은 카테고리 Ticket : embedding column

def normal(x):
    최소 = data['Fare'].min()
    최대 = data['Fare'].max()

    return (x-최소)/(최대-최소)

feature_column.append(tf.feature_column.numeric_column('Fare',normalizer_fn=normal))
feature_column.append(tf.feature_column.numeric_column('Parch'))
feature_column.append(tf.feature_column.numeric_column('SibSp'))

Age = tf.feature_column.numeric_column('Age')
Age_buket = tf.feature_column.bucketized_column(Age, boundaries=[10,20,30,40,50,60] )
feature_column.append(Age_buket)

vocab = data['Sex'].unique()
cate =tf.feature_column.categorical_column_with_vocabulary_list('Sex',vocab)
one_hot = tf.feature_column.indicator_column(cate)
feature_column.append(one_hot)

vocab = data['Embarked'].unique()
cate =tf.feature_column.categorical_column_with_vocabulary_list('Embarked',vocab)
one_hot = tf.feature_column.indicator_column(cate)
feature_column.append(one_hot)

vocab = data['Pclass'].unique()
cate =tf.feature_column.categorical_column_with_vocabulary_list('Pclass',vocab)
one_hot = tf.feature_column.indicator_column(cate)
feature_column.append(one_hot)


#embedding
vocab = data['Ticket'].unique()
cate =tf.feature_column.categorical_column_with_vocabulary_list('Ticket',vocab)
one_hot = tf.feature_column.embedding_column(cate, dimension=9)
feature_column.append(one_hot)

model= tf.keras.Sequential([
    tf.keras.layers.DenseFeatures(feature_column),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(64, activation = 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['acc'])
ds_batch = ds.batch(32)
model.fit(ds_batch,  shuffle=True, epochs = 20)

'''
ds_batch = ds.batch(32)
next(iter(ds_batch))[0]
feature_layer = tf.keras.layers.DenseFeatures(tf.feature_column.numeric_column('Fare'))
feature_layer(next(iter(ds_batch))[0])

batch 하나 넣어보기
'''