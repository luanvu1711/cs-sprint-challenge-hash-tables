#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

cache = {}

def reconstruct_trip(tickets, length):
    # create an empty route array
    route = []
    # for every ticket in the tickets array,
    # add the ticket to the cache by using
    # the ticket source as the key, and 
    # the ticket destination as the value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # initial setup, knowing the original flight has a source of NONE
    # append it to the list with the key NONE from the cache
    route.append(cache['NONE'])

    # iterate over the length of the tickets array,
    # finding the next value in the routes array
    for index in range(length):
        # if the value from route is in the cache (which it should be)
        if route[index] in cache:
            # first check to make sure we aren't re-adding the initial value
            if cache[route[index]] == route[0]:
                continue
            # add the remaining stops to the route array,
            # by grabbing the value at route[index]
            # and pulling it's value out of the cache
            route.append(cache[route[index]])

    # when we get to this point, we have a full route
    return route


# test set up to reduce reliance on unit tests
if __name__ == "__main__":
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    print(reconstruct_trip(tickets, len(tickets)))

    # expected:  expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP", "SLC", "PIT", "ORD", "NONE"]