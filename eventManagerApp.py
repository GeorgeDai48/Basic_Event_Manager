from event import Event
from specialEvent import SpecialEvent

def run():
    print ("Event Manager - [George Dai]")
    eventsCollection = []
    def addReg():
        eventID = input ('Please enter the event ID: ')
        eventLocation = input ('Please enter the event location: ')
        category = input ('Please enter the event category: ')
        while True:
            fees = input ('please enter the event fees: ')
            if fees.replace('.','').isnumeric():
                break
            print ('please enter a positive numeric value: ')
            
        event = Event(eventID, eventLocation, category, fees)
        print ('Event added')
        eventsCollection.append (event)
    def addSpec():
        eventID = input ('Please enter the special event ID: ')
        eventLocation = input ('Please enter the special event location: ')
        category = input ('Please enter the special event category: ')
        while True:
            vipFees = input ('please enter the special event fees: ')
            if vipFees.replace('.','').isnumeric():
                break
            print ('please enter a positive numeric value: ')
        specEvent = SpecialEvent(eventID, eventLocation, category, vipFees)
        print ('Special event added')
        eventsCollection.append (specEvent)
    def calc():
        fees = input ('Please enter the fees for the regular event: ')
        specfees = input ('Please enter the fees for the special event: ')
        totFees = 0
        for events in eventsCollection:
            totFees += events.calculateEventFee()
        return totFees

        
    while True:
        selection = input ('''Select what you would like to do:
"1" to add a regular event
"2" to add a special event
"3" to calculate event fees for all events
"4" to exit the app
''')
        if selection == '1':
            addReg()
        elif selection == '2':
            addSpec()
        elif selection == '3':
            calc()
        elif selection == '4':
            print ('Exiting the app')
            exit()
        else:
            print ('Input not recognized')
            continue
                           
    




run()