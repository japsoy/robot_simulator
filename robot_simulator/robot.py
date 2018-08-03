
class Robot:
    FACE_SET = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self, board, x, y, face):
        self.board = board
        self.x = x
        self.y = y
        self.face = face

    def __str__(self):
        return 'OUTPUT %s, %s (%s)' % (self.x, self.y, self.face)

    def change_face(self, command):
        for i, face in enumerate(self.FACE_SET):
            if self.face == face:
                if command == 'RIGHT':
                    if i + 1 >= len(self.FACE_SET):
                        new_face = self.FACE_SET[0]
                    else:
                        new_i = i + 1
                        new_face = self.FACE_SET[new_i]
                if command == 'LEFT':
                    new_i = i - 1
                    new_face = self.FACE_SET[new_i]
        self.face = new_face

    def move_position(self):
        values = 1
        axis = "x"

        if self.face == 'NORTH':
            axis = 'y'
        if self.face == 'SOUTH':
            axis = 'y'
            values = -1
        if self.face == 'EAST':
            axis = 'x'
        if self.face == 'WEST':
            axis = 'x'
            values = -1
        if self.validate_position(axis, values):
            if axis == 'y':
                self.y += values
            else:
                self.x += values

    def validate_position(self, axis, values):
        axis_value = self.x
        max_value = self.board.max_x
        if axis == 'y':
            axis_value = self.y
            max_value = self.board.max_y
        axis_value += values
        return axis_value > 0 and axis_value <= max_value
