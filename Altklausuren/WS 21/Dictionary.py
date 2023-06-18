def cluster_by_grade(points: dict[str, int]) -> dict[int, list[str]]:
    copy_dict = points
    new_dict = {}
    new_dict_2 = {}
    points_list = []
    for integer in points.values():
        if integer not in new_dict:
            integer = integer / 10
            integer = int(integer)
            integer = integer * 10
            new_dict[integer] = set()
        for name, point in points.items():
            if point in new_dict:
                new_dict[integer] = name
        for nami, inti in points.items():
            inti = inti / 10
            inti = int(inti)
            inti = inti * 10
            new_dict_2[nami] = inti
    '''print(new_dict_2)'''
    return new_dict






if __name__ == '__main__':
    points = {"Paul": 15, "Frank": 44, "Tim": 20, "Anna": 29}
    print(cluster_by_grade(points))
