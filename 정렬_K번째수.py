# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수는?
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands


def solution(array, commands):
    answer = []

    for i in commands:

        ary = array[i[0]-1: i[1]]    # 문제에서 주어진 크기만큼 자르기
        # for문 commands의 첫번째 i가 돌때, i = [2,5,1] 이다. 
        # [2,5,1]에서 i[0]-1 == 1 이고,
        # [2,5,1]에서 i[1] == 5 이다.
        # 그러면, ary = array[1:5]
        # ary = array[5,2,6,3,7]
        ary.sort()    # sort 함수로 정렬
        # ary = [2,3,5,6,7]
        answer.append(ary[i[2]-1])    # k 번째 값 집어넣기
        # .append()로 요소추가 가능.

        # i[2] = 1 이었고, << i[2] = k번째 의미 >>
        # ary[k] 로 하면 ary[1]이 되므로, ary[0]값을 얻기 위해 -1을 하는 것이다.
        # ary[i[2]-1] = ary[0] = 2
        # 따라서 answer = [2]
    return answer
                                 # 문제상 i,j,k의 각 원소를 가진 commands
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 1], [1, 4, 4], [1, 7, 7]]))

