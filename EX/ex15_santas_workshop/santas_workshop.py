"""EX 15."""
import csv


class Info:
    """Info centre."""

    def __init__(self, naughty_list_file: str, nice_list_file: str, wish_list_file: str):
        """Info constructor."""
        self.naughty_children = self.add_children_from_list(naughty_list_file, "naughty")
        self.nice_children = self.add_children_from_list(nice_list_file, "nice")
        self.add_presents_from_wishlist(wish_list_file)

    def add_children_from_list(self, file: str, child_type: str):
        """Read file and add children to certain list."""
        result_list = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if child_type == "nice":
                    result_list.append(Child(row[0], "nice", row[1][1:]))
                else:
                    result_list.append(Child(row[0], "naughty", row[1][1:]))
        return result_list

    def add_presents_from_wishlist(self, file):
        """Add presents from file to present list."""
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                child = self.find_children_in_list(row[0])
                if child is not None:
                    child.add_presents([row[i][1:] for i in range(1, len(row))])

    def find_children_in_list(self, name: str):
        """Find child in list."""
        for child in self.nice_children:
            if child.name == name:
                return child
            else:
                return None


class Child:
    """Child info."""

    def __init__(self, name: str, child_type: str, country: str):
        """Child constructor."""
        self.name = name
        self.child_type = child_type
        self.country = country
        self.presents = []

    def add_presents(self, wish_list: list):
        """Add presents to child from file."""
        self.presents += wish_list


if __name__ == '__main__':
    info = Info("ex15_naughty_list.csv", "ex15_nice_list.csv", "ex15_wish_list.csv")