# Create an instance of Dropdown menu

import ipywidgets as widgets

class Dropdown:
    def __init__(self, DropdownOptions, DropdownDescription):
        self.DropdownOptions = DropdownOptions
        self.DropdownDescription = DropdownDescription
        
    
    #Create a Dropdown to select one single option
    def createDropdown(self):
        self.features = widgets.Dropdown(
            options=self.DropdownOptions,
            description=self.DropdownDescription,
            disabled=False,
        )
    
    
    #Return the array of the selected value
    def getValue(self):
        return self.features.value
    
    #Return the array of options
    def getFeatureOptions(self):
        return self.features.options
    
    #Display the options on the screen
    def displayDropdown(self):
        display(self.features)