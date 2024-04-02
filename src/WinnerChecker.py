

class WinnerChecker:

    def check(self, board):
        regions = [*board.get_lines(), *board.get_columns(), *board.get_diagonals()]

        for region in regions:
            if len(set([position.get_value() for position in region])) == 1 and region[0].get_value():
                board.set_value(region[0].get_value())
                print(f"Player {board.get_value()} won")
                return region[0].get_value()

        return None