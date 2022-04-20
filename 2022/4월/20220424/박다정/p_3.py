import sys

input = sys.stdin.readline
n = int(input().rstrip())
bulbs = list(input().rstrip())
answer = input().rstrip()
INF = sys.maxsize


def is_answer(bulbs):
    tmp = ''.join(bulbs)
    return tmp == answer


def change_bulbs(start, bulbs_arr):
    count = 0

    for i in range(start, n):

        if i == 0:
            bulbs_arr[i] = '0' if bulbs_arr[i] == '1' else '1'
            bulbs_arr[i + 1] = '0' if bulbs_arr[i + 1] == '1' else '1'
            count += 1

        elif i == n - 1:
            if bulbs_arr[i - 1] != answer[i - 1]:
                bulbs_arr[i] = '0' if bulbs_arr[i] == '1' else '1'
                bulbs_arr[i - 1] = '0' if bulbs_arr[i - 1] == '1' else '1'
                count += 1

        else:
            if bulbs_arr[i - 1] != answer[i - 1]:
                bulbs_arr[i] = '0' if bulbs_arr[i] == '1' else '1'
                bulbs_arr[i - 1] = '0' if bulbs_arr[i - 1] == '1' else '1'
                bulbs_arr[i + 1] = '0' if bulbs_arr[i + 1] == '1' else '1'
                count += 1

    if is_answer(bulbs_arr):
        return count
    return INF


def main():
    result = min(change_bulbs(0, bulbs[:]), change_bulbs(1, bulbs[:]))
    if result == INF:
        print(-1)
    else:
        print(result)


if __name__ == '__main__':
    main()
