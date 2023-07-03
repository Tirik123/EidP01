def cluster_by_ingredience(recipes: dict[str, list[str]]) -> dict[str, list[str]]:
    new_dict = {}
    for meal, zutat in recipes.items():
        for zutaten in zutat:
            if zutaten not in new_dict.keys():
                new_dict[zutaten] = [meal]
            elif zutaten in new_dict.keys():
                new_dict[zutaten].append(meal)
    return new_dict



if __name__ == '__main__':
    recipess = { 'Pizza Margehrita': ['Mehl', 'Hefe', 'Tomaten', 'Käse'],
                'Pasta Napoli': ['Penne', 'Tomaten'],
                'Nudelauflauf': ['Penne', 'Käse', 'Eier', 'Sahne']
                }
    print(cluster_by_ingredience(recipess))