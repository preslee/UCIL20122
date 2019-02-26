#This class generates feedback on the cluster selection question
from numpy import *
import matplotlib.pyplot as plt
from IPython.display import display
from Widget import *

class getFeedbackOnClusters:
    #The object takes a Widget object as argument
    def __init__(self, WidgetObject):
        self.WidgetObject = WidgetObject
    
    #Create the feedback button
    def createButton(self, buttonName):
        self.button = widgets.Button(description = buttonName)
        
    #Display the button on the screen
    def displayButton(self):
        display(self.button)
        
    #Analyse and print the results from Widget
    def printFeedback(self, WidgetObject):
        if 'Top-left' in WidgetObject.getFeatureValues():
            print("\N{Heavy Check Mark} Your answer is correct. Generally, rugby players are heavier and smaller than ballet dancers.")
        else:
            print("\N{Cross Mark} I'm afraid you are wrong. Generally, rugby players are heavier and smaller than ballet dancers.")
        
        rugbyHeights = [150, 145, 130, 163, 171, 168]
        rugbyWeights = [85, 93, 75, 99, 100, 84]
        
        balletHeights = [190, 185, 202, 180, 174, 174]
        balletWeights = [63, 55, 75, 50, 57, 66]

        plt.scatter(rugbyHeights, rugbyWeights, color = 'red', marker = '^')
        plt.scatter(balletHeights, balletWeights, color = 'blue')
        plt.title("Data distribution on heights and weights")
        plt.xlabel("Height")
        plt.ylabel("Weight")
        plt.show()
