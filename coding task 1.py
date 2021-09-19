

import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense

input_features = np.array([[2,3]])



weights = np.array([[0.1],[0.2]])



model = Sequential()

#adding input & hiddenlayer

model.add(Dense(output_dim = 4, init = 'uniform', activation = 'relu', input_dim = 2))


#output layer

model.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

#compile
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

output = model.predict()