import aiohttp
import asyncio
from fastapi import FastAPI



fastapi = FastAPI()


async def bus_data(route_number):
    async with aiohttp.ClientSession() as session:
        request_url = "http://45.135.131.226/api/buscoordinates/{0}".format(route_number)
        async with session.get(request_url) as resp:
            res_json = await resp.json()
            print(res_json)
            return res_json

#asyncio.run(bus_data(47))
@fastapi.get('/bus/{bus_route}')
async def bus_info(bus_route: int):
    bus_json = await bus_data(bus_route)
    for bus in bus_json:
        latitude = bus['latitude']
        longitude = bus['longitude']


{
    'H332': {
        'route': '47',
        'time': '2023-04-01 17:59:36',
        'latitude': 51.06113,
        'longitude': 71.4214,
        'angle': 174.9338313358419
    },
    'H364': {
        'route': '47',
        'time': '2023-04-01 17:59:30',
        'latitude': 51.09813,
        'longitude': 71.40907,
        'angle': 272.75910765853774
    }, 'H355': {
        'route': '47',
        'time': '2023-04-01 17:59:36',
        'latitude': 51.121254,
        'longitude': 71.4298553,
        'angle': 14.408479572230789
    }, 'H348': {
        'route': '47',
        'time': '2023-04-01 17:59:26',
        'latitude': 51.15179,
        'longitude': 71.51764,
        'angle': 231.78016131153223},
    'H311': {
        'route': '47',
        'time': '2023-04-01 17:59:35',
        'latitude': 51.1298141,
        'longitude': 71.45658,
        'angle': 239.33328994340468
    },
    'H366': {
        'route': '47',
        'time': '2023-04-01 17:54:49',
        'latitude': 51.0895767,
        'longitude': 71.40282,
        'angle': 20.922092809335044
    }
}