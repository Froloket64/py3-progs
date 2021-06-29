import re
from random import randint


def genDates(amount, legit = True):
	dates = []
	for i in range(amount):
		if legit: 
			day = randint(0, 31)
			month = randint(0, 12)
			year = randint(1000, 2021)
		else:
			day = randint(0, 99)
			month = randint(0, 99)
			year = randint(0, 9999)

		dates.append(f'{day if day >= 10 else "0" + str(day)}.{month if month >= 10 else "0" + str(month)}.{year}')

	return dates


def filter(dates: list or tuple):
	regex = re.compile('([012]\d|3[01])\.(0\d|1[012])\.(1...|20[01].)')

	result = []
	for date in dates:
		if re.search(regex, date):
			result.append(date)
	
	return result


amount = int( input('How much dates to generate: ') )

dates = genDates(amount, False)

for date in filter(dates):
	print(date)