phone_book = ["119", "97674223", "5524421", "12352151", "161", "152121", "119521891"]
print(phone_book)

def solution(phone_book):
    
    # 1. 비교할 A선택 (폰북 전체길이)
        for i in range(len(phone_book)) :
           # 2. 비교할 B선택 (위의 폰북 A와 폰북의 i+1 번째를 비교)
            for j in range(i+1, len(phone_book)) :
                # 3. 서로가 서로의 접두어인지 확인한다.
# String1.startswith(String2)
# String1이 String2로 시작되는지 (String2가 String1의 접두어인지)를 찾아주는 기본 함수이고,
# 이 문제에서 사용하기 아주 적합한 함수이다.

                if phone_book[i].startswith(phone_book[j]):
                    return False
                if phone_book[j].startswith(phone_book[i]):
                    return False

        return True

print(solution(phone_book))
