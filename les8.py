import requests
import asyncio
import random


class SomeError(Exception):
    def __init__(self, text=None):
        self.text = text


class Product:
    id = ''
    name = ''

    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Parser:
    __headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0",
    }
    __params = {
        'records_per_page': 50,
        'categories': '',
    }

    def __init__(self, stat_url: str):
        self.__start_url = stat_url
        self.products = []

    def parse(self):
        url = self.__start_url
        while url:
            response = requests.get(url, params=self.__params, headers=self.__headers)
            data = response.json()
            url = None
            self.products.extend(Product(itm) for itm in data['results'])


async def one(n):
    for num in range(n):
        await asyncio.sleep(random.randint(1, 15))
        print(num, 'one', n)
        await asyncio.sleep(random.randint(1, 15))


if __name__ == '__main__':
    tasks = asyncio.wait([one(n) for n in range(1, 5)])
    asyncio.run(tasks)
    print(1)
