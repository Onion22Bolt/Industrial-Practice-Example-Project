from redis import Redis
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
r = Redis()
client = AsyncIOMotorClient()
industrialdb = client['industrialdb']
mycol = industrialdb['mycol']


async def insert_coords(hashdata, longitude, latitude):
    doc = {'hashdata': hashdata, 'longitude': longitude, 'latitude': latitude}
    mycol.insert_one(doc)

async def get_coords(hashdata):
    data = await mycol.find_one({'hashdata': hashdata})
    dict_data = {'latitude': data['latitude'], 'longitude': data['longitude']}
    return dict_data





#     print(type(data))
#     print(data)
# asyncio.run(get_coords(870265134006407))