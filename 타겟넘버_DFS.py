#DFS 풀이
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += DFS(numbers, target, depth+1)
        print(answer)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        print(answer)
        return answer

if __name__ == "__main__":

    print("answer:", solution([5, 2, 1, 1], 3))

# BFS가 수평적으로 더해 한꺼번에 모든 결과값을 얻었다면, DFS를 이용할 땐 하나씩 비교한다
# depth 변수 값을 통해 탐색 중인 트리의 깊이를 알 수 있다.
# 트리 끝에 도착했다면, number값을 모두 더한 값을 비교한다.