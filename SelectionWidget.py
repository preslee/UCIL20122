# Create an instance of SelectionWidget
# The WidgetOptions variable should be an array of options

import ipywidgets as widgets

class SelectionWidget:
    def __init__(self, WidgetOptions, WidgetDescription):
        self.WidgetOptions = WidgetOptions
        self.WidgetDescription = WidgetDescription
        
    
    #Create a SelectionWidget to select multiple options
    def createSelectMultiple(self):
        self.features = widgets.SelectMultiple(
            options = self.WidgetOptions,
            description = self.WidgetDescription,
            disabled = False
        )
        
    #Create a SelectionWidget to select one single option
    def createSelectSingle(self):
        self.features = widgets.Select(
            options = self.WidgetOptions,
            description = self.WidgetDescription,
            disabled = False
        )
    
    
    #Return the array of selected values
    def getFeatureValues(self):
        return self.features.value
    
    #Return the array of options
    def getFeatureOptions(self):
        return self.features.options
    
    #Display the options on the screen
    def displayWidget(self):
        display(self.features)