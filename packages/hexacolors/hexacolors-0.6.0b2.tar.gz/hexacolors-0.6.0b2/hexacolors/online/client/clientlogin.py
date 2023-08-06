import aiohttp

class ClientGet:

    def __init__(self, type: str, value: str) -> None:

        self.url = 'https://www.thecolorapi.com/id?{}={}'.format(type, value)
    
    async def request(self):

        async with aiohttp.ClientSession() as request:

            async with request.get(self.url) as response:

                res = await response.json(encoding='utf-8')
                return res['hex']['clean']
