from dataclasses import dataclass

from ..enums import Queue, Tier, Division


@dataclass
class Summoner:
    id: str
    account_id: str
    puuid: str
    name: str
    icon: int
    lvl: int

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return '<{0.__class__.__name__} {0.name}>'.format(self)

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id
        return NotImplemented
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


@dataclass
class ChampionMastery:
    id: int                     # Champion ID for this entry
    lvl: int                    # Champion level for specified player and champion combination
    points: int                 # Total number of champion points for this player and champion combination - they are used to determine championLevel
    last_play: int              # Last time this champion was played by this player - in Unix milliseconds time format
    points_since_last_lvl: int  # Number of points earned since current level has been achieved
    points_until_next_lvl: int  # Number of points needed to achieve next level. Zero if player reached maximum champion level for this champion
    chest: bool                 # Is chest granted for this champion or not in current season
    tokens: int                 # The token earned for this champion at the current championLevel. When the championLevel is advanced the tokensEarned resets to 0

    def __str__(self) -> str:
        return 'Champion {0.id} | {0.points} points'.format(self)

    def __repr__(self) -> str:
        return '<{0.__class__.__name__} id={0.id}, points={0.points}>'.format(self)


@dataclass
class Rotation:
    champions: list[int]
    champions_for_new: list[int]
    max_new_player_lvl: int

    def __repr__(self) -> str:
        return '<{0.__class__.__name__}: {0.champions}>'.format(self)


@dataclass
class MiniSeries:
    target: int
    wins: int
    losses: int
    progress: str


@dataclass
class Ranked:
    summoner_id: str
    summoner_name: str
    id: str
    queue: Queue
    tier: Tier
    rank: Division
    lp: int
    wins: int
    losses: int
    miniseries: MiniSeries
    veteran: bool
    inactive: bool
    fresh_blood: bool
    hot_streak: bool

    def __str__(self):
        if self.tier is None:
            return '{0.summoner_name} {0.lp}LP'.format(self)
        return '{0.tier.name} {0.rank.name}'.format(self)

    def __repr__(self):
        if self.tier is None:
            return '<{0.__class__.__name__} summoner={0.summoner_name} lp={0.lp}>'.format(self)
        return (
            '<{0.__class__.__name__} summoner={0.summoner_name}, queue={0.queue.name}, '
            'tier={0.tier.name}, rank={0.rank.name}, lp={0.lp}LP>'
        ).format(self)


@dataclass
class League:
    id: str
    tier: Tier
    queue: Queue
    name: str
    summoners: list[Ranked]

    def __str__(self):
        return '{0.tier.name} {0.name}'.format(self)

    def __repr__(self):
        return '<{0.__class__.__name__} tier={0.tier.name} name={0.name}>'.format(self)