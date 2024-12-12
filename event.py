class Event:
    def __init__ (self, eventID, eventLocation, category):
        self._eventID = eventID
        self._eventLocation = eventLocation
        self._category = category
    
    def getEventID(self):
        return self._eventID
    def getEventLocation(self):
        return self._eventLocation
    def getCategory(self):
        return self._category
    def setEventLocation(self):
        try:
            if self._eventLocation == '':
                raise ValueError ('Location is blank/not all alphabetic')
            elif self._eventLocation.isalpha() == False:
                raise ValueError ('Location is blank/not all alphabetic')
            else:
                return self._eventLocation
        except ValueError as error:
            print("Exception: ", error)