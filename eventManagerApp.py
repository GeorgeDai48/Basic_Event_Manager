from event import Event
from specialEvent import SpecialEvent
import csv
import os.path

def run():
    
    eventsCollection = []
    #add regular event function
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
    #add special event function
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
    #calculate fees function
    def calc():
        totFees = 0
        for events in eventsCollection:
            totFees += events.calculateEventFee()
        return totFees
    #saving data function
    def saveDataToFile():
        with open ('events.csv','w', newline='') as file:
            writer = csv.writer (file)
            for event in eventsCollection:
                writer.writerow ([event.getEventID(), event.getEventLocation(), event.getCategory(), event.getFees()])
    #opening file function
    def loadDataFromFile():
        with open ('events.csv','r') as file:
            reader = csv.reader (file)
            for row in reader:
                event = Event(row[0], row[1], row[2], row[3])
                eventsCollection.append(event)
    if os.path.isfile("events.csv"):
        loadDataFromFile()
    print ("Event Manager - [George Dai]")
    #main menu input loop 
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
            totFees = calc()
            print (f'The total fees are: {totFees}')
        elif selection == '4':
            saveDataToFile()
            print ('Exiting the app')
            exit()
        else:
            print ('Input not recognized')
            continue
                           
    




run()