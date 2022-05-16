# -*- coding=utf-8 -*-


# 获取socket连接
import asyncio
import json

import websockets

websocket = ''

def get_websocket():
    global websocket
    host = '127.0.0.1'
    port = '8999'
    websocket = websockets.connect("ws://127.0.0.1:8999")
    return websocket


async def send_msg(step, status):
    async with websockets.connect('ws://localhost:8999') as websocket:
        await websocket.send(step)
        await websocket.send(status)


if __name__ == '__main__':
    config = json.load(open('config.json', 'r', encoding='utf-8'))
    print(config.get("step"))
