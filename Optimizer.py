#This class is the optimizer for the Neural Network of Titanic dataset
from InputWidget import *
from IPython.display import display
import numpy as np
import tensorflow as tf
import keras

class Optimizer:
    #Define the constructor
    def __init__(self, InputWidgetObject1, InputWidgetObject2, InputWidgetObject3, Dropdown1, Dropdown2, Dropdown3, Dropdown4, trainFeatures, trainLabels, testFeatures, testLabels):
        self.InputWidgetObject1 = InputWidgetObject1
        self.InputWidgetObject2 = InputWidgetObject2
        self.InputWidgetObject3 = InputWidgetObject3
        self.trainFeatures = trainFeatures
        self.trainLabels = trainLabels
        self.testFeatures = testFeatures
        self.testLabels = testLabels
        self.Dropdown1 = Dropdown1
        self.Dropdown2 = Dropdown2
        self.Dropdown3 = Dropdown3
        self.Dropdown4 = Dropdown4
        self.model = keras.models.Sequential()
        
    #Create the button
    def createButton(self, buttonName):
        self.button = widgets.Button(description = buttonName)
        
    #Display the button on the screen
    def displayButton(self):
        display(self.button)
        
    #Create the model based on the inputs
    def createModel(self):
        np.random.seed(7)
        
        structure = [7 , self.InputWidgetObject1.getValue(), self.InputWidgetObject2.getValue(), 2]

        # Input layer + hidden layer 1
        self.model.add(keras.layers.Dense(units=structure[1], input_dim = structure[0], activation = self.Dropdown1.getValue()))

        # Hidden layer 2
        self.model.add(keras.layers.Dense(units=structure[2], activation = self.Dropdown2.getValue()))

        # Output layer
        self.model.add(keras.layers.Dense(units=structure[3], activation = self.Dropdown3.getValue()))

    def compileModel(self):
        
        self.model.compile(loss = 'categorical_crossentropy', optimizer = self.Dropdown4.getValue(), metrics = ['accuracy'])


        print('Starting training')

        training_stats = self.model.fit(self.trainFeatures, self.trainLabels, batch_size = 1, epochs = self.InputWidgetObject3.getValue(), verbose = 0)

        print('Training finished')
        print('Training Evaluation: accuracy = %0.2f%%'
              %(100 * training_stats.history['acc'][-1]))
        
    def printTestingAccuracy(self):
        evaluation = self.model.evaluate(self.testFeatures, self.testLabels, verbose=0)
        print('Test Set Evaluation: accuracy = %0.2f%%' %(100*evaluation[1]))
        
    def resetModel(self):
        self.model.reset_states()
        