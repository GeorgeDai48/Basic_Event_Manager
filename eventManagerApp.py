import event
import specialEvent

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
            pass
        elif selection == 'adds':
            pass
        elif selection == 'calc':
            pass
        elif selection == 'exit':
            print ('Exiting the app')
            exit()
        else:
            print ('Input not recognized')
            continue
                           



run()