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
    while 0 not in robot.get_line_sensors():
        robot.set_wheels_speed(15)
        robot.sleep(1)
        robot.set_wheels_speed(0)
    while True:
        if robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
            robot.set_wheels_speed(5)
            robot.sleep(1)
        elif robot.get_second_line_sensor_from_right() == 0:
            robot.set_left_wheel_speed(10)
            robot.sleep(1)
        elif robot.get_second_line_sensor_from_left() == 0:
            robot.set_right_wheel_speed(10)
            robot.sleep(1)
        else:
            robot.set_wheels_speed(0)
            robot.done()
            break


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
