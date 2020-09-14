#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    t_dict = {} 
    o_flights = [] 

    for ticket in tickets: 
        t_dict[ticket.source] = ticket.destination

    destination = t_dict['NONE']

    while destination != 'NONE':
        o_flights.append(destination)
        destination = t_dict[destination]
    
    o_flights.append(destination)

    return o_flights

#* ALL TESTS PASSED
