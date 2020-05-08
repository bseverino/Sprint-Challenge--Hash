#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    route = [None] * length
    current_source = "NONE"

    for i in range(length):
        route[i] = cache[current_source]
        current_source = cache[current_source]

    return route

tickets = [
    Ticket( "PIT", "ORD" ),
    Ticket( "XNA", "CID" ),
    Ticket( "SFO", "BHM" ),
    Ticket( "FLG", "XNA" ),
    Ticket( "NONE", "LAX" ),
    Ticket( "LAX", "SFO" ),
    Ticket( "CID", "SLC" ),
    Ticket( "ORD", "NONE" ),
    Ticket( "SLC", "PIT" ),
    Ticket( "BHM", "FLG" )
]

print(reconstruct_trip(tickets, 10))