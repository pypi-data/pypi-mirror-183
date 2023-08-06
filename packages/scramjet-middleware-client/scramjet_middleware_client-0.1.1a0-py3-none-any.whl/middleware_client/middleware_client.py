from urllib.parse import urlparse
from manager_client.manager_client import *
import aiohttp

class MiddlewareClient:
    def __init__(self, url: str, token=None):
        self.url = urlparse(url)
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}
        
    async def get(self, url: str) -> str:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = f'{self.url.geturl()}{url}'
            async with session.get(url) as resp:
                return await resp.text()
    
    async def post(self, url: str, headers: str = None, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = f'{self.url.geturl()}{url}'
            
            async with session.post(url, headers=headers, data=data, params=config) as resp:
                return await resp.text()
    
    async def get_manager_client(self, id: str, manager_api_base: str = "/api/v1"):
        return ManagerClient(self.url.geturl()+ '/space/' + id + manager_api_base)

    async def get_managers(self) -> str:
        url = f'/spaces'
        return await self.get(url)
    
    async def get_version(self) -> str:
        url = f'/version'
        return await self.get(url)
