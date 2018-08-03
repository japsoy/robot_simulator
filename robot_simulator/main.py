from robot import Robot
from board import Board
from commands import Command

board = Board(5, 5)
robot = Robot(board, 0, 0, 'NORTH')
obj_command = Command(robot)

while True:
    command = raw_input("Input Command (MOVE, LEFT, RIGHT, REPORT)")
    if not command:
        break
    obj_command.parse_command(command)
