class Passenger:
    def __init__(self, name, surname, country, age):
        self.name = name
        self.surname = surname
        self.country = country
        self.age = age

passengers = []

test = {'ostin':['power', 'usa', 16], 'ammy':['second', 'greatbritain', 28], 'ruslan':['petrov', 'russia', 29], }

# for x in range(3):
#     passenger = Passenger(x, surname,)
#     passengers.append(passenger)

for item in test:
	a = test[item][0]
	b = test[item][1]
	c = test[item][2]
	passenger = Passenger(item, a, b, c)
	passengers.append(passenger)
print(passengers)

for passenger in passengers:
    print(passenger) # вывод будет примерно таким <__main__.Passenger object at 0x7f4b945992b0>
    print(passenger.name, passenger.surname, passenger.country, passenger.age)