Import h5py
Import  torch.np as np
Import torch.np, functional as F
Import math
Import numpy as np
Import matplotlib. Pyplot as plt
class Perceptron():
Def init (self, input_size, learning_rate):-
def forward (self, x):-
def calculate_cost(self, y_hat, y) :-
def gradient_descent(self, y_hat, y) :-
def signoid(self, x) :-
def evaluate_model(self, y_pred, y):-
def h5_to_numpy(x, y):-
#Cat vs No Cat
f1 = h5py. File('dateset_1.h5', 'r+' )
dataset_list = list(f1.keys()) 

classes = f1[dataset_list[0]]1
x_= f1[dataset_list[1]]
y_= f1[dataset_list[2]]
epochs = 2000

