import usbrelay_py
import time

count = usbrelay_py.board_count()
print("Count: ",count)

boards = usbrelay_py.board_details()
print("Boards: ",boards)

def activate_relay():
    usbrelay_py.board_control(boards[0][0], 1, 1)


def deactivate_relay():
    usbrelay_py.board_control(boards[0][0], 1, 0)



