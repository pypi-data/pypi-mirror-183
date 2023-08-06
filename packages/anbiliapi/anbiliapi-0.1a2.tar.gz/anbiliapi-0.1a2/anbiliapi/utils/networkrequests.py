from httpx import AsyncClient

from .credential import Credential


async def requests(url: str,
                   method: str = "GET",
                   cookies: dict = None,
                   data: dict = None,
                   files=None,
                   json: dict = None
                   ):
    cookies = {} if cookies is None else cookies
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}
    client = AsyncClient(timeout=60, headers=headers)
    try:
        if method == "GET":
            req = client.get(url, params=data, cookies=cookies)
        else:
            req = client.post(url, data=data, cookies=cookies, files=files, json=json)

        res = await req
    finally:
        await client.aclose()
    return res


class Requests:

    def __init__(self, credential: Credential):
        self.__credential = credential

    async def requests(self,
                       url: str,
                       method: str = "GET",
                       cookies: dict = None,
                       data: dict = None,
                       files=None,
                       json: dict = None
                       ):
        cookies = {} if cookies is None else cookies
        cookies.update(self.__credential.dict())
        return await requests(url=url,
                              method=method,
                              cookies=cookies,
                              data=data,
                              files=files,
                              json=json)
