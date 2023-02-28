dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
dict2 = {'0' :'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110',
         '7': '0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100',
         'D': '1101','E': '1110', 'F': '1111'}
# T = int(input())
N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
arr = list(set(arr))
num2 = ''

# 16진수 2진수로 바꾸기
for i in range(len(arr)):
    num = ''
    for j in arr[i]:
        num += dict2[j]
    arr[i] = num
# print(arr)
# 뒤부터 1이 나올 때까지 0 잘라주기
a = len(arr[0])
for i in range(len(arr)):
    for r in range(a - 1, -1, -1):
        if arr[i][r] == '0':
            arr[i] = arr[i][0:r]
        elif arr[i][r] == '1':
            break
    # print(len(arr[i]))
print(arr)

# 길이를 7의 배수로 만들기
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if len(arr[i]) > 0:
            if len(arr[i]) % 7 != 0:
                b = len(arr[i]) % 7
                arr[i] = arr[i][j+b:]
print(len(arr[i]))

# 7개씩 8개로 만들기 -> 실패,,,
mycode = []
for i in range(len(arr)):
    for j in range(0,len(arr[i])-1,7):
        mycode.append(arr[i][j:j+7])

print(mycode)

for i in range(len(mycode)-1, -1,-1):





