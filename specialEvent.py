from event import Event

class SpecialEvent(Event):
    def __init__(self, eventID, eventLocation, category, vipFees):
        super().__init__ (eventID, eventLocation, category, vipFees)
        self._vipFees = vipFees
    def calculateEventFee(self):
        return float(self._vipFees) * 1.135


