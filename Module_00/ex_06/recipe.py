def print_dict():
	for key in cookbook:
		print(key)

def print_recipe(recipe):
	print(recipe, end = ': ')
	for key in cookbook[recipe]['ingredients'] :
		print(key, end=', ')


if __name__ == "__main__":
	cookbook = {
		'Sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
					 'meal': 'lunch',
					 'prep_time': 10},
		'Cake': {'ingredients': ['flour', 'sugar', 'eggs'],
					 'meal': 'dessert',
					 'prep_time': 60},
		'Salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
					 'meal': 'lunch',
					 'prep_time': 15}
		}
	print_dict()
	print_recipe("Sandwich")


	