# Create an instance of InputWidget
# The inputName variable should be a string naming the input (e.g. features such as age, weight etc.)

import ipywidgets as widgets

class InputWidget:
    def __init__(self, inputName, defaultValue, minValue, maxValue):
        self.inputName = inputName
        self.defaultValue = defaultValue
        self.minValue = minValue
        self.maxValue = maxValue
        
    
    #Create a float type inputWidget
    def createFloatInputWidget(self):
        self.features = widgets.BoundedFloatText(
            value = self.defaultValue,
            min = self.minValue,
            max = self.maxValue,
            step=0.1,
            description = self.inputName,
            disabled = False
        )
        
    #Create an int type inputWidget
    def createIntInputWidget(self):
        self.features = widgets.BoundedIntText(
            value = self.defaultValue,
            min = self.minValue,
            max = self.maxValue,
            step=0.1,
            description = self.inputName,
            disabled = False
        )
    
    #Return the value in the box
    def getValue(self):
        return self.features.value
    
    #Display the inputWidget on the screen
    def displayInputWidget(self):
        display(self.features)