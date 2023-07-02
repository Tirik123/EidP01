def count_folds(width: int, height: int) -> int:
    iter = 0
    while width != 0 and height != 0:
        if width > height:
            iter += 1
            width = width // 2
        elif width < height:
            iter += 1
            height = height // 2
        elif width == height:
            iter += 1
            width = width // 2
    return iter
    








if __name__ == '__main__':
    print(count_folds(2, 1))
    #print(1//2)