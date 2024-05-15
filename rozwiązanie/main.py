import random

# Description
# - positions printed to user are counted from 1 to 8 in respect to top-left corner of chessboard
# - user should provide also positions in respect to top-left corner of chessboard from 1 to 8

def generate_random_position():
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    return (x, y)

# returns True if position available and False if not
def check_position_available(map, position):
    return map[position[1]][position[0]] == ' '

def generate_map(k):
    map = [[' ' for x in range(8)] for y in range(8)]

    for i in range(k):
        kingPosition = generate_random_position()
        while(check_position_available(map, kingPosition) == False):
            kingPosition = generate_random_position()
        map[kingPosition[1]][kingPosition[0]] = 'K'

    pawnPosition = generate_random_position()
    while(check_position_available(map, pawnPosition) == False):
            pawnPosition = generate_random_position()
    map[pawnPosition[1]][pawnPosition[0]] = 'P'

    return map

def get_pawn_position(map):
    position = ()
    for [index, row] in enumerate(map):
        try:
            position = (row.index('P'), index)
            break
        except ValueError:
            continue

    return position

def print_map(map):
    edge = f'+{'-'*(8*4-1)}+\n'
    mapString = edge

    for row in map:
        mapString += f'| {' | '.join(row)} |\n{edge}'

    print(mapString)

def check_diagonals_for_king(map, pawnPosition):
    kingsThatCanCapture = []
    # go up left
    i = 0
    while (pawnPosition[1]-i) >= 0 and (pawnPosition[0]-i) >= 0:
        if map[pawnPosition[1]-i][pawnPosition[0]-i] == 'K':
            kingsThatCanCapture.append((pawnPosition[0]-i, pawnPosition[1]-i))
            break
        i += 1
    # go up right
    i=1
    while (pawnPosition[1]-i) >= 0 and (pawnPosition[0]+i) <= 7:
        if map[pawnPosition[1]-i][pawnPosition[0]+i] == 'K':
            kingsThatCanCapture.append((pawnPosition[0]+i, pawnPosition[1]-i))
            break
        i += 1
    # go down left
    i=1
    while (pawnPosition[1]+i) <= 7 and (pawnPosition[0]-i) >= 0:
        if map[pawnPosition[1]+i][pawnPosition[0]-i] == 'K':
            kingsThatCanCapture.append((pawnPosition[0]-i, pawnPosition[1]+i))
            break
        i += 1
    # go down right
    i=1
    while (pawnPosition[1]+i) <= 7 and (pawnPosition[0]+i) <= 7:
        if map[pawnPosition[1]+i][pawnPosition[0]+i] == 'K':
            kingsThatCanCapture.append((pawnPosition[0]+i, pawnPosition[1]+i))
            break
        i += 1

    return kingsThatCanCapture

def check_row_for_king(map, pawnPosition):
    kingsThatCanCapture = []
    # go left
    i = 0
    while pawnPosition[0]-i >= 0:
        if map[pawnPosition[1]][pawnPosition[0]-i] == 'K':
            kingsThatCanCapture.append((pawnPosition[0]-i, pawnPosition[1]))
            break
        i+=1
    # go right
    i = 0
    while pawnPosition[0]+i <= 7:
        if map[pawnPosition[1]][pawnPosition[0]+i] == 'K':
            kingsThatCanCapture.append((pawnPosition[0]+i, pawnPosition[1]))
            break
        i+=1

    return kingsThatCanCapture

def check_column_for_king(map, pawnPosition):
    kingsThatCanCapture = []
    # go up
    i = 0
    while pawnPosition[1]-i >= 0:
        if map[pawnPosition[1]-i][pawnPosition[0]] == 'K':
            kingsThatCanCapture.append((pawnPosition[0], pawnPosition[1]-i))
            break
        i+=1
    #go down
    i = 0
    while pawnPosition[1]+i <= 7:
        if map[pawnPosition[1]+i][pawnPosition[0]] == 'K':
            kingsThatCanCapture.append((pawnPosition[0], pawnPosition[1]+i))
            break
        i+=1

    return kingsThatCanCapture

def list_filter(element):
    return element != []

def check_for_capture(map, pawnPosition):
    kingsThatCanCapture = []
    # check row
    kingsThatCanCapture.append(check_row_for_king(map, pawnPosition))
    # check col
    kingsThatCanCapture.append(check_column_for_king(map, pawnPosition))
    # check diag
    kingsThatCanCapture.append(check_diagonals_for_king(map, pawnPosition))

    return list(sum(filter(list_filter, kingsThatCanCapture), []))

def is_capture_possible(kings):
    return len(kings) > 0

def print_capturing_kings_positions(kings):
    edge = f'+{'-'*8}+\n'
    capturingKingsString = edge

    for king in kings:
        capturingKingsString += f'| ({king[0]+1}, {king[1]+1}) |\n{edge}'

    print("\nKings that can capture positions: \n"+capturingKingsString)

def print_if_capture_is_possible(kings):
    print('\n--- Capture IS possible ---\n\n' if is_capture_possible(kings) else '\n--- Capture IS NOT possible ---\n\n')

def print_menu():
    print('\n\nMENU:\n1. Generate new pawn position respecting current kings positions\n2. Delete king on specified position\n')

def main(k, map):
    print_map(map)
    
    pawnPosition = get_pawn_position(map)
    print(f'Pawn position: ({pawnPosition[0]+1}, {pawnPosition[1]+1})\n')
    
    kings = check_for_capture(map, pawnPosition)
    print_if_capture_is_possible(kings)
    if is_capture_possible(kings):
        print_capturing_kings_positions(kings)
    
    print_menu()
    selectedOption = int(input("Select option: "))
    while selectedOption not in [1, 2]:
        print("No such option. Try again.\n")
        selectedOption = int(input("Select option: "))

    match selectedOption:
        case 1:
            #generate new pawn position
            newPawnPosition = generate_random_position()
            while newPawnPosition == pawnPosition or check_position_available(map, newPawnPosition) != True:
                newPawnPosition = generate_random_position()

            map[pawnPosition[1]][pawnPosition[0]] = ' '
            map[newPawnPosition[1]][newPawnPosition[0]] = 'P'

            main(k, map)
        case 2:
            #delete specified king
            print("Provide king position to delete:\n")
            x = int(input("x: "))
            y = int(input("y: "))  
            while map[y-1][x-1] is not 'K' or map[y-1][x-1] == 'P' or x>8 or y>8:
                print("There is no king at specified position. Try again.\n")
                x = int(input("x: "))
                y = int(input("y: ")) 

            map[y-1][x-1] = ' '

            main(k, map)

if __name__ == '__main__':
    k = int(input("How many kings should be placed on chessboard?: "))
    if k > 5:
        print("Number of kings can't be greater than 5\n")
        main()
    print('\n')
    
    map = generate_map(k)
    main(k, map)