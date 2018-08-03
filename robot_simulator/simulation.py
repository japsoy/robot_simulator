from robot import Robot
from board import Board
from commands import Command
board = Board(5, 5)
robot = Robot(board, 0, 0, 'NORTH')
object_command = Command(robot)
with open('action.txt', 'r') as file_input:
    commands = file_input.read()
commands = commands.replace('\n', '-')

commands = commands.split('-')
for command in commands:
    if command:
        print command
        object_command.parse_command(command)
