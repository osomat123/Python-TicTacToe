# write your code here
cells = '_________'
state = [[cells[i],cells[i+1],cells[i+2]] for i in range(len(cells)) if i%3 == 0]
players = ['X','O']
winner = []
move_count = 0

def print_state():
    global state
    print('---------')
    for row in state:
        print('|', end=' ')
        for ele in row:
            if ele == '_':
                print(' ',end=' ')
                continue
            print(ele, end=' ')
        print('|')
    print('---------')

def is_impossible():
    global state

    X_count = 0
    O_count = 0

    # Check if impossible
    for cell in cells:
        if cell == 'X':
            X_count += 1
        elif cell == 'O':
            O_count += 1

    if abs(X_count - O_count) >= 2:
        return True

    return False

def find_winner(winner):
    global state

    if state[0][0] == state[0][1] and state[0][1] == state[0][2]:
        winner.append(state[0][0])

    if state[1][0] == state[1][1] and state[1][1] == state[1][2]:
        winner.append(state[1][0])

    if state[2][0] == state[2][1] and state[2][1] == state[2][2]:
        winner.append(state[2][0])

    if state[0][0] == state[1][0] and state[1][0] == state[2][0]:
        winner.append(state[0][0])

    if state[0][1] == state[1][1] and state[1][1] == state[2][1]:
        winner.append(state[0][1])

    if state[0][2] == state[1][2] and state[1][2] == state[2][2]:
        winner.append(state[0][2])

    if state[0][0] == state[1][1] and state[1][1] == state[2][2]:
        winner.append(state[0][0])

    if state[2][0] == state[1][1] and state[1][1] == state[0][2]:
        winner.append(state[2][0])


def check_status():
    global state
    global winner

    winner = []
    find_winner(winner)

    #impossible = is_impossible()
    empty = is_empty()

    #if impossible == True or len(winner) > 1:
    #   print("Impossible")

    if len(winner) == 1 and winner[0] != '_':
        return 1

    elif empty == True:
        return 0
        print("Game not finished")

    elif empty == False:
        return -1

def is_empty():
    global state

    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                return True

    return False

def get_input():
    global state

    move = [int(i) for i in input("Enter the coordinates: ").split(maxsplit=1) if i.isdigit()]

    if len(move) == 2:
        x = 3 - move[1]
        y = move[0] - 1

        if x in range(3) and y in range(3):
            if state[x][y] == '_':
                return (x,y)
            else:
                return -3

        else:
            return -1

    elif len(move) < 2:
        return -2

def add_to_state(coords):
    global move_count
    global state
    global players

    x = coords[0]
    y = coords[1]

    state[x][y] = players[move_count % 2]

print_state()
while True:

    coords = get_input()

    if coords == -1:
        print("Coordinates should be from 1 to 3!")
        continue

    elif coords == -2:
        print("You should enter numbers!")
        continue

    elif coords == -3:
        print("This cell is occupied! Choose another one!")
        continue

    add_to_state(coords)
    move_count += 1

    print_state()
    status = check_status()

    if status == 1:
        print(winner[0], "wins")
        break

    elif status == -1:
        print("Draw")
        break







