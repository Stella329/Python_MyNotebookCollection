from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()  ## method
        self.head = self.segment_list[0]


    # create segment
    def add_segment(self,position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)

    def create_snake(self):
        for position in START_POSITION: ## 3 locations = 3 segments
            self.add_segment(position)

    def extend_snake(self):
        ## add a new segment to the snake body
        last_position = self.segment_list[-1].position()
            ## turtle.position() 返回海龟当前的坐标 (x,y)
        self.add_segment(last_position)


    def move(self):
        for body_num in range(len(self.segment_list) - 1, 0, -1):  ## body 2
            move_to_x = self.segment_list[body_num - 1].xcor()
            move_to_y = self.segment_list[body_num - 1].ycor()
            self.segment_list[body_num].goto(move_to_x, move_to_y)  ## body 3 moves

        self.segment_list[0].forward(DISTANCE)

    def up(self):
        ## turtle.setheading(xx): east-0, north-90, west-180,south-270
        if self.head.heading() != 270:
            self.segment_list[0].setheading(90)
    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.segment_list[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.segment_list[0].setheading(0)


    def tail_collision(self):
        # METHOD 1: 列举所有可能性 (my)
        for segment in range(len(self.segment_list)-1,1,-1):
            head_coor = self.head.position()
            body_coor = self.segment_list[segment-1].position()
            if abs(head_coor[0] - body_coor[0]) <1 and abs(head_coor[1] - body_coor[1]) ==0:
                return True
            elif abs(head_coor[0] - body_coor[0]) ==0 and abs(head_coor[1] - body_coor[1]) <1:
                return True

        ## METHOD 2: using .distance() and slicing 有个问题：如果body立刻转去临近行（i.e. 第二行），也会game_over
        # for segment in self.segment_list[1:]:
        #     if self.head.distance(segment) < 10:
        #         return True



