"""EX13 Board Games."""


class Statistics:
    """Collect data and create statistics."""

    def __init__(self, filename: str):
        """Stat constructor."""
        self.games = []
        self.players = []
        self.filename = filename
        self.import_data()

    def import_data(self):
        """Get data from file."""
        data_list = []
        with open(self.filename) as file:
            for line in file:
                if "\n" in line:
                    data_list.append(tuple(line[:-1].split(";")))
                else:
                    data_list.append(tuple(line.split(";")))
        self.add_player_from_data(data_list)
        self.add_games_from_data(data_list)

    def get(self, path: str):
        """Return requested statistics."""
        if path == "/players":
            return [player.name for player in self.players]
        elif path == "/games":
            return [game.name for game in self.games]

        elif "/total" in path:
            if "/total/" in path:
                if path[7:] == "points":
                    return sum([game.counter for game in self.games if game.type == "points"])
                elif path[7:] == "places":
                    return sum([game.counter for game in self.games if game.type == "places"])
                elif path[7:] == "winner":
                    return sum([game.counter for game in self.games if game.type == "winner"])
            return sum([game.counter for game in self.games])

        elif "/game" in path:
            return self.get_game_stat(path)

        elif "/player" in path:
            return self.get_player_stat(path)

    def get_player_stat(self, path):
        """Get player statistics."""
        if "/amount" in path:
            player_name = path[8:path.index("/amount")]
            player = self.find_player_in_list(player_name)
            return sum(player.games.values())

        elif "/favourite" in path:
            player_name = path[8:path.index("/favourite")]
            player = self.find_player_in_list(player_name)
            game_count = 0
            for key, value in player.games.items():
                if value > game_count:
                    game_count = value
                    game = self.find_game_in_list(key)
            return game.name

        elif "/won" in path:
            player_name = path[8:path.index("/won")]
            player = self.find_player_in_list(player_name)
            return sum(player.wins.values())

    def get_game_stat(self, path):
        """Get game stat."""
        if "/amount" in path:
            game_name = path[6:path.index("/amount")]
            return self.find_game_in_list(game_name).counter
        elif "/player-amount" in path:
            game_name = path[6:path.index("/player-amount")]
            game = self.find_game_in_list(game_name)
            return max(game.number_of_players, key=game.number_of_players.count)
        elif "/most-wins" in path:
            game_name = path[6:path.index("/most-wins")]
            game = self.find_game_in_list(game_name)
            return max(game.winners, key=game.winners.count)
        elif "/most-frequent-winner" in path:
            self.get_most_freq_winner(path)
        elif "/most-losses" in path:
            game_name = path[6:path.index("/most-losses")]
            game = self.find_game_in_list(game_name)
            return min(game.losers, key=game.losers.count)
        elif "/most-frequent-loser" in path:
            self.get_most_freq_loser(path)
        elif "/record-holder" in path:
            game_name = path[6:path.index("/record-holder")]
            game = self.find_game_in_list(game_name)
            record = 0
            for player in game.results:
                max_result = int(max(game.results[player]))
                if max_result > record:
                    record = max_result
                    record_holder = player
            return record_holder

    def get_most_freq_winner(self, path: str):
        """Find most frequent winner."""
        game_name = path[6:path.index("/most-frequent-winner")]
        game_win_freq = 0
        for player in self.players:
            if game_name in player.wins and game_name in player.games:
                win_freq = player.wins[game_name] / player.games[game_name]
                if win_freq > game_win_freq:
                    game_win_freq = win_freq
                    best_player = player.name
        return best_player

    def get_most_freq_loser(self, path: str):
        """Find most frequent loser."""
        game_name = path[6:path.index("/most-frequent-loser")]
        game_loss_freq = 0
        for player in self.players:
            if game_name in player.losses and game_name in player.games:
                loss_freq = player.losses[game_name] / player.losses[game_name]
                if loss_freq > -game_loss_freq:
                    game_loss_freq = -loss_freq
                    player_name = player.name
        return player_name

    def add_games_from_data(self, data_list):
        """Create and add games."""
        for element in data_list:
            game = self.find_game_in_list(element[0])
            if not game:
                game = Game(element[0], element[2])
                self.games.append(game)
            players = element[1].split(",")
            game.add_count(element[1])
            game.winners.append(self.find_winner(players, element))

            if game.type == "points":
                game.losers.append(self.find_loser(players, element))
                points = element[3].split(",")
                for i, player in enumerate(players):
                    game.add_results((player, points[i]))
            elif game.type == "places":
                game.losers.append(self.find_loser(players, element))
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
        loser_name = ""
        for element in data_list:
            players = element[1].split(",")
            winner_name = self.find_winner(players, element)
            if element[2] == "points" or element[2] == "places":
                loser_name = self.find_loser(players, element)
            for player_name in players:
                player = self.find_player_in_list(player_name)
                if not player:
                    player = Player(player_name)
                    self.players.append(player)
                if player_name == winner_name:
                    player.add_win(element[0])
                if player_name == loser_name:
                    player.add_loss(element[0])
                player.add_game_count(element[0])

    def find_winner(self, players, element):
        """Find winner."""
        if element[2] == "points":
            points = [int(element) for element in element[3].split(",")]
            max_points = max(points)
            points_index = points.index(max_points)
            return players[points_index]

        elif element[2] == "places":
            places = element[3].split(",")
            return places[0]

        elif element[2] == "winner":
            return element[3]

    def find_loser(self, players, element):
        """Find loser."""
        if element[2] == "points":
            points = [int(element) for element in element[3].split(",")]
            min_points = min(points)
            points_index = points.index(min_points)
            return players[points_index]

        elif element[2] == "places":
            places = element[3].split(",")
            return places[-1]

    def find_player_in_list(self, player_name):
        """Find player in player list."""
        for player in self.players:
            if player_name == player.name:
                return player
        return False

    def find_game_in_list(self, game_name):
        """Find game in game list."""
        for game in self.games:
            if game_name == game.name:
                return game
        return False


class Player:
    """Info about player."""

    def __init__(self, name: str):
        """Player constructor."""
        self.name = name
        self.wins = {}
        self.games = {}
        self.losses = {}

    def __repr__(self):
        """Name."""
        return self.name

    def add_win(self, game: str):
        """Add win to wins dict."""
        if game not in self.wins:
            self.wins[game] = 1
        else:
            self.wins[game] += 1

    def add_loss(self, game: str):
        """Add loss to losses dict."""
        if game not in self.losses:
            self.losses[game] = 1
        else:
            self.losses[game] += 1

    def add_game_count(self, game: str):
        """Count games."""
        if game not in self.games:
            self.games[game] = 1
        else:
            self.games[game] += 1


class Game:
    """Statistics about games."""

    def __init__(self, name: str, game_type: str):
        """Game constructor."""
        self.name = name
        self.type = game_type
        self.results = {}
        self.winners = []
        self.losers = []
        self.counter = 0
        self.number_of_players = []

    def __repr__(self):
        """Name."""
        return self.name

    def add_results(self, result: tuple):
        """Get list of tuples (player name, result) and add to results dict."""
        if result[0] not in self.results:
            self.results[result[0]] = [result[1]]
        else:
            self.results[result[0]].append(result[1])

    def add_count(self, players):
        """
        Add game count.

        Get string with players and add number of players to list.
        """
        self.counter += 1
        self.number_of_players.append(len(players.split(",")))


if __name__ == "__main__":
    stat = Statistics("data.txt")
    print(stat.get("/game/terraforming mars/record-holder"))
