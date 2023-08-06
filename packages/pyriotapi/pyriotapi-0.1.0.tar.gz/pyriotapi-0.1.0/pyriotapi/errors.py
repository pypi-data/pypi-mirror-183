from typing import Dict

from httpx import Response


#Base Exception
class HTTPExeption(Exception):
    def __init__(self, response: Response, data: Dict) -> None:
        self.response: Response = response
        self.text = data['status']['message']

        fmt = '[{0.status_code} {0.reason_phrase}] - {1}'

        super().__init__(fmt.format(self.response, self.text))

#400
class BadRequest(HTTPExeption):
    pass

#403
class Forbidden(HTTPExeption):
    pass

#404
class NotFound(HTTPExeption):
    pass