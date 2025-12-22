#Lesson 1 Practice
def eventDate(event):
    return event.date

def currentUsers(events):
    events.sort(key=eventDate)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            # use discard to avoid KeyError if the user isn't present
            machines[event.machine].discard(event.user)
    return machines

def generateReport(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            userList = ', '.join(users)
            print("{}: {}".format(machine, userList))


# Example usage:
class Event:
    def __init__(self, date, type, user, machine):
        self.date = date
        self.type = type
        self.user = user
        self.machine = machine
    def __repr__(self):
        return "Event({}, {}, {}, {})".format(self.date, self.type, self.user, self.machine)

events = [
    # Event is now defined above; date is an ISO-like string so sorting works lexicographically
    Event('2024-01-01 10:00', 'login', 'alice', 'machine1'),
    Event('2024-01-01 10:05', 'login', 'bob', 'machine1'),
    Event('2024-01-01 10:10', 'logout', 'alice', 'machine1'),
    Event('2024-01-01 10:15', 'login', 'charlie', 'machine2'),
]

currentUsersData = currentUsers(events)
print(currentUsersData)
generateReport(currentUsersData)
print("Report generated.")