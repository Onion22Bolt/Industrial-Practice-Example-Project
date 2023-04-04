import aiohttp
import asyncio
import json
from fastapi import FastAPI
from db import r
from map import collect_coordinates, display_map

fastapi = FastAPI()


async def bus_data(route_number):
    async with aiohttp.ClientSession() as session:
        request_url = "http://45.135.131.226/api/buscoordinates/{0}".format(route_number)
        async with session.get(request_url) as resp:
            res_json = await resp.json()
        return res_json


@fastapi.get('/bus/{bus_route}')
async def bus_info(bus_route: int):
    bus_json = await bus_data(bus_route)
    for bus in bus_json:
        latitude = bus_json[bus]['latitude']
        longitude = bus_json[bus]['longitude']
        coordinates = {'latitude': latitude, 'longitude': longitude}
        r.hset(bus, 'coordinates', json.dumps(coordinates))
        await collect_coordinates(bus)

@fastapi.get('/map')
async def show_map():
    await display_map()