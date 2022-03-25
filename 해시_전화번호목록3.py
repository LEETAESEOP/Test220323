
# phone_book = ["119", "976", "1195","118"]

# print(phone_book)
# print(phone_book[1:])
# print(" ")
# print(list(zip(phone_book, phone_book[1:])))

# def solution(phone_book):
#     phone_book.sort()
#     print(phone_book)

#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         print("p1:", p1)
#         print("p2:", p2)
#         print(" ")
#         if p2.startswith(p1):
#             return False
#     return True


# print(solution(phone_book))

def solution(phone_book): # 1. Hash map을 만든다 
    hash_map = {} 
    for phone_number in phone_book:
        hash_map[phone_number] = 1 
    # 2. 접두어가 Hash map에 존재하는지 찾는다 
    for phone_number in phone_book: 
        jubdoo = "" 
        for number in phone_number:
            # print(number) 
            jubdoo += number
            print(jubdoo) 
    # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number: 
                return False 
    return True 
print(solution(["67", "12", "6789"]))