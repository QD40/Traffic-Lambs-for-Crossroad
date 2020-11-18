import time
line = "-"*30
road1 = "Road 1: "
road2 = "Road 2: "
road3 = "Road 3: "
road4 = "Road 4: "
red = "Currently Acitve Light: Red"
yellow = "Currently Active Light: Yellow"
green = "Currently Active Light: Green"

def transition(yellow,line,road1,road2,road3,road4):
    print(line)
    print(road1, yellow)
    print(road2, yellow)
    print(road3, yellow)
    print(road4, yellow)
    timer = 3
    while timer > 0:
        print(line)
        print("Time Left: ", timer)
        timer -= 1
        time.sleep(1)


def road_1(red,green,road1,road2,road3,road4,line):
    print(line)
    print(road1, green)
    print(road2, red)
    print(road3, red)
    print(road4, red)
    timer = 10
    while timer > 0:
        print(line)
        print("Time Left: ", timer)
        timer -= 1
        time.sleep(1)

def road_2(red,green,road1,road2,road3,road4,line):
    print(line)
    print(road1, red)
    print(road2, green)
    print(road3, red)
    print(road4, red)
    timer = 10
    while timer > 0:
        print(line)
        print("Time Left: ", timer)
        timer -= 1
        time.sleep(1)

def road_3(red,green,road1,road2,road3,road4,line):
    print(line)
    print(road1, red)
    print(road2, red)
    print(road3, green)
    print(road4, red)
    timer = 10
    while timer > 0:
        print(line)
        print("Time Left: ", timer)
        timer -= 1
        time.sleep(1)

def road_4(red,green,road1,road2,road3,road4,line):
    print(line)
    print(road1, red)
    print(road2, red)
    print(road3, red)
    print(road4, green)
    timer = 10
    while timer > 0:
        print(line)
        print("Time Left: ", timer)
        timer -= 1
        time.sleep(1)

while True:
    road_1(red, green, road1, road2, road3, road4, line)
    transition(yellow, line, road1, road2, road3, road4)
    road_2(red, green, road1, road2, road3, road4, line)
    transition(yellow, line, road1, road2, road3, road4)
    road_3(red, green, road1, road2, road3, road4, line)
    transition(yellow, line, road1, road2, road3, road4)
    road_4(red, green, road1, road2, road3, road4, line)
    transition(yellow, line, road1, road2, road3, road4)


