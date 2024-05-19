"""
TODO:
    - Implement ignoring mechanical DNFs because they're not the driver's fault
"""

import trueskill as ts


class DriverStats:
    def __init__(self, _id: int, full_name: str) -> None:
        # Driver data
        self.id = _id
        self.full_name = full_name

        # Driver career data
        self.n_races: int = 0

        # Driver ELO
        self.elo = ts.Rating()

    def add_race(self) -> None:
        self.n_races += 1
