import aiohttp
import hashlib
import json
import uuid

import codefast as cf
import requests
from codefast.asyncio import async_render
from codefast.io.osdb import osdb
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from hashids import Hashids

from pyserverless.apps.rabbitmq import AMQPPublisher

cf.info("Pyserverless started ...")
cache = osdb('/tmp/cache.db')

app = FastAPI()


@app.get('/hello')
async def hello_world():
    return "hello world"


@app.get('/demo')
@app.post('/demo')
async def demo_():
    return "DEMO MESSAGE."


@app.post('/callback')
@app.get('/callback')
async def callback_():
    return {"code": 200, "msg": "SUCCESS", "uuid": str(uuid.uuid4())}


@app.post('/redis')
@app.get('/redis')
async def redis_(info: Request):
    info = await info.json()
    key = info.get('key')
    value = info.get('value')
    if value is None:
        return {"value": cache[key]}
    else:
        cache[key] = value
        return {"value": value, "key": key}


def pubmessage(que: str, msg: str, url:str=None):
    p = AMQPPublisher(que, url)
    p.publish(json.dumps(msg).encode('utf-8'))


@app.post('/amqp')
@app.get('/amqp')
async def post_amqp(info: Request):
    try:
        info = await info.json()
        queue_name = info['queue_name']
        message = info['message']
        url = info.get('url')
        resp = await async_render(pubmessage, queue_name, message, url)
        return {"result": "success", 'resp': str(resp)}
    except Exception as e:
        return {"result": "fail", "msg": str(e)}


@app.post('/shorten')
async def url_shorter(info: Request):
    req_info = await info.json()
    url = req_info.get('url')
    md5 = hashlib.md5(url.encode()).hexdigest()
    uniq_id = Hashids(salt=md5, min_length=6).encode(42)
    cf.info('uniq_id: ' + uniq_id)
    cache[uniq_id] = url
    cf.info('uniq id inserted')
    return {'code': 200, 'status': 'SUCCESS', 'url': 's/' + uniq_id}


@app.post('/bark')
async def bark_(info: Request):
    info = await info.json()
    token = info['token']
    title = info['title']
    message = info['message']
    icon = info.get('icon')

    from pyserverless.auth import auth
    if token != auth.api_token:
        return {'code': 500, 'message': 'token error'}

    url = f"{auth.local_bark}/{title}/{message}"
    if icon:
        url = f"{url}?icon={icon}"
    return requests.post(url).json()


@app.post('/humidifier/{action}')
async def humidifier(action:str):
    db_url = 'https://cf.ddot.cc/api/redis'
    async with aiohttp.ClientSession() as session:
        async with session.post(db_url, json={
            'key': 'humidifier',
            'value': action
        }) as resp:
            _ = await resp.json()

        return {'action': action}
