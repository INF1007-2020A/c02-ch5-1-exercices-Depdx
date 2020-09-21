#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sousTotal = 0

	taxesRate = 15/100
	for article in data:
		sousTotal += article[INDEX_PRICE]*article[INDEX_QUANTITY]
	taxes = taxesRate * sousTotal
	total = sousTotal + taxes

	bill_data =[
		("SOUS TOTAL ", sousTotal),
		("TAXES      ", taxes),
		("TOTAL      ",total)
	]
	bill = name
	for bd in bill_data:
		bill += "\n" + f"{bd[0]}{bd[1]: >10.2f} $"

	#bill += "\n" + f"SOUS TOTAL {sousTotal: >10.2f} $"
	#bill += "\n" + f"TAXES      {taxes: >10.2f} $"
	#bill += "\n" + f"TOTAL      {total: >10.2f} $"


	return bill


def format_number(number, num_decimal_digits):
	whole_part = int(abs(number))
	decimal_part = abs(number)%1
	#nombre = [int(number),abs(number)%1]

	#formater partie decimal
	decimal_part_str = "." + format(str(int(round(decimal_part*10**num_decimal_digits))),"0<3")

	#formater partie entiere
	whole_part_str = ""

	while whole_part >= 1000:
		digits = whole_part % 1000
		digits_str = f" {digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part //= 1000

	whole_part_str = str(whole_part) + whole_part_str

	#concat les 2 partie
	if number < 0:
		whole_part_str = "-" + whole_part_str

	return whole_part_str + decimal_part_str



def get_triangle(num_rows):
	bordure= "+"
	triangleChart = "A"
	largeurTriangle = 2*num_rows+1
	brodure_row= bordure*(largeurTriangle+2)
	format = " ^" + str(largeurTriangle)
	triangle_str = brodure_row + "\n"
	for indexrow in range(num_rows):
		nbdechar = 1+2*indexrow
		lignedeChar= triangleChart*nbdechar
		triangle_str += f"{bordure}{lignedeChar:{format}}{bordure}\n"
	triangle_str+=brodure_row
	return triangle_str


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
