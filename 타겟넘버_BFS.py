# BFS를 이용한 풀이


def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        print("num", num)
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
            print("tmp:", tmp)
        leaves = tmp
        print("leaves:", leaves)
        
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer


print("answer:", solution([5, 2, 1, 1], 3))


# numbers의 숫자를 더하거나 뺀 경우를 수평적으로 추가해준다.
# 결국 leaves리스트에 모든 계산 결과가 담기게 된다. 이후 target값과 비교해서 결과 출력.

