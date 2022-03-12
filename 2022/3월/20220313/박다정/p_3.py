n = int(input())


def dfs(n):
    if n == 1:
        return ['  *  \n',
                ' * * \n',
                '*****\n']

    top_triangle = dfs(n // 2)
    top_triangle_bottom_length = len(top_triangle[-1][:-1]) // 2
    left_triangle = top_triangle[:]
    right_triangle = top_triangle[:]

    # 별 사이에 공백 추가
    for i in range(len(top_triangle)):
        space = ' ' * (top_triangle_bottom_length + 1)
        top_triangle[i] = space + top_triangle[i][:-1] + space + '\n'
        left_triangle[i] = left_triangle[i][:-1]

    for i in range(len(top_triangle)):
        top_triangle.append(left_triangle[i] + ' ' + right_triangle[i])

    return top_triangle


print(''.join(dfs(n // 3)))
