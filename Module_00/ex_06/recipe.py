import sys

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

def print_dict():
	global cookbook
	for key in cookbook:
		print(key)

def print_recipe(recipe):
	global cookbook
	print(recipe, end = ': ')
	print(', '.join(cookbook[recipe]['ingredients']))

def del_recipe(recipe):
	global cookbook
	cookbook.pop(recipe)



def add_recipe():
	global cookbook
	recipe_name = input ("Enter a name:\n")
	print("Enter ingredients:")
	ingredients = sys.stdin.readlines()
	meal = input ("Enter a meal type:\n")
	prep_time = input ("Enter a preparation time:\n")
	new_line = {recipe_name: {'ingredients': [f for f in ingredients],
                				'meal': meal,
                				'prep_time': prep_time}
                }
	cookbook.update(new_line)
	print_dict()

	
	


if __name__ == "__main__":
	print_dict()
	# print_recipe("Sandwich")
	add_recipe()
	del_recipe("chips")

	print_dict()

	