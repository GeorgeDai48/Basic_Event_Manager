from event import Event
from specialEvent import SpecialEvent

def run():
    print ("Event Manager - [George Dai]")
    eventsCollection = []
    while True:
        selection = input ('''Select what you would like to do:
"addr" to add a regular event
"adds" to add a special event
"calc" to calculate event fees for all events
"exit" to exit the app
''')
        if selection == 'addr':
            addReg()
        elif selection == 'adds':
            addSpec()
        elif selection == 'calc':
            calc()
        elif selection == 'exit':
            print ('Exiting the app')
            exit()
        else:
            print ('Input not recognized')
            continue
                           
def addReg():
    eventID = input ('Please enter the event ID: ')
    eventLocation = input ('Please enter the event location: ')
    category = input ('Please enter the event category: ')
    event = Event(eventID, eventLocation, category)
    print ('Event added')
def addSpec():
    eventID = input ('Please enter the special event ID: ')
    eventLocation = input ('Please enter the special event location: ')
    category = input ('Please enter the special event category: ')
    event = SpecialEvent(eventID, eventLocation, category)
    print ('Special event added')
def calc():
    fees = input ('Please enter the fees for the regular event: ')
    specfees
run()