import usbrelay_py
import time

count = usbrelay_py.board_count()
print("Count: ",count)

boards = usbrelay_py.board_details()
print("Boards: ",boards)

def activate_relay():

    for board in boards:
        print("Board: ",board)
        relay = 1
        while(relay < board[1]+1):
            result = usbrelay_py.board_control(board[0],relay,1)
            print("Result: ",result)
            relay += 1


def deactivate_relay():

    for board in boards:
        print("Board: ",board)
        relay = 1
        while(relay < board[1]+1):
            result = usbrelay_py.board_control(board[0],relay,0)
            print("Result: ",result)
            relay += 1