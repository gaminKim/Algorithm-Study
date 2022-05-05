def biggerIsGreater(w):
    # Write your code here
    w = list(w)
    start = 0

    for j in range(len(w) - 1, 0, -1):
        if w[j] > w[j - 1]:
            start = j - 1
            break

    order = []

    for j in range(len(w) - 1, start, -1):
        if w[start] < w[j]:
            order.append([w[j], j])

    order.sort()
    if len(order) > 0:
        _, end = order[0]
        tmp = w[start]
        w[start] = w[end]
        w[end] = tmp

        new_order = w[start + 1:]
        new_order.sort()
        return ''.join(w[:start + 1] + new_order)

    return 'no answer'
