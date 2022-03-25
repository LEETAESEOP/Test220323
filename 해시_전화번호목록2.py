phone_book = ["119", "97674223", "5524421", "12352151", "161", "152121", "119521891"]

def solution(phone_book):
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

# print(phone_book)
# print(phone_book[1:])
# print(list(zip(phone_book, phone_book[1:])))

# for p1, p2 in zip(phone_book, phone_book[1:]):
#     if p2.startswith(p1):
#         return False
#     return True


print(solution(phone_book))
