import os

current = os.getcwd()
file_name = 'cook_book.txt'

full_path = os.path.join(current, file_name)

cook_book = {}
with open (full_path, 'rt', encoding='utf8') as file:
    for l in file:
        recipe = l.strip()
        cook_book[recipe] = []
        count_ingridients = file.readline()
        for i in range(int(count_ingridients)):
            ingr = file.readline()
            ingridient_name, quantity, measure = ingr.strip().split(' | ') 
            cook_book[recipe].append({'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure})
        blank_string = file.readline()
        

def get_shop_list_by_dishes(dishes, person_count):
    get_shop_list = {}
    for dish in dishes:
        print(dish)
        for n in cook_book[dish]:
            get_shop_list[n['ingridient_name']] = {'measure': n['measure'], 'quantity': int(n['quantity']) * person_count}
    print(get_shop_list)

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
        




