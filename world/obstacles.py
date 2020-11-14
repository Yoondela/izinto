import random

obstacles = [(-63, -171), (-44, 168),(16, -169)]
occupied = []
y_change = False


# for i in range(10):
#     y = random.randint(-150, 150)
#     x = random.randint(-250, 250)
#     obstacles.append((y,x))


def is_position_blocked(x,y):
    pos = (x,y)
    for i in range(3):
        obstacle = obstacles[i]
        helper(obstacle)
    if pos in occupied:
        return True
    else:
        return False


def helper(obstacle):
    global occupied, y_change
    (x,y) = obstacle
    y_marker = y
  
    for i in range(6):
        for j in range(5):
            occupied.append((x,y))              
            
            if y_change:
                x = y_marker
                occupied.append((x,y))
                y_change = False
            x = x + 1
        y = y - 1
        y_change = True


def is_path_blocked(x1,y1,x2,y2):
    start = (x1,y1)
    end = (x2, y2)
    start_x = start[0]
    end_x = end[0]
    start_y = start[1]
    end_y = end[1]
    blocked = False
    if start_x <= end_x:
        for i in range(start_x, end_x+1):
            if start_y <= end_y:
                for j in range(start_y, end_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in occupied:
                        blocked = True

            elif start_y > end_y:
                for j in range(end_y, start_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in occupied:
                        blocked = True

            if start_x < end_x:
                start_x = start_x + 1
            elif start_x > end_x:
                start_x = start_x - 1

    elif start_x > end_x:
        for i in range(end_x, start_x+1):
            if start_y <= end_y:
                for j in range(start_y, end_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in occupied:
                        blocked = True

            elif start_y > end_y:
                for j in range(end_y, start_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in occupied:
                        blocked = True

            if start_x < end_x:
                start_x = start_x + 1
            elif start_x > end_x:
                start_x = start_x - 1
    return blocked


def get_obstacles():
    # start_obstacles = []
    end_obstacle = []
    for i in obstacles:
        end_obstacle.append(i)
        x = i[0] + 4
        y = i[1] - 4
        end_obstacle.append((x,y))
    return end_obstacle



print(get_obstacles())
print(is_position_blocked(-63, -171))
print(is_path_blocked(12,45,-166, -173))
print(occupied)