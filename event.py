class Event:
    def __init__ (self, eventID, eventLocation, category):
        self._eventID = eventID       
        self._category = category
        self._eventLocation = Event.setEventLocation(self, eventLocation)
    
    def getEventID(self):
        return self._eventID
    def getEventLocation(self):
        return self._eventLocation
    def getCategory(self):
        return self._category
    def setEventLocation(self, eventLocation):
        try:
            if eventLocation == '':
                raise ValueError ('Location is blank/not all alphabetic')
            elif eventLocation.isalpha() == False:
                raise ValueError ('Location is blank/not all alphabetic')
            else:
                return eventLocation
        except ValueError as error:
            print("Exception: ", error)
            return eventLocation
    def calculateEventFee(self, eventFee):
        return eventFee * 1.135
    
#testing    
event = Event (1, 'g5', 'yes')
print (event.getEventLocation())
print (event.getEventID())