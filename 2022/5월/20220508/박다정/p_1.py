def highestValuePalindrome(s, n, k):
    s = list(s)
    changed_index = []
    if n == k:
        return '9' * n

    for i in range(n):
        if s[i] == s[n - i - 1]:
            continue

        if k == 0:
            return '-1'

        if s[i] > s[n - i - 1]:
            s[n - i - 1] = s[i]
        else:
            s[i] = s[n - i - 1]
        changed_index.append(i)
        k -= 1

    if k == 0:
        return ''.join(s)

    for i in range(n):
        if k == 0:
            return ''.join(s)

        if s[i] == '9' and s[n - i - 1] == '9':
            continue

        if i in changed_index:
            if k >= 1:
                k -= 1
                s[i] = '9'
                s[n - i - 1] = '9'
        else:
            if k >= 2:
                k -= 2
                s[i] = '9'
                s[n - i - 1] = '9'
    # 가운데 글자 하나가 최대가 아닐 때 12321
    if k > 0 and len(s) % 2 == 1:
        s[len(s) // 2] = '9'
    return ''.join(s)