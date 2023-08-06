import sys
from typing import Any, ClassVar

import httpx

from . import __version__
from .errors import (
    HTTPExeption,
    BadRequest,
    Forbidden,
    NotFound
)


class Route:
    def __init__(self, path, **params: Any):        
        url = self.BASE + path
        if params:
            url = url.format_map(params)
        self.url = url

class RiotRoute(Route):
    BASE: ClassVar[str] = 'https://{region}.api.riotgames.com'

class DDragonRoute(Route):
    BASE: ClassVar[str] = 'https://ddragon.leagueoflegends.com'


class HTTPClient:
    def __init__(self, token: str = None) -> None:
        self.__token = token
        self.__session: httpx.AsyncClient = httpx.AsyncClient()

        user_agent = 'PyRiotApiBot {0} Python/{1[0]}.{1[1]} httpx/{2}'
        self.user_agent = user_agent.format(__version__, sys.version_info, httpx.__version__)

    async def request(self, route: Route) -> Any:
        url = route.url

        headers = {
            'User-Agent': self.user_agent
        }

        if self.__token is not None:
            headers['X-Riot-Token'] = self.__token

        response = await self.__session.get(url, headers = headers)
        data = response.json()

        if response.status_code == 200:
            return data
        elif response.status_code == 400:
            raise BadRequest(response, data)
        elif response.status_code == 403:
            raise Forbidden(response, data)
        elif response.status_code == 404:
            raise NotFound(response, data)
        else:
            raise HTTPExeption(response, data)