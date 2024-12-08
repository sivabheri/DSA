def analyze_sales(grocery_list):

	n = len(grocery_list)

	max_total = 0

	max_item = None

	avg_price = 0

	total = 0

	for item, quant, price in grocery_list:

		total += quant*price 

		if total > max_total:
			max_item = item
			max_total = total
	avg_price = max_total/(n+1)

	return max_item,max_total,round(avg_price,2)


# Example usage
grocery_list = [
    ("Apple", 30, 5),
    ("Banana", 50, 4),
    ("Orange", 20, 8),
    ("Apple", 10, 10)
]

result = analyze_sales(grocery_list)
print("Higher selling item:", result[0])
print("Total selling item:", result[1])
print("Average selling item:", result[2])
