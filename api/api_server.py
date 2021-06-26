import json

from aiohttp import web
from aiohttp.web_response import json_response

data = json.load(open("pokemon.json"))

async def handle(request):
    id = int(request.match_info.get('name'))

    return web.json_response(data[id]['name'])

app = web.Application()

app.add_routes([web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)