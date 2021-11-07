"""XP01."""
import math


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:

    """Calculate the meeting position of 2 jangurus.
    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru
    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru

    @:return positions where jangurus first meet
    """
    time_move = math.gcd(sleep1, sleep2)
    same_sleep_time = math.lcm(sleep1, sleep2)
    time = 1
    while time <= same_sleep_time:
        if time == sleep1:
            pos1 += jump_distance1
        if time == sleep2:
            pos2 += jump_distance2
        if pos1 == pos2:
            return pos1
        time += time_move
    try:
        return meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2)
    except RecursionError:
        return -1


if __name__ == "__main__":
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(1, 7, 1, 15, 5, 1))  #  => 50
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(1, 2, 1, 1, 3, 1))  # => -1