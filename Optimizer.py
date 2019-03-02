#This class is the optimizer for the Neural Network of Titanic dataset
from InputWidget import *
from IPython.display import display

class Optimizer:
    #Define the constructor
    def __init__(self, InputWidgetObject1, InputWidgetObject2, InputWidgetObject3, Dropdown1, Dropdown2, Dropdown3, Dropdown4, trainFeatures, trainLabels, testFeatures, testLabels):
        self.InputWidgetObject1 = InputWidgetObject1
        self.InputWidgetObject2 = InputWidgetObject2
        self.InputWidgetObject3 = InputWidgetObject3
        self.Dropdown1 = Dropdown1
        self.Dropdown2 = Dropdown2
        self.Dropdown3 = Dropdown3
        self.Dropdown4 = Dropdown4
        
    #Create the button
    def createButton(self, buttonName):
        self.button = widgets.Button(description = buttonName)
        
    #Display the button on the screen
    def displayButton(self):
        display(self.button)
        
    #Create the model based on the inputs
    def createModel(self):
        np.random.seed(7)
        model = keras.models.Sequential()

        structure = [7 , self.InputWidgetObject1.getValue(), self.InputWidgetObject2.getValue(), 2]

        # Input layer + hidden layer 1
        model.add(keras.layers.Dense(units=structure[1], input_dim = structure[0], activation = self.Dropdown1.getValue()))

        # Hidden layer 2
        model.add(keras.layers.Dense(units=structure[2], activation = self.Dropdown2.getValue()))

        # Output layer
        model.add(keras.layers.Dense(units=structure[3], activation = self.Dropdown3.getValue()))

    def compileModel(self):
        
        model.compile(loss = 'categorical_crossentropy', optimizer = Dropdown4.getValue(), metrics = ['accuracy'])


        print('Starting training')

        training_stats = model.fit(self.trainFeatures, self.trainLabels, batch_size = 1, epochs = self.InputWidgetObject3.getValue(), verbose = 0)

        print('Training finished')
        print('Training Evaluation: accuracy = %0.2f%%'
              %(100 * training_stats.history['acc'][-1]))
        
    def printTestingAccuracy(self):
        evaluation = model.evaluate(self.testFeatures, self.testLabels, verbose=0)
        print('Test Set Evaluation: accuracy = %0.2f%%' %(100*evaluation[1]))
        