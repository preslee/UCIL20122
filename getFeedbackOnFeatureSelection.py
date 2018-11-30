#This class generates feedback on the feature selection question
from IPython.display import display
from Widget import *

class getFeedbackOnFeatureSelection:
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
        if 'Height' in WidgetObject.getFeatureValues():
            print("\N{Heavy Check Mark} The height is a distinguishing measurement as normally ballet dancers are taller than rugby players.")
        else:
            print("\N{Cross Mark} You missed the height measurement. Normally, ballet dancers are taller than rugby players.")

        if 'Weight' in WidgetObject.getFeatureValues():
            print("\N{Heavy Check Mark} The average weight of an England rugby player is 105 kg. A ballet dancer's weight is between 40 - 60 kg.")    
        else:
            print("\N{Cross Mark} You missed the weight measurement. On average an England rugby player weights 105 kg whereas normally a ballet dancer does't weight more than 60 kg.")

        if 'Age' in WidgetObject.getFeatureValues():
            print("\N{Cross Mark} In this case, the age is not really an indicator as more rugby players and ballet dancers have the same age.")

        if 'Sex' in WidgetObject.getFeatureValues():
            print("\N{Cross Mark} Sex is not a good indicator as both rugby and ballet are practiced by men and women.")

        if 'Name' in WidgetObject.getFeatureValues():
            print("\N{Cross Mark} The name is irrelevant as it does't give any clue about a person.")
