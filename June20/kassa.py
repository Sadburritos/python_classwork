from ticket import Ticket

class Kassa:
    balance = 0
    tickets = []

    def get_price(self, source, destination):
        return (len(source) + len(destination)) * 1000

    def buy_ticket(self, source, destination, person):
        money = person.pay( self.get_price(source, destination) )
        if money:
            self.balance += money
            new_ticket = Ticket(source, destination, person.name, person.iin, person.age)
            self.tickets.append(new_ticket)
            print("Tiket number is ", new_ticket.number)
        else:
            print("No money - no ticket!")
    def get_ticket(self, iin, source, destination):
            for x in self.tickets:
                if x.source == source and x.destination == destination and x.passenger_iin == iin:
                    return x 

    def delite_ticket(self, ticket):
        self.tickets.remove
print("kassa", __name__)