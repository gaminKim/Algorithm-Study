def comb(arr, n, m, index):
    if len(arr) == m:
        return [arr]
    if len(arr) > m:
        return []
    if index == n:
        return []
    
    result = []
    tmp = arr[:]
    arr.append(index)
    
    result += comb(arr, n, m, index+1)
    result += comb(tmp, n, m, index+1)

    return result

def get_chicken_house(towns):
    result = []

    for i in range(len(towns)):
        for j in range(len(towns)):
            if towns[i][j] == 2:
                result.append((i, j))
    return result

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def rotate_chicken_house(orders, chicken_houses, x, y):
    distance = 100000000000

    for i in range(len(orders)):
        chicken_x, chicken_y = chicken_houses[orders[i]]
        distance = min(distance, get_distance(x, y, chicken_x, chicken_y))

    return distance

def get_all_distance(chicken_house, towns, all_case):
    result = []

    for chicken in all_case:
        distance = 0

        for i in range(len(towns)):
            for j in range(len(towns)):
                if towns[i][j] == 1:
                    distance += rotate_chicken_house(chicken, chicken_house, i, j)
        result.append(distance)
    return result

def main(n, m, towns):
    chicken_house = get_chicken_house(towns)
    all_case = comb([], len(chicken_house), m, 0)
    result = get_all_distance(chicken_house, towns, all_case)
    result.sort()

    return min(result[:m])
if __name__ == '__main__':
    n, m = map(int, input().split())
    towns = [list(map(int, input().split())) for _ in range(n)]
    print(main(n, m, towns))