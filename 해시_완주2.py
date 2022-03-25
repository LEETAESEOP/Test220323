import collections

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["marina", "josipa", "nikola", "vinko"]


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer)[0])
    return list(answer.keys())[0]


a = solution(participant, completion)

print("%s 선수는 명단에 없으므로, 완주하지 않았습니다" %a)
