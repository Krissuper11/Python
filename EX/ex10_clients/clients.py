"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Client earnings per day since the start.

        You can either calculate the value or
        save it into a new attribute and return the value.
        """
        earnings_per_day = (self.current_amount - self.starting_amount) / self.account_age
        return earnings_per_day


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    person_list = []
    with open(filename) as file:
        data = file.read()
    data_list = data.split("\n")
    try:
        for element in data_list:
            info_list = element.split(",")
            person_list.append(Client(info_list[0], info_list[1], int(info_list[2]), int(info_list[3]), int(info_list[4])))
    except IndexError:
        return []
    return person_list


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    filtered_person_list = []
    person_list = read_from_file_into_list(filename)
    for person in person_list:
        if person.bank == bank:
            filtered_person_list.append(person)
    return filtered_person_list


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    person_list = read_from_file_into_list(filename)
    person_list_sorted = sorted(person_list, key=lambda x: (x.earnings_per_day() * -1, x.account_age))
    try:
        if person_list_sorted[0].current_amount <= person_list_sorted[0].starting_amount:
            return None
        else:
            return person_list_sorted[0]
    except IndexError:
        return None


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    person_list = read_from_file_into_list(filename)
    person_list_sorted = sorted(person_list, key=lambda x: (x.earnings_per_day(), x.account_age))
    try:
        if person_list_sorted[0].current_amount >= person_list_sorted[0].starting_amount:
            return None
        else:
            return person_list_sorted[0]
    except IndexError:
        return None


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]

    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]

    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh

    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
