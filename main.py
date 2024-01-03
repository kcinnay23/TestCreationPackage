import numpy as np
from YannPackage.model import Model
from YannPackage.loss import Loss
from YannPackage.dense import Dense
from YannPackage.sigmoid import Sigmoid


X = np.array([[ 2,  3, -2],
       [ 4,  5, -1],
       [-5,  2,  3],
       [ 0,  5,  4]])

Y = np.random.randn(4, 1)

sigmoid = Sigmoid()

model = Model(layers = [ Dense(neurons=2, activation=sigmoid),
       Dense(neurons=1)])
mse = Loss()
model.compile(loss=mse, learning_rate=0.01)
h = model.fit(X, Y, epochs=10)