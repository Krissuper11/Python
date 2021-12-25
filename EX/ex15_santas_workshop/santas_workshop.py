"""EX 15."""
import binascii
import csv
import json
import urllib.request
import urllib.parse
import urllib.error
from copy import deepcopy
import re
import base64


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
        for child in self.naughty_children:
            if child.name == name:
                return child
        return None


class Child:
    """Child info."""

    def __init__(self, name: str, child_type: str, country: str):
        """Child constructor."""
        self.name = name
        self.child_type = child_type
        self.country = country
        self.presents = []

    def __repr__(self):
        """Name."""
        return self.name

    def add_presents(self, wish_list: list):
        """Add presents to child from file."""
        self.presents += wish_list


class Factory:
    """Santa's factory."""

    def __init__(self, info: Info):
        """Factory constructor."""
        self.completed_presents = {}
        self.info = info
        self.presents = []

    def produce_presents(self):
        """Produce presents."""
        children_list = deepcopy(sorted(self.info.nice_children, key=lambda x: len(x.presents), reverse=True))
        counter = 0
        time_count = 0
        try:
            max_counter = len(children_list[0].presents)
        except IndexError:
            return None
        while counter <= max_counter:
            for i, child in enumerate(self.info.nice_children):
                if time_count < 525600:
                    time_count += self.add_gift_info(child, counter)
                elif 525600 < time_count < max_counter:
                    counter += max_counter
            if counter == 0:
                for child in self.info.naughty_children:
                    if time_count < 525600:
                        time_count += self.add_gift_info(child, counter)
                    elif 8760 < time_count < max_counter:
                        counter += max_counter
            counter += 1

    def add_gift_info(self, child, counter):
        """Add information about gift."""
        try:
            query = child.presents[counter]
            gift = deepcopy(self.find_gift_in_list(query))
            if gift is None:
                page = urllib.parse.urlencode({"name": query})
                response = urllib.request.urlopen(f"http://api.game-scheduler.com:8089/gift?{page}")
                gift_info = json.loads(response.read().decode())
                gift = Gift(gift_info["gift"], child.name, child.country, gift_info["weight_in_grams"], gift_info["production_time"])
                self.presents.append(gift)
            else:
                gift.child_name = child.name
                gift.country = child.country
            if child.name not in self.completed_presents:
                self.completed_presents[child.name] = [gift]
            else:
                self.completed_presents[child.name].append(gift)
            return gift.time
        except IndexError:
            return 0
        except urllib.error.HTTPError:
            return 0


    def find_gift_in_list(self, gift_name):
        """Find gift."""
        for gift in self.presents:
            if gift.gift_name == gift_name:
                return gift
        return None


class Gift:
    """Gift."""

    def __init__(self, gift_name, child_name, country, weight, time):
        """Present constructor."""
        self.gift_name = gift_name
        self.child_name = child_name
        self.country = country
        self.weight = weight
        self.time = time

    def __repr__(self):
        """Name."""
        return self.gift_name


class FlightPlan:
    """Prepare for departure."""

    def __init__(self, factory: Factory):
        """FlightPlan constructor."""
        self.factory = factory
        self.flight_plan = {}
        self.ready_transport = {}

    def create_flight_plan(self):
        """Create flight plan."""
        for present_list in self.factory.completed_presents.values():
            if present_list[0].country not in self.flight_plan:
                self.flight_plan[present_list[0].country] = [present_list]
            else:
                self.flight_plan[present_list[0].country].append(present_list)

    def prepare_transport(self):
        """Prepare transport."""
        for country, country_gift_list in self.flight_plan.items():
            for gift_list in country_gift_list:
                for gift in gift_list:
                    added_check = False
                    if country not in self.ready_transport:
                        self.ready_transport[country] = [Transport(country)]
                    for transport in self.ready_transport[country]:
                        if gift.weight <= transport.space_left and not added_check:
                            transport.add_gifts(gift)
                            transport.space_left -= gift.weight
                            added_check = True
                            continue
                    if not added_check:
                        transport = Transport(country)
                        self.ready_transport[country].append(transport)
                        transport.add_gifts(gift)
        for transport_list in self.ready_transport.values():
            for transport in transport_list:
                transport.create_delivery_note()


class Transport:
    """Transport."""

    def __init__(self, country):
        self.country = country
        self.space_left = 50000
        self.gifts = {}
        self.delivery_note = ""

    def __repr__(self):
        return self.country

    def add_gifts(self, gift):
        """Add gifts."""
        if gift.child_name not in self.gifts:
            self.gifts[gift.child_name] = [gift]
        else:
            self.gifts[gift.child_name].append(gift)

    def create_delivery_note(self):
        """Create delivery note."""
        self.delivery_note += \
            r"""                          DELIVERY ORDER
                                                          _v
                                                     __* (__)
             ff     ff     ff     ff                {\/ (_(__).-.
      ff    <_\__, <_\__, <_\__, <_\__,      __,~~.(`>|-(___)/ ,_)
    o<_\__,  (_ ff ~(_ ff ~(_ ff ~(_ ff~~~~~@ )\/_;-"``     |
      (___)~~//<_\__, <_\__, <_\__, <_\__,    | \__________/|
      // >>     (___)~~(___)~~(___)~~(___)~~~~\\_/_______\_//
                // >>  // >>  // >>  // >>     `'---------'` 

FROM: NORTH POLE CHRISTMAS CHEER INCORPORATED
TO: """
        self.delivery_note += self.country.upper() + "\n" + "\n"
        gift_dict_by_name = sorted(self.gifts, key=lambda x: len(x), reverse=True)
        max_name = len(gift_dict_by_name[0])
        if max_name < 4:
            max_name = 4
        max_gift_length = 0
        for gift_list in self.gifts.values():
            gift_list_length = len(str(gift_list))
            if gift_list_length > max_gift_length:
                max_gift_length = gift_list_length - 2
        if max_gift_length < 5:
            max_gift_length = 5
        self.delivery_note += f"//={'=' * max_name}=[]={'=' * max_gift_length}=[]{'=' * 18}\\\\\n"
        self.delivery_note += f"|| {' ' * ((max_name - 4) // 2)}Name{' ' * ((max_name - 4) - (max_name - 4) // 2)}" \
                              f" || {' ' * ((max_gift_length - 5) // 2)}Gifts" \
                              f"{' ' * ((max_gift_length - 5) - (max_gift_length - 5) // 2)} || Total Weight(kg) ||\n"
        self.delivery_note += f"|]={'=' * max_name}=[]={'=' * max_gift_length}=[]{'=' * 18}[|\n"
        for name, gift_list in self.gifts.items():
            gift_list_length = len(str(gift_list)) - 2
            weight_sum = round(sum([int(gift.weight) / 1000 for gift in gift_list]), 2)
            self.delivery_note += f"|| {name}{' ' * (max_name - len(name))} || {str(gift_list)[1:-1]}" \
                                  f"{' ' * (max_gift_length - gift_list_length)} || " \
                                  f"{' ' * (16 - len(str(weight_sum)))}{weight_sum} ||\n"
        self.delivery_note += f"\\\\={'=' * max_name}=[]={'=' * max_gift_length}=[]{'=' * 18}//"


class PostOffice:
    """Santa's Post office."""

    def __init__(self, info):
        """Constructor."""
        self.info = info
        self.name = ""
        self.name_check = []

    def read_letter(self, test_parameter: str = None):
        """
        Read letter.

        Test parameter is used only while testing to give exact string to read.
        """
        for i in range(50):
            counter = 0
            if test_parameter is not None:
                gift_info = test_parameter
            else:
                response = urllib.request.urlopen("http://api.game-scheduler.com:8089/letter")
                gift_info = json.loads(response.read().decode())
            task_completed = self.set_data(gift_info, counter)
            if task_completed is False and counter == 0:
                counter += 1
                gift_info_encoded = self.encode(gift_info, -4)
                task_completed = self.set_data(gift_info_encoded, counter)
            if task_completed is False and counter == 1:
                counter += 1
                try:
                    gift_info_encoded = base64.b64decode(gift_info).decode("UTF-8")
                    self.set_data(gift_info_encoded, counter)
                except UnicodeDecodeError:
                    pass
                except binascii.Error:
                    pass
            if test_parameter is not None:
                break

    def set_data(self, gift_info, counter):
        """Set data."""
        name = None
        result = re.findall(r"(?<=[Ii] want ).+(?=\.)|(?<=[Ii] wish for ).+(?=\.)|(?<=wishlist: ).+(?=\.)",
                            gift_info)
        res = re.finditer(r"(?<=\n)([\w ]+), ([\w ]+)$", gift_info)
        for match in res:
            name = match.group(1)
            country = match.group(2)
        if counter == 1 and name is not None:
            name = name.title()
            country = country.title()
            if "of" in country:
                country[country.index("of"):country.index("of") + 2] = "of"
        if len(result) == 0 or name is None:
            return False
        if name not in self.name_check:
            self.name_check.append(name)
            if self.info.find_children_in_list(name) is None:
                child = Child(name, "nice", country)
                self.info.nice_children.append(child)
            else:
                child = self.info.find_children_in_list(name)
            for gift_list in result:
                gift_str = gift_list.split(", ")
                for gift in gift_str:
                    if gift.lower() not in [gift1.lower() for gift1 in child.presents]:
                        child.presents.append(gift)
        return True

    def encode(self, message: str, shift: int) -> str:
        """Encode a message using a Caesar cipher."""
        new_letter = ""
        for i in range(len(message)):
            if message[i] == "n" and message[i - 1] == "\\":
                continue
            elif not message[i].isalpha():
                new_letter += message[i]
            elif message[i].isalpha():
                index = ord(message[i]) + shift
                index -= 26 * ((index - 97) // 26)
                new_letter += chr(index)
            else:
                pass
        return new_letter


if __name__ == '__main__':
    info = Info("test_empty.csv", "test_empty.csv", "ex15_wish_list.csv")
    factory = Factory(info)
    PostOffice(info).read_letter("SGVsbG8sIFNhbnRhIQoKSSBoYXZlIGJlZW4gdmVyeSBuaWNlIHRvIG15IGZhbWlseSBhbmQgZnJpZW5kcywgYW5kIGV2ZW4gc29tZSBwZW9wbGUgd2hvIGhhdmUgbm90IGJlZW4gdmVyeSBuaWNlIHRvIG1lLCBsaWtlIG91ciBuZWlnaGJvciB3aG8geWVsbHMgYXQgbWUgd2hlbiBJIHBsYXkgd2l0aCB0aGUgd2F0ZXJob3NlLgoKVGhpcyB5ZWFyLCBJIHdhbnQgUGluayB0cmljeWNsZS4KCkNhbid0IHdhaXQgdG8gc2VlIHlvdSwKQnJlbm5hbiwgUHVlcnRvIFJpY28=")
    factory.produce_presents()
    flight = FlightPlan(factory)
    flight.create_flight_plan()
    flight.prepare_transport()
    print(flight.ready_transport)
    print(flight.ready_transport["Puerto Rico"][0].delivery_note)
