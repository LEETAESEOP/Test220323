

# 1,1,2,3,5,8,13,
# Fn = Fn-1 + Fn-2
def fiboForRecursive(n):
    if n < 2:
         return n # 0,1
    return fiboForRecursive(n-1) + fiboForRecursive(n-2)


# 1,1,2,3,5,8,13,
def fiboForLoop(n):
    if n < 2: 
        return n

    a, b = 0, 1
    for _ in range(n-1):
        # a, b = b, a + b # 아래 내용을 파이썬으로 표현

        # 현재 b의 값을 기억
        temp = b # fn-1
        b = a + b #fn = fn-2 + fn-1
        #a = fn-1 의 값이 되므로써 다음 반복에서 단계가 넘어가며 fn-2가됨
        a = temp 

    return b


def fiboForCacheLoop(n):
    if n < 2: return n

    # fiboCache = [0 for _ in range(n+1)]
    fiboCache = [0] * (n+1)
    fiboCache[1] = 1

    for i in range(2, n+1):
        fiboCache[i] = fiboCache[i-1] + fiboCache[i-2]

    return fiboCache[n]


def fiboForCacheRecursive(n):
    
    fiboCache = [-1] * (n+1)

    def fiboRecursive(n):

        if n < 2: return n

        # 캐시된 값이 있다면 반환
        if fiboCache[n] != -1:
            return fiboCache[n]

        # 결과를 캐시
        # fiboRecursive()를 재귀호출하며 이미 이전 결과는 캐시되어 있어서 빠르게 읽어옴
        fiboCache[n] = fiboRecursive(n-1) + fiboRecursive(n-2)

        return fiboCache[n]
    
    return fiboRecursive(n)


# for n in range(1,40):
#     print(f'{fiboForRecursive(n)} ', end='')

for n in range(1,10):
    print(f'{fiboForLoop(n)} ', end='')

# for n in range(1,10):
#     print(f'{fiboForCacheLoop(n)} ', end='')

# for n in range(1,10):
#     print(f'{fiboForCacheRecursive(n)} ', end='')

print()

# print(f'fibo: {fibo(5)}')

