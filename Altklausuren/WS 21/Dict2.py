def cluster_by_points(points: dict[str, int]) -> dict[int, str]:
    new_dict = {}
    for name, note in points.items():
        if note not in new_dict:
            round_note = (note // 10) * 10
            if round_note in new_dict:
                new_dict[round_note] += [name]
            else:
                new_dict[round_note] = [name]
    return new_dict




if __name__ == '__main__':
    print(cluster_by_points(points = {"Line": 9, "Daniel": 12, "Charlotte": 15, "Frank": 30}))