from ..http import HTTPClient
from ..endpoints.lol import (
    SummonerEndpoint,
    ChampionMasteryEndpoint,
    RotationEndpoint,
    RankedEndpoints
)



class LoLApi:
    def __init__(self, token: str) -> None:
        self.http = HTTPClient(token = token)

        self._summoner = SummonerEndpoint(self.http)
        self._mastery = ChampionMasteryEndpoint(self.http)
        self._rotation = RotationEndpoint(self.http)
        self._ranked = RankedEndpoints(self.http)

    async def get_current_path(self) -> str:
        path = ''

    @property
    def summoner(self) -> SummonerEndpoint:
        return self._summoner
    
    @property
    def mastery(self) -> ChampionMasteryEndpoint:
        return self._mastery

    @property
    def rotation(self) -> RotationEndpoint:
        return self._rotation

    @property
    def ranked(self) -> RankedEndpoints:
        return self._ranked