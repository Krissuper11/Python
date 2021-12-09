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
    while 0 not in robot.get_line_sensors():
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
    while True:
        if robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
            robot.set_wheels_speed(45)
            robot.sleep(0.01)
            counter = 0
        elif sum(robot.get_left_line_sensors()) < sum(robot.get_right_line_sensors()) and counter != 1:
            robot.set_right_wheel_speed(70)
            robot.set_left_wheel_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            robot.sleep(0.01)
        elif sum(robot.get_left_line_sensors()) > sum(robot.get_right_line_sensors()):
            robot.set_left_wheel_speed(70)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            robot.sleep(0.01)
        elif counter == 1:
            robot.set_right_wheel_speed(80)
            robot.set_left_wheel_speed(-80)
            robot.sleep(0.42)
            counter += 1
            big_counter += 1
        elif counter == 2 or big_counter == 2:
            robot.done()
            break
        elif sum(robot.get_line_sensors()) == 6144 and big_counter != 2:
            robot.set_right_wheel_speed(80)
            robot.set_left_wheel_speed(-80)
            robot.sleep(0.15)
            counter += 1

    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move.
    """
