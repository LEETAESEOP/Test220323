
tile_map = [
    ['o','x','o','x','x','x','x','o','F'],
    ['o','o','o','x','x','o','o','o','x'],
    ['o','x','o','x','o','o','o','x','x'],
    ['o','o','o','o','o','o','o','o','o'],
    ['x','o','x','x','x','x','x','o','x'],
    ['o','o','o','o','x','o','o','o','o'],
    ['x','o','x','o','o','o','x','o','x'],
    ['o','o','o','o','x','o','o','o','x'],
    ['S','x','x','o','o','x','x','o','x'],
]

MAX_COL = len(tile_map[0])
MAX_ROW = len(tile_map)
OFFSET_RIGHT = (0,1)
OFFSET_LEFT = (0,-1)
OFFSET_TOP = (1,0)
OFFSET_DOWN = (-1,0)
OFFSETS = [OFFSET_RIGHT,OFFSET_LEFT,OFFSET_TOP,OFFSET_DOWN]

start_tile = (8,0)
finish_tile = (0,8)





class TileNode:

    parent = None
    position:tuple[int] = None

    def __init__(self, position:tuple, parent = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, __o) -> bool:
        return self.position == __o.position

    # def equalPosition(self, node) -> bool:
    #     return self.position == node.position

    # def calculationCost():
    #     pass


# 각 노드의 f,g,h 값을 파악해서 비용에 따른 길찾기
# g (현재 노드에서 출발 지점까지의 총 비용, 각노드의 이동방향에 따른 고정된 비용이 누적됨, 대각선이동이 가능할땐 피타고라스정의를 사용해서 대각선의 비용을 정의)
# h (Heuristic 휴리스틱, 현재 노드에서 목적지까지의 추정거리, 맨하튼거리 사용)
# f = g + h (총비용, 이 비용이 낮은것을 우선순위로 파악해 이동시 가장 낮은 비용을 들여 목적지에 도달 할 수 있는지를 파악)
def pathFinding(map_matrix:tuple[tuple[int]], start_pos:tuple[int], finish_pos:tuple[int]) -> list[tuple[int]]:

    open_list:list[TileNode] = []
    close_list:list[TileNode] = []

    # 찾은 경로가 담김
    path:list[tuple[int]] = []
    
    # 길파악 시작
    # 처음에 시작위치의 노드를 넣고 시작
    open_list.append(TileNode(start_pos))

    # open_list가 비어있을때까지 반복
    while open_list:

        current_index = 0
        current_node = open_list[current_index]

        # open_list 중에 가장 낮은 f값을 가진 노드를 가져옴
        # 주변노드를 파악해볼때 사용될 현재노드를 파악, f 값이 낮을수록 최단거리일 가능성이 높아서임
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_index = index
                current_node = item

        # open_list에서는 제외, close_list에 넣어둠
        # 이미 파악이 끝난 노드로 다시 확인되지 않도록 open_list에서 제외하고 close_list에 넣어둠
        open_list.pop(current_index)
        close_list.append(current_node)


        # 현재 노드가 도착지인지 파악
        # 부모 노드를 역으로 따라서 추적하면 이동가능한 경로가 나옴 (트리구조)
        if current_node.position == finish_pos:

            # 현재 노드를 시작으로 부모노드를 추적해서 위치를 모아 경로를 구성
            path.append(current_node.position)
            parent_node: TileNode = current_node.parent
            
            # == 는 내부 __eq__ 를 사용하기에 is를 통해서 형을 비교
            while parent_node is not None:
                path.append(parent_node.position)

                # 해당 노드의 부모노드를 역으로 추적
                parent_node = parent_node.parent

            # 역으로 추적한거라 반대로 뒤집어주면 시작부터 순서대로 정렬됨
            path.reverse()
            return path



        # 현재노드 중심으로 이동가능한 방향의 오프셋을 모두 파악
        for offset in OFFSETS:

            offset_cost = 10
            target_pos_y: int = current_node.position[0] + offset[0]
            target_pos_x: int = current_node.position[1] + offset[1]
            

            # 유효한 범위내에 좌표인지 확인
            if target_pos_x > MAX_COL - 1 or target_pos_x < 0 or target_pos_y > MAX_ROW - 1 or target_pos_y < 0:
                continue

            # 이동이 가능한 위치인지 파악
            tile_val = map_matrix[target_pos_y][target_pos_x]
            if tile_val == 'x':
                continue

            # close_list 에 포함되어있는 노드면 무시 및 다음 위치 확인 (이미 파악이 완료되었거나 파악중이거나)
            # 클래스내에 __eq__ 메소드의 구현내용으로 비교
            target_node = TileNode((target_pos_y, target_pos_x), current_node)
            if target_node in close_list:
                continue

            # if len([close_node for close_node in close_list 
            #     if target_node.position == close_node.position
            #     ]) > 0:

            #     continue
            
            # f,g,h 값 업데이트
            # 시작위치에서 누적되는 비용 (현재노드까지 누적된 g 에 해당 방향의 비용을 증가, 가로,세로 10, 대각선 이동은 불허)
            target_node.g = current_node.g + offset_cost
            # 현재위치에서 목적지까지 장애물을 무시한 최단거리 비용
            # 맨하튼 거리 사용 ( 거리 = abs(현재.y - 목적지.y) + abs(현재.x - 목적지.x) )
            target_node.h = abs(target_pos_y - finish_pos[0]) + abs(target_pos_x - finish_pos[1])
            # 총비용 (g + h)
            target_node.f = target_node.g + target_node.h

            # open_list 에 포함되어 있고 g값이 더 큰 노드면 무시 및 다음 위치를 확인 
            # 동일한 탐색가능 위치지만 작은 비용의 노드를 사용 (비교 위치에 따라서 누적되는 이동비용이 다름)
            # TODO open_list 에 중복되는 노드지만 현재 노드의 비용이 적다면 open_list에 들어있는 노드의 내용을 교체한다??
            if len([open_node for open_node in open_list 
                if target_node == open_node and target_node.g > open_node.g
                ]) > 0:

                continue

            # 탐색이 가능한 open_list에 추가해두고 다음 탐색시 참조
            open_list.append(target_node)

    return path

def displayMap(path: tuple[tuple:[int]] = ()):

    row = 0
    col = 0

    # 더이상 나열이 불가한 최소 단위의 항목을 하나씩 가져옴
    for datas in tile_map:
        # 한번 반복에 최대 9개까지 출력
        for data in datas:
            # 최대 9번 반복
            # print(f'{row,col}', end=',')
            # print(data, end=' ')

            # 해당 위치가 경로에 포함이라면 표시
            pos = (row, col)
            if pos == start_tile or pos == finish_tile:
                print(data, end=' ')
            elif pos in path:
                print('◼︎', end=' ')
            else:
                print(data, end=' ')

            col += 1

        # 줄내림
        print()
        row += 1
        col = 0

# display_map()
# print()

find_path = pathFinding(map_matrix=tile_map, start_pos= start_tile, finish_pos = finish_tile)
# print(find_path)
displayMap(find_path)




