"""EX14 Robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while True:
        robot.set_wheels_speed(10)
        if 0 in robot.get_line_sensors():
            robot.set_wheels_speed(30)
            robot.sleep(1)
            robot.set_wheels_speed(0)
            robot.done()
            break
        robot.sleep(1)


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    counter = 0
    big_counter = 0
    drive_to_start(robot)
    for i in range(300):
        if robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
            robot.set_wheels_speed(100)
            robot.sleep(0.05)
            counter = 0
        elif sum(robot.get_left_line_sensors()) < sum(robot.get_right_line_sensors()) and counter != 1:
            robot.set_right_wheel_speed(70)
            robot.set_left_wheel_speed(100)
            robot.sleep(0.03)
            robot.set_wheels_speed(0)
            robot.sleep(0.01)
        elif sum(robot.get_left_line_sensors()) > sum(robot.get_right_line_sensors()):
            robot.set_left_wheel_speed(70)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.03)
            robot.set_wheels_speed(0)
            robot.sleep(0.01)
        elif counter == 1:
            robot.set_right_wheel_speed(80)
            robot.set_left_wheel_speed(-80)
            robot.sleep(0.35)
            counter += 1
            big_counter += 1
        elif counter == 2 or big_counter == 2:
            robot.set_right_wheel_speed(80)
            robot.set_left_wheel_speed(-80)
            robot.sleep(0.15)
            robot.done()
            break
        elif sum(robot.get_line_sensors()) == 6144 and big_counter != 2:
            robot.set_right_wheel_speed(80)
            robot.set_left_wheel_speed(-80)
            robot.sleep(0.15)
            counter += 1


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move.
    """
    counter = 0
    big_counter = 0
    drive_to_start(robot)
    for i in range(5000):
        if robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
            robot.set_wheels_speed(70)
            robot.sleep(0.05)
            counter = 0
        elif sum(robot.get_left_line_sensors()) < sum(robot.get_right_line_sensors()) and counter != 1:
            robot.set_right_wheel_speed(50)
            robot.set_left_wheel_speed(100)
            robot.sleep(0.02)
            robot.set_wheels_speed(0)
            robot.sleep(0.01)
        elif sum(robot.get_left_line_sensors()) > sum(robot.get_right_line_sensors()):
            robot.set_left_wheel_speed(70)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.02)
            robot.set_wheels_speed(0)
            robot.sleep(0.01)
        elif 0 not in robot.get_line_sensors() and 1024 not in robot.get_line_sensors():
            robot.set_right_wheel_speed(100)
            robot.set_left_wheel_speed(-100)
            robot.sleep(0.3)
        elif counter == 1:
            robot.set_right_wheel_speed(80)
            robot.set_left_wheel_speed(-80)
            robot.sleep(0.35)
            counter += 1
            big_counter += 1
        elif big_counter in [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16]:
            robot.set_wheels_speed(100)
            robot.sleep(0.1)
            big_counter += 1
            counter = 0
        elif big_counter == 18:
            robot.done()
            break
        elif sum(robot.get_line_sensors()) == 6144:
            robot.set_right_wheel_speed(80)
            robot.set_left_wheel_speed(-80)
            robot.sleep(0.16)
            counter += 1
            big_counter = if_big_counter(big_counter)
        else:
            robot.set_wheels_speed(10)
            robot.sleep(0.05)


def if_big_counter(big_counter):
    """If big counter is 9, 10 or 17, + 1."""
    if big_counter == 9 or big_counter == 10 or big_counter == 17:
        return big_counter + 1
    return big_counter


def drive_to_start(robot):
    """Drive to line."""
    while 0 not in robot.get_line_sensors():
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
