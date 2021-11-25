"""EX13 Board Games."""


class Statistics:
    """Collect data and create statistics."""

    def __init__(self, filename: str):
        """Statistics constructor."""
        self.games = []
        self.players = []
        self.filename = filename
        self.import_data()

    def import_data(self):
        data_list = []
        with open(self.filename) as file:
            for line in file:
                data_list.append(tuple(line[:-1].split(";")))
        self.add_player_from_data(data_list)
        self.add_games_from_data(data_list)

    def get(self, path: str):
        """Return requested statistics."""
        if path == "/players":
            return [player.name for player in self.players]
        elif path == "/games":
            return [game.name for game in self.games]
        elif path == "/total":
            return sum([len(game.winners) for game in self.games])
        if "/player" in path:
            return self.get_player_stat(path)

    def get_player_stat(self, path):
        """Get player statistics."""
        if "/amount" in path:
            player_name = path[8:path.index("/amount")]
            player = self.find_player_in_list(player_name)
            return sum(player.games.values())
        elif "/favorite" in path:
            player_name = path[8:path.index("/favorite")]
            player = self.find_player_in_list(player_name)
            game_count = 0
            game = ""
            for key, value in player.games.items():
                if value > game_count:
                    game_count = value
                    game = key
            return game
        elif "/won" in path:
            player_name = path[8:path.index("/won")]
            player = self.find_player_in_list(player_name)
            return sum(player.wins.values())

    def add_games_from_data(self, data_list):
        """Create and add games."""
        for element in data_list:
            in_list = False
            for game in self.games:
                if element[0] == game.name:
                    game = game
                    in_list = True
            if not in_list:
                game = Game(element[0], element[2])
                self.games.append(game)
            players = element[1].split(",")
            game.winners.append(self.find_winner(players, element))
            if game.type == "points":
                points = element[3].split(",")
                for i, player in enumerate(players):
                    game.add_results((player, points[i]))
            elif game.type == "places":
                players = element[3].split(",")
                for i, player in enumerate(players):
                    game.add_results((player, i + 1))
            elif game.type == "winner":
                for player in players:
                    if player == element[3]:
                        game.add_results((player, 1))
                    else:
                        game.add_results((player, 2))

    def add_player_from_data(self, data_list):
        """Create and add player."""
        for element in data_list:
            players = element[1].split(",")
            winner_name = self.find_winner(players, element)
            for player_name in players:
                player = self.find_player_in_list(player_name)
                if not player:
                    player = Player(player_name)
                    self.players.append(player)
                if player_name == winner_name:
                    player.add_win(element[0])
                player.add_game_count(element[0])

    def find_winner(self, players, element):
        """Find winner."""
        if element[2] == "points":
            points = element[3].split(",")
            max_points = max(points)
            points_index = points.index(max_points)
            return players[points_index]
        elif element[2] == "places":
            places = element[3].split(",")
            return places[0]
        elif element[2] == "winner":
            return element[3]

    def find_player_in_list(self, player_name):
        """Find player in player list."""
        for player in self.players:
            if player_name == player.name:
                return player
        return False


class Player:
    """Info about player."""

    def __init__(self, name: str):
        """Player constructor."""
        self.name = name
        self.wins = {}
        self.games = {}

    def __repr__(self):
        """Name."""
        return self.name

    def add_win(self, game: str):
        """Add points to points dict."""
        if game not in self.wins:
            self.wins[game] = 1
        else:
            self.wins[game] += 1

    def add_game_count(self, game: str):
        """Count games."""
        if game not in self.games:
            self.games[game] = 1
        else:
            self.games[game] += 1


class Game:
    """Statistics about games."""
    def __init__(self, name: str, game_type: str):
        self.name = name
        self.type = game_type
        self.results = {}
        self.winners = []

    def __repr__(self):
        """Name."""
        return self.name

    def add_results(self, result: tuple):
        """Get list of tuples (player name, result) and add to results dict."""
        if result[0] not in self.results:
            self.results[result[0]] = [result[1]]
        else:
            self.results[result[0]].append(result[1])


if __name__ == "__main__":
    stat = Statistics("data.txt")
    print(stat.get("/total"))
