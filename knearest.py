#This class makes predictions based on KNearest for 2 features
import numpy as np
from numpy import *
from IPython.display import display
from InputWidget import *
import math

class knearest:
    #The object takes two InputWidget objects as arguments and a training matrix
    def __init__(self, InputWidgetObject1, InputWidgetObject2, inputTrainingMatrix):
        self.InputWidgetObject1 = InputWidgetObject1
        self.InputWidgetObject2 = InputWidgetObject2
        self.inputTrainingMatrix = inputTrainingMatrix
        self.distances = np.empty([0,2])
    
    #Create the button
    def createButton(self, buttonName):
        self.button = widgets.Button(description = buttonName)
        
    #Display the button on the screen
    def displayButton(self):
        display(self.button)
        
        
    #Find the k-nearest neighbours
    def getLabel(self, k):
        
        #Calculate the distances
        for trainingPoint in self.inputTrainingMatrix:
            distance = math.sqrt((trainingPoint[0] - self.InputWidgetObject1.getValue())**2 + (trainingPoint[1] - self.InputWidgetObject2.getValue())**2)
            self.distances = np.vstack([self.distances, [distance, trainingPoint[2]]])
            
        #Sort the distances    
        self.distances = self.distances[self.distances[:,0].argsort()]

        classOne = 0
        classTwo = 0

        for i in range(0, int(len(heights)/2)):
            if self.distances[i][1] == 1:
                classOne = classOne + 1
            else:
                classTwo = classTwo + 1

        if classOne > classTwo:
            return 1
        else:
            return 2
            
    
    #Print the results
    def printPrediction(self, classOneName, classTwoName, k):
        if self.getLabel(k) == 1:
            print (classOneName)
        else:
            print (classTwoName)