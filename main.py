#!/usr/bin/python3

from classes import hotels

inputPrice = input("Введите сумму: ")

hotels_dict = {'Atlantic Castle Hotel':[3, 45000], 'Oriental Tide Hotel & Spa':[5, 92000], 'Bronze Mansion Resort': [4, 84000], 'Parallel Harbor Hotel':[4, 80000], 'Obsidian Vertex Hotel':[5, 120000], 'Noble Memorial Hotel':[4, 59000], 'Mirth Hotel':[4, 64000], 'Felicity Motel':[3, 29000], 'Renaissance Hotel':[3, 49000], 'Rainbow Hotel & Spa':[5, 154000]}

hotelsObjectList = []

for hotel in hotels_dict:
	hotelStar = hotels_dict[hotel][0]
	hotelPrice = hotels_dict[hotel][1]
	hotelItem = hotels(hotel, hotelStar, hotelPrice)
	hotelsObjectList.append(hotelItem)

sortedHotelsObjectList = sorted(hotelsObjectList, key=lambda object1: object1.price) 

tempItemPrice = sortedHotelsObjectList[0].price

i = 0

for item in sortedHotelsObjectList:
	if int(inputPrice) > item.price and int(inputPrice) < sortedHotelsObjectList[len(sortedHotelsObjectList)-1].price and i < 3:
		continue	
	elif int(inputPrice) >= sortedHotelsObjectList[len(sortedHotelsObjectList)-1].price:
		print('вариантов нет')
		break
	elif i >= 3:
		break
	else:
		item.showAll()
		i+=1


	