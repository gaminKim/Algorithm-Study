def get_swap_count(arr):
    count = 0
    indexs = {}

    for i in range(len(arr)):
        indexs[arr[i]] = i

    tmp = arr[:]
    arr.sort()

    for i in range(len(tmp)):
        if tmp[i] != arr[i]:
            count += 1
            j = indexs[arr[i]]
            indexs[tmp[i]] = indexs[arr[i]]
            tmp[i], tmp[j] = arr[i], tmp[i]

    return count


def lilysHomework(arr):
    # Write your code here
    reverse_arr = list(reversed(arr))
    return min(get_swap_count(arr), get_swap_count(reverse_arr))
