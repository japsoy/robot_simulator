from robot import Robot
from board import Board


class Command:
    def __init__(self, robot):
        self.robot = robot

    def parse_command(self, commands):
        REPORT = 'REPORT'
        DIRECTION = ['LEFT', 'RIGHT']
        MOVE = 'MOVE'
        COMMAND_LIST = ['REPORT', 'MOVE']
        COMMAND_LIST = COMMAND_LIST + DIRECTION
        commands = commands.upper()

        if 'PLACE' in commands:
            place_str_list = commands.split(' ')
            location_list = place_str_list[1].split(',')
            try:
                coords_x = int(location_list[0])
                coords_y = int(location_list[1])
                if (
                    coords_x < 5 and coords_y < 5 and
                    coords_x >= 0 and coords_y >= 0 and
                    location_list[2] in self.robot.FACE_SET
                ):
                    self.robot = Robot(Board(5, 5), coords_x, coords_y, location_list[2])
                else:
                    print "INVALID COMMAND"
            except ValueError:
                print "INVALID COMMAND"

        else:
            if commands in COMMAND_LIST:
                if commands in DIRECTION:
                    self.robot.change_face(commands)
                if commands == REPORT:
                    print str(self.robot)
                if commands == MOVE:
                    self.robot.move_position()
            else:
                print "INVALID COMMAND"
