from typing import Any, ClassVar

from ..http import HTTPClient, Route, RiotRoute
from ..enums import (
    Region,
    Tier,
    Division,
    Queue
)
from ..models.lol import (
    Summoner,
    ChampionMastery,
    Rotation,
    League,
    Ranked,
    MiniSeries
)


class BaseEndpoint:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def _request(self, route: Route) -> Any:
        return await self._http.request(route)


class BaseLoLEndpoint(BaseEndpoint):
    async def _request(self, region: Region, path: str):
        if not isinstance(region, Region):
            raise TypeError(
                'Argument `region` must be {0.__name__} not {1.__name__}'.format(
                    Region, type(region)
                )
            )
        route = RiotRoute(path, region = region.value)
        return await super()._request(route)


class SummonerEndpoint(BaseLoLEndpoint):
    BASE: ClassVar[str] = '/lol/summoner/v4/summoners'

    def _create_summoner_from_data(self, data) -> Summoner:
        return Summoner(
            id = data['id'],
            account_id = data['accountId'],
            puuid = data['puuid'],
            name = data['name'],
            icon = data['profileIconId'],
            lvl = data['summonerLevel']
        )

    async def _request(self, region: Region, path: str) -> Summoner:
        data = await super()._request(region, path)
        return self._create_summoner_from_data(data)

    async def by_name(self, region: Region, name: str) -> Summoner:
        path = self.BASE + f'/by-name/{name}'
        return await self._request(region, path)

    async def by_id(self, region: Region, _id: str) -> Summoner:
        path = self.BASE + f'/{_id}'
        return await self._request(region, path)
    
    async def by_account_id(self, region: Region, account_id: str) -> Summoner:
        path = self.BASE + f'/by-account/{account_id}'
        return await self._request(region, path)

    async def by_puuid(self, region: Region, puuid: str) -> Summoner:
        path = self.BASE + f'/by-puuid/{puuid}'
        return await self._request(region, path)


class ChampionMasteryEndpoint(BaseLoLEndpoint):
    BASE: ClassVar[str] = '/lol/champion-mastery/v4/champion-masteries'

    def _create_mastery_from_data(self, data):
        return ChampionMastery(
            id = data['championId'],
            lvl = data['championLevel'],
            points = data['championPoints'],
            last_play = data['lastPlayTime'],
            points_since_last_lvl = data['championPointsSinceLastLevel'],
            points_until_next_lvl = data['championPointsUntilNextLevel'],
            chest = data['chestGranted'],
            tokens = data['tokensEarned']
        )

    async def _request(self, region: Region, path: str) -> Summoner:
        data = await super()._request(region, path)
        if isinstance(data, list):
            return [self._create_mastery_from_data(item) for item in data]
        return self._create_mastery_from_data(data)

    async def by_id(self, region: Region, _id: str, *, count: int = None, champion: int = None):
        path = self.BASE
        if count is not None:
            path += f'/by-summoner/{_id}/top?count={count}'
        elif champion is not None:
            path += f'/by-summoner/{_id}/by-champion/{champion}'
        else:
            path += f'/by-summoner/{_id}'

        return await self._request(region, path)

    async def scores(self, region: Region, _id: str):
        path = f'/lol/champion-mastery/v4/scores/by-summoner/{_id}'
        return await super().get(region, path)


class RotationEndpoint(BaseLoLEndpoint):
    BASE: ClassVar[str] = '/lol/platform/v3/champion-rotations'

    async def get(self, region: Region):
        data = await super()._request(region, self.BASE)
        return Rotation(
            champions = data['freeChampionIds'],
            champions_for_new = data['freeChampionIdsForNewPlayers'],
            max_new_player_lvl = data['maxNewPlayerLevel']
        )


class RankedEndpoints(BaseLoLEndpoint):
    BASE: ClassVar[str] = '/lol/league/v4'

    def _create_ranked_from_data(self, data) -> Ranked:
        return Ranked(
            summoner_id = data['summonerId'],
            summoner_name = data['summonerName'],
            id = data.get('leagueId'),
            queue = Queue(data['queueType']) if 'queueType' in data else None,
            tier = Tier(data['tier']) if 'tier' in data else None,
            rank = Division(data['rank']),
            lp = data['leaguePoints'],
            wins = data['wins'],
            losses = data['losses'],
            miniseries = MiniSeries(**data['miniSeries']) if 'miniSeries' in data else None,
            veteran = data['veteran'],
            inactive = data['inactive'],
            fresh_blood = data['freshBlood'],
            hot_streak = data['hotStreak']
        )

    def _create_league_from_data(self, data) -> League:
        return League(
            id = data['leagueId'],
            tier = Tier(data['tier']),
            queue = Queue(data['queue']),
            name = data['name'],
            summoners = [self._create_ranked_from_data(item) for item in data['entries']]
        )
    
    async def get(
        self,
        region: Region,
        *,
        queue: Queue,
        tier: Tier,
        division: Division,
        page: int = 1
    ) -> Ranked:
        path = f'/lol/league-exp/v4/entries/{queue.value}/{tier.value}/{division.name}?page={page}'
        data = await self._request(region, path)
        return [self._create_ranked_from_data(item) for item in data]

    async def by_summoner(self, region: Region, _id: str) -> Ranked:
        path = self.BASE + f'/entries/by-summoner/{_id}'
        data = await self._request(region, path)
        return [self._create_ranked_from_data(item) for item in data]

    async def by_league_id(self, region: Region, _id: str) -> League:
        path = self.BASE + f'/leagues/{_id}'
        data = await self._request(region, path)
        return self._create_league_from_data(data)

    async def get_challenger(self, region: Region, queue: Queue) -> League:
        path = self.BASE + f'/challengerleagues/by-queue/{queue.value}'
        data = await self._request(region, path)
        return self._create_league_from_data(data)

    async def get_grandmaster(self, region: Region, queue: Queue) -> League:
        path = self.BASE + f'/grandmasterleagues/by-queue/{queue.value}'
        data = await self._request(region, path)
        return self._create_league_from_data(data)

    async def get_master(self, region: Region, queue: Queue) -> League:
        path = self.BASE + f'/masterleagues/by-queue/{queue.value}'
        data = await self._request(region, path)
        return self._create_league_from_data(data)