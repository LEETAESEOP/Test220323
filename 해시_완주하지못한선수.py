
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["marina", "josipa", "nikola", "vinko"]

print(len(participant))
print(len(completion))

def solution(participant, completion):

    #두 리스트를 소팅함.

    participant.sort()
    completion.sort()

    # 2. completion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]
    return(participant[len(participant)-1])

a = solution(participant, completion)

print("%s 선수는 명단에 없으므로, 완주하지 않았습니다" %a)
