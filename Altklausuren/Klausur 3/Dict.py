def cluster_by_ingredience(recipes: dict[str, list[str]]) -> dict[str, list[str]]:
    new_dict = {}
    for meal, ingredient in recipes.items():
        for ingredients in ingredient:
            if ingredients not in new_dict.keys():
                new_dict[ingredients] = [meal]
            elif ingredients in new_dict.keys():
                new_dict[ingredients].append(meal) 
    return new_dict


if __name__ == '__main__':
    recipess = { 'Pizza Margehrita': ['Mehl', 'Hefe', 'Tomaten', 'Käse'],
                'Pasta Napoli': ['Penne', 'Tomaten'],
                'Nudelauflauf': ['Penne', 'Käse', 'Eier', 'Sahne']
                }
    print(cluster_by_ingredience(recipess))