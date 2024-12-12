from event import Event

#special event class
class SpecialEvent(Event):
    def __init__(self, eventID, eventLocation, category, vipFees):
        super().__init__ (eventID, eventLocation, category, vipFees)
        self._vipFees = vipFees
    #overwrite calculating event fees and fees getter
    def calculateEventFee(self):
        return float(self._vipFees) * 1.135
    def getFees(self):
        return self._vipFees

