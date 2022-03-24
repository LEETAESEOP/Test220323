import time
import os
import math

board_text_list = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
board_col_num = len(board_text_list)

# 임의의 값
# display_text = "hello"
# display_text_length = len(display_text)



# 사용자 입력
display_text = ''
display_text_length = 0

while display_text_length <= 0:
    display_text = input(f'문구를 입력하세요 (최대 {board_col_num}자): ')
    display_text = display_text[0:min(len(display_text), board_col_num)]

    display_text_length = len(display_text)




# 왼쪽정렬
# board_text_list[0:display_text_length] = display_text

# 오른쪽정렬
# board_text_list[board_col_num-display_text_length:] = display_text

# 중앙정렬
begin_index = max(0, math.ceil((board_col_num - display_text_length) - (display_text_length * 0.5)))
board_text_list[begin_index:begin_index+display_text_length] = display_text


while True:
    os.system('cls')
    print(''.join(board_text_list))

    # 스왑하면서 전체가 한칸씩 이동
    for i in range(0, board_col_num-1):

        next_i = i+1

        val1 = board_text_list[i]
        val2 = board_text_list[next_i]

        # 스왑
        board_text_list[i] = val2
        board_text_list[next_i] = val1

    time.sleep(1)