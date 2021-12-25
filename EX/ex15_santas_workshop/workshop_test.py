import santas_workshop

info = santas_workshop.Info("ex15_naughty_list.csv", "ex15_nice_list.csv", "ex15_wish_list.csv")
factory = santas_workshop.Factory(info)
factory.produce_presents()
flight = santas_workshop.FlightPlan(factory)
flight.create_flight_plan()
flight.prepare_transport()


def test_add_to_list():
    """Test that all children are added."""
    assert len(info.nice_children) == 291
    assert len(info.naughty_children) == 108
    nice_children = ["Stacy", "Libby", "Dillion", "Selena", "Mimi"]
    nice_names = [child.name for child in info.nice_children]
    naughty_children = ["Bailey", "Tanya", "Sylvia", "Austin", "Mel"]
    naughty_names = [child.name for child in info.naughty_children]
    for child_name in nice_children:
        assert child_name in nice_names and child_name not in naughty_names
    for child_name in naughty_children:
        assert child_name in naughty_names and child_name not in nice_children


def test_correct_countries():
    """Test that country is read correctly."""
    nice_dict = {}
    naughty_dict = {}
    nice_children = {"Stacy": "United Kingdom", "Libby": "United Kingdom",
                     "Dillion": "Germany", "Selena": "Australia", "Mimi": "Canada"}
    for child in info.nice_children:
        nice_dict[child.name] = child.country
    naughty_children = {"Bailey": "Peru", "Tanya": "United Kingdom", "Sylvia": "United Kingdom",
                        "Austin": "Peru", "Mel": "Sweden"}
    for child in info.naughty_children:
        naughty_dict[child.name] = child.country
    for name in nice_children:
        assert nice_dict[name] == nice_children[name]
    for name in naughty_children:
        assert naughty_dict[name] == naughty_children[name]


def test_presents_added_correctly():
    """Test that presents are added correctly from wish list."""
    nice_dict = {}
    naughty_dict = {}
    nice_children = {"Stacy": ["Polyhedral dice set", "Wall-mount diamond pickaxe", "500 TikTok followers"],
                     "Libby": ["Zebra Jumpy", "Princess dress", "Lego death star"],
                     "Dillion": ["Xbox Series X"], "Selena": ["Baby born doll", "Toy kitchen set"],
                     "Mimi": ["Toy dinosaur play set"]}
    for child in info.nice_children:
        nice_dict[child.name] = child.presents
    naughty_children = {
        "Bailey": ["Magic: The Gathering Commander Legends booster box", "Ninja Turtles backpack", "Zebra Jumpy"],
        "Tanya": ["Nintendo Switch", "Frozen Olaf plush toy"], "Sylvia": ["Tablet computer"],
        "Austin": ["Carbon fiber road bike"], "Mel": ["Lego Grogu"]}
    for child in info.naughty_children:
        naughty_dict[child.name] = child.presents
    for name in nice_children:
        assert nice_dict[name] == nice_children[name]
    for name in naughty_children:
        assert naughty_dict[name] == naughty_children[name]


def test_gift_created_correctly():
    """Test that gift has correct information (name, weight)"""
    test_list = {"Stacy": factory.completed_presents["Stacy"], "Libby": factory.completed_presents["Libby"]}
    gifts = {"Stacy": {"Polyhedral dice set": 10, "Wall-mount diamond pickaxe": 695, "500 TikTok followers": 1},
             "Libby": {"Zebra Jumpy": 1337, "Princess dress": 278, "Lego death star": 2000}}
    name_counter = 0
    for key, value in test_list.items():
        for gift in value:
            assert gift.gift_name in gifts[key].keys()
            assert gift.child_name == list(gifts.keys())[name_counter]
            assert gift.weight == gifts[key][gift.gift_name]
        name_counter += 1


def test_good_children_get_all():
    """Test that good children get all what they wished."""
    nice_children = {"Stacy": 3, "Libby": 3, "Dillion": 1, "Selena": 2, "Mimi": 1}
    for child in nice_children:
        assert len(factory.completed_presents[child]) == nice_children[child]


def test_naughty_get_only_one():
    """Test that naughty children get no more than one gift."""
    naughty_children = ["Bailey", "Tanya", "Sylvia", "Jay", "Danni"]
    for child in naughty_children:
        assert len(factory.completed_presents[child]) == 1


def test_correct_flight_plan():
    """Test correct flight plan."""
    correct_num = len([child.country for child in info.nice_children if child.country == "Estonia"])
    correct_num += len([child.country for child in info.naughty_children if child.country == "Estonia"])
    assert len(flight.flight_plan["Estonia"]) == correct_num
    correct_num = len([child.country for child in info.nice_children if child.country == "United Kingdom"])
    correct_num += len([child.country for child in info.naughty_children if child.country == "United Kingdom"])
    assert len(flight.flight_plan["United Kingdom"]) == correct_num


def test_optimized_transport():
    """Test correct optimization."""
    # Test if weight is exactly 50kg.
    info = santas_workshop.Info("nice_test_transport.csv", "naughty_test_transport.csv", "wish_list_test.csv")
    factory = santas_workshop.Factory(info)
    factory.produce_presents()
    flight = santas_workshop.FlightPlan(factory)
    flight.create_flight_plan()
    flight.prepare_transport()
    assert len(flight.ready_transport["Estonia"]) == 1
    # Test if over 50 and if first gift does not fit, but second fits
    assert len(flight.ready_transport["Finland"]) == 2
    assert "Georgi" not in flight.ready_transport["Finland"][0].gifts \
           and "Pekka" in flight.ready_transport["Finland"][0].gifts



def test_delivery_note():
    """Test delivery note."""
    this_test_info = santas_workshop.Info("naughty_test.csv", "nice_test.csv", "wish_list_test.csv")
    this_test_factory = santas_workshop.Factory(this_test_info)
    this_test_factory.produce_presents()
    this_test_flight = santas_workshop.FlightPlan(this_test_factory)
    this_test_flight.create_flight_plan()
    this_test_flight.prepare_transport()
    assert this_test_flight.ready_transport["Estonia"][0].delivery_note == \
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
TO: ESTONIA

//==========[]========================================================[]==================\\
||   Name   ||                         Gifts                          || Total Weight(kg) ||
|]==========[]========================================================[]==================[|
|| Smidl    || Cyberpunk 2077, Digital camera, Beyblade Burst spinner ||              1.2 ||
|| Danja    || World of Warcraft: Shadowlands Collectors Edition      ||              0.3 ||
|| Kristina || Ninja Turtles backpack, Tablet computer, VHS player    ||             1.98 ||
\\==========[]========================================================[]==================//"""
    this_test_info = santas_workshop.Info("naughty_test.csv", "nice_test_note.csv", "wish_list_test.csv")
    this_test_factory = santas_workshop.Factory(this_test_info)
    this_test_factory.produce_presents()
    this_test_flight = santas_workshop.FlightPlan(this_test_factory)
    this_test_flight.create_flight_plan()
    this_test_flight.prepare_transport()
    assert this_test_flight.ready_transport["Estonia"][0].delivery_note == \
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
TO: ESTONIA

//======[]=========[]==================\\
|| Name ||  Gifts  || Total Weight(kg) ||
|]======[]=========[]==================[|
|| Eva  || Crayons ||             0.05 ||
\\======[]=========[]==================//"""


def test_post_office():
    """Test that post office read letters correctly."""
    # Test when no info about gifts
    info = santas_workshop.Info("test_empty.csv", "test_empty.csv", "test_empty.csv")
    santas_workshop.PostOffice(info).read_letter("Dear Santa!\n\nI saw an elf the other day, he was just making it out through the window when I spotted him\n\nSincerely yours,\nMaxwell, Puerto Rico")
    assert len(info.nice_children) == 0

    # Test when usual letter
    info = santas_workshop.Info("test_empty.csv", "test_empty.csv", "test_empty.csv")
    santas_workshop.PostOffice(info).read_letter("Hi, Santa!\n\nI saw an elf the other day, he was just making it out through the window when I spotted him\n\nThe following is my wishlist: Wall-mount diamond pickaxe, Magic: The Gathering Commander Legends booster box.\n\nThanks, Santa,\nAmelia, South Africa")
    assert len(info.nice_children) == 1
    child = info.nice_children[0]
    assert child.name == "Amelia"
    assert child.country == "South Africa"
    assert child.presents == ["Wall-mount diamond pickaxe", "Magic: The Gathering Commander Legends booster box"]

    # Test when Caesar cipher
    info = santas_workshop.Info("test_empty.csv", "test_empty.csv", "test_empty.csv")
    santas_workshop.PostOffice(info).read_letter("hiev qv erh qvw werxe!\n\nm lezi fiir vieppc kssh xlmw ciev.\n\nxli jsppsamrk mw qc amwlpmwx: tspev fiev tpywlmi, gcfivtyro 2077, omxxir tpywlmi.\n\nxlero csy,\nnegowsr, wsyxl ejvmge")
    assert len(info.nice_children) == 1
    child = info.nice_children[0]
    assert child.name == "Jackson"
    assert child.country == "South Africa"
    assert child.presents == ["polar bear plushie", "cyberpunk 2077", "kitten plushie"]

    # Test with base64
    info = santas_workshop.Info("test_empty.csv", "test_empty.csv", "test_empty.csv")
    santas_workshop.PostOffice(info).read_letter("SGVsbG8sIFNhbnRhIQoKSSBoYXZlIGJlZW4gdmVyeSBuaWNlIHRvIG15IGZhbWlseSBhbmQgZnJpZW5kcywgYW5kIGV2ZW4gc29tZSBwZW9wbGUgd2hvIGhhdmUgbm90IGJlZW4gdmVyeSBuaWNlIHRvIG1lLCBsaWtlIG91ciBuZWlnaGJvciB3aG8geWVsbHMgYXQgbWUgd2hlbiBJIHBsYXkgd2l0aCB0aGUgd2F0ZXJob3NlLgoKVGhpcyB5ZWFyLCBJIHdhbnQgUGluayB0cmljeWNsZS4KCkNhbid0IHdhaXQgdG8gc2VlIHlvdSwKQnJlbm5hbiwgUHVlcnRvIFJpY28=")
    assert len(info.nice_children) == 1
    child = info.nice_children[0]
    assert child.name == "Brennan"
    assert child.country == "Puerto Rico"
    assert child.presents == ["Pink tricycle"]


def test_bad_files():
    """Test wrong files."""
    # Test empty files
    info = santas_workshop.Info("test_empty.csv", "test_empty.csv", "test_empty.csv")
    factory = santas_workshop.Factory(info)
    factory.produce_presents()
    flight = santas_workshop.FlightPlan(factory)
    flight.create_flight_plan()
    flight.prepare_transport()
    assert len(info.nice_children) == 0
    assert len(info.naughty_children) == 0
    assert len(factory.completed_presents) == 0
    assert len(flight.ready_transport) == 0

    # Test when no gift in database
    info = santas_workshop.Info("test_empty.csv", "test_wrong_gift.csv", "wish_list_test.csv")
    factory = santas_workshop.Factory(info)
    factory.produce_presents()
    flight = santas_workshop.FlightPlan(factory)
    flight.create_flight_plan()
    flight.prepare_transport()
    assert len(info.nice_children) == 1
    assert len(info.nice_children[0].presents) == 1
    assert len(factory.completed_presents) == 0
    assert len(flight.ready_transport) == 0
