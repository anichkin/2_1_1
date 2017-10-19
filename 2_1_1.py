cook_book = {}
number = 0
quantity_2 = []
composition = []

def dishes(number): 
	with open('recipes.txt', encoding='utf-8') as f:
		for line in f:
			dish = line.strip().lower()
			cook_book[dish]=number
			number+=1
			quantity = int(f.readline())
			quantity_2.append(str(quantity)) 
			for i in range(0,quantity):
				f.readline()
			f.readline()
		return(cook_book)

dishes(number)

def compositions():
	with open('recipes.txt', encoding='utf-8') as f:
		for line in f:
			quantity = int(f.readline())
			for i in range(0,quantity):
				composition.append(f.readline().strip('\n'))
			f.readline()
		return(composition)

compositions()

first = 1
def chosen_compositions(name, first, person):
	for dish in cook_book:
		if dish == name:
			for m in range(int(cook_book.get(dish))):
				first+=int(quantity_2[m])
				second=first+int(quantity_2[m+1])	
			for i in range(first, second):
				composition[i].split('|')
				print('{} {} {}'.format(composition[i].split('|')[0], person*int(composition[i].split('|')[1]), composition[i].split('|')[2]))
	

			

def program():
	name = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
	person = int(input('Введите количество человек: '))
	first = 1
	for i in range(len(name)):
		chosen_compositions(name[i], first, person)
	program()

program()


