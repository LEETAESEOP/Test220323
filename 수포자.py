

def solution(answers):
    cnt = [0, 0, 0]
    ans = []
    supo1 = [1, 2, 3, 4, 5, 6]
    # supo1의 len = 6
    print(supo1[0%(len(supo1))])
    # supi[0] = 1
    # 0 % 6 = 0 이다. 따라서 supo1[0]= 1
    print(supo1[1%(len(supo1))])
    # supo[1] = 2
    # 1 % 6 = 1 이다. 따라서 supo2[1] = 2
    print(supo1[2%(len(supo1))])
    # supo[2] = 3
    print(supo1[3%(len(supo1))])
    print(supo1[4%(len(supo1))])
    print(supo1[5%(len(supo1))])
    print(supo1[6%(len(supo1))])
    print(supo1[7%(len(supo1))])
    
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # len 8
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # len 10

    for i in range(len(answers)) :
        # range 로 시작하는 for문은 i값이 0부터 시작한다.
        # supo의 리스트는 계속 반복해서 찍으므로 %를 사용한다.
        print("i값은:", i)
        if answers[i] == supo1[i%(len(supo1))] : cnt[0] += 1
        if answers[i] == supo2[i%(len(supo2))] : cnt[1] += 1
        if answers[i] == supo3[i%(len(supo3))] : cnt[2] += 1
    
    print("cnt:", cnt)

    for i in range(len(cnt)) :
        print("cnt의 i값은:", i)
        if cnt[i] == max(cnt) :
            ans.append(i + 1)
    return ans

a = solution([1,2,3,45])
print("a:", a)