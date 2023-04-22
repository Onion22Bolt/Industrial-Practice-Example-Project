from db import r, insert_coords, get_coords
import osmnx as ox
import matplotlib.pyplot as plt
import json
import time

hash_list = []


async def collect_coordinates(bus):
    bus_data = r.hget(bus, 'coordinates')
    bus_data_dict = json.loads(bus_data)
    latitude = bus_data_dict['latitude']
    longitude = bus_data_dict['longitude']
    timestamp = time.time()

    hashdata = hash(timestamp)
    hash_list.append(hashdata)
    await insert_coords(hashdata, longitude, latitude)


async def display_map():
    coordinates = []
    for hesh in hash_list:
        dict_data = await get_coords(hesh)
        coordinates.append(dict_data)
    print(coordinates)
    display_coordinates_on_map(coordinates)


def display_coordinates_on_map(coordinates, zoom=14):
    G = ox.graph_from_point((coordinates[0]['latitude'], coordinates[0]['longitude']), dist=10000, dist_type='bbox',
                            network_type='all')

    fig, ax = ox.plot_graph(G, bgcolor='white', edge_color='black', node_size=0, show=False, close=False)

    for coord in coordinates:
        ax.scatter(coord['longitude'], coord['latitude'], c='red', s=50, zorder=3)

    plt.savefig('map_with_coordinates{timestamp}.png'.format(timestamp=time.time()), dpi=300, bbox_inches='tight')

    plt.show()
