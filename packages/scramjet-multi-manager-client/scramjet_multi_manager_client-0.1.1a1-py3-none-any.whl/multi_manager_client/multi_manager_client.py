from urllib.parse import urlparse
from manager_client.manager_client import ManagerClient
import aiohttp
import json

class MultiManagerClient:
    def __init__(self, url: str, token=None, config=None):
        self.url = urlparse(url)
        self.token = token
        self.config = config
        self.headers = {'Authorization': f'Bearer {self.token}'}
    
    async def get(self, url: str) -> str:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = f'{self.url.geturl()}{url}'
            async with session.get(url) as resp:
                return await resp.text()
    
    async def post(self, url: str, headers: str = None, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = f'{self.url.geturl()}{url}'
            async with session.post(url, headers=headers, json=data, params=config) as resp:
                return await resp.text()
    
    async def get_manager_client(self, id: str, manager_api_base: str = '/api/v1'):
        return ManagerClient(self.url.geturl()+ '/space/' + id + manager_api_base, self.token)

    async def start_manager(self, config: dict, manager_api_base : str = '/api/v1'):
        resp = await self.post(
            url='/start',
            headers={'content-type': 'application/json', **self.headers},
            data=config
        )
        json_data = json.loads(resp)
        if 'error' in json_data:
            raise Exception(json_data.get('error'))
        return ManagerClient(self.url.geturl() + "/space/" + json_data.get('id') + manager_api_base)

    async def get_managers(self) -> str:
        url = f'/list'
        return await self.get(url)
    
    async def get_version(self) -> str:
        url = f'/version'
        return await self.get(url)
    
    async def get_load(self) -> str:
        url = f'/load'
        return await self.get(url)
    
    async def get_log_stream(self) -> str:
        url = f'/log'
        return await self.get(url)
    
    async def get_info(self) -> str:
        url = f'/info'
        return await self.get(url)
