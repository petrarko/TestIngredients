


def calculate_amount_to_clean(recipes: set):
    counter = 1
    recipes_used = []
    for recipe in recipes:
        for recipe_used in recipes_used:
            if not (recipe.issubset(recipe_used) or recipe_used.issubset(recipe)):
                counter += 1
                break
        recipes_used.append(recipe)
    return counter


def pop_line(input_string, is_console):
    if is_console:
        return None, input()
    return "\n".join(input_string.split("\n")[1:]), input_string.split("\n")[0]


def parse_input(input_string):
    is_console = True if input_string is None else False
    input_string, main_args = pop_line(input_string, is_console)
    amount_of_recipes = int(main_args.split(' ')[0])  # ignore amount of components
    recipes = []
    for _ in range(int(amount_of_recipes)):
        input_string, input_line = pop_line(input_string, is_console)
        recipe = set(input_line.split(' ')[1:])  # ignore amount of components
        recipes.append(recipe)
    return recipes


if __name__ == '__main__':
    action_list = parse_input(None)
    print(calculate_amount_to_clean(action_list))
