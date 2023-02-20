# 첫번째 풀이
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(M):
        lst.append(lst.pop(0))
    print(f'#{tc} {lst[0]}')


# 두번째 풀이
# 마지막 원소 뒤에 새로운 원소 삽입
def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data


# 가장 앞에 있는 원소 삭제
def dequeue():
    global front
    front += 1
    return queue[front]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split())) + [0] * M
    # 인덱스 제일 앞 0의 앞
    front = -1
    # 인덱스 제일 뒤
    rear = N - 1

    for _ in range(M):
        enqueue(dequeue())

    print(f'#{test_case} {dequeue()}')



