cook_book = {}

with open('recipes.txt', 'r') as f:
    while True:
        name = f.readline().strip()
        if name == '':
            break
        ingredients_count = int(f.readline().strip())

        ingredient_list = []
        for i in range(ingredients_count):
            ingredient = f.readline().strip()

            ingredient_name, quantity, measure = ingredient.split(' | ')

            dictionary = {
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            }

            ingredient_list.append(dictionary)

        cook_book[name] = ingredient_list

        f.readline()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        # print(ingredients)
        for ing in ingredients:
            quantity = ing['quantity'] * person_count

            result[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': quantity}

    return result


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
