def cluster_by_grade(points: dict[str, int]) -> dict[int, list[str]]:
    result_help = {}
    result = {}
    for name, grade in points.items():
        grade = grade / 10
        grade = int(grade) * 10
        result_help[name] = grade
    for namez, gradez in result_help.items():
        if gradez not in result.keys():
            result[gradez] = [namez]
        elif gradez in result.keys():
            result[gradez].append(namez)
    return result



if __name__ == '__main__':
    points = {"Line": 9, "Daniel": 12, "Charlotte": 15, "Frank": 30}
    print(cluster_by_grade(points))

