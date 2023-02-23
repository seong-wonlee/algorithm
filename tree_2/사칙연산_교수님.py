def f(i):
    if tree[i] not in ['+', '/', '*', '-']:
        return tree[i]
    else:
        r1 = f(left[i]) # 왼쪽 서브트리의 연산결과
        r2 = f(right[i])    # 오른쪽 서브트리의 연산결과
    return result   # 연산 결과를 리턴