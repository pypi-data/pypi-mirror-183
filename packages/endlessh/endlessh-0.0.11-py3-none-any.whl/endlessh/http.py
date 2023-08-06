#!/usr/bin/env python3
import asyncio
import random

from codefast.logger import get_logger

logger = get_logger('/tmp/httptarpit.log')


async def handler(_reader, writer):
    writer.write(b'HTTP/1.1 200 OK\r\n')
    peername = _reader._transport.get_extra_info('peername')
    logger.info(f'connection from peer {peername}')
    try:
        while True:
            await asyncio.sleep(5)
            header = random.randint(0, 2**32)
            value = random.randint(0, 2**32)
            writer.write(b'X-%x: %x\r\n' % (header, value))
            await writer.drain()
    except ConnectionResetError:
        pass


async def main():
    server = await asyncio.start_server(handler, '0.0.0.0', 10101)
    async with server:
        await server.serve_forever()


def tarpit():
    asyncio.run(main())
