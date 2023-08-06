#!/usr/bin/env python3
import argparse
import asyncio
import random
import timeit

import codefast as cf
import requests
from colorama import Back, Fore, Style


class Hosts(object):
    peer = {}
    myredis = None

    @classmethod
    def sort_by_time(cls):
        return sorted(cls.peer.items(), key=lambda p: p[1])

    @classmethod
    def get_location(cls, ip: str) -> str:
        '''Returns the location of the ip address'''
        try:
            url = 'https://ipinfo.io/' + ip + '/json'
            resp = requests.get(url).json()
            ipinfo = '{}, {}'.format(resp['city'], resp['region'])
            return ipinfo
        except Exception as e:
            cf.warning(e)
        return 'location unknown'

    @classmethod
    def get_connection_duraion(cls, peer: str) -> int:
        '''Returns the connection duration of the peer'''
        return timeit.default_timer() - cls.peer[peer]


async def handler(_reader, writer):
    try:
        while True:
            peer = ':'.join(
                map(str, _reader._transport.get_extra_info('peername')))
            if peer not in Hosts.peer:
                Hosts.peer[peer] = timeit.default_timer()
                loc = Hosts.get_location(peer.split(':')[0])
                cf.info('connection from peer {}, {}'.format(
                    peer, Fore.LIGHTMAGENTA_EX + loc + Style.RESET_ALL))
            writer.write(b'%x\r\n' % random.randint(0, 2**32))
            if int(peer.split(':').pop()) < 10000 and random.randint(
                    0, 100) == 63:
                cf.info(
                    'MANUALLY close connection for peer {}'.format(peer))
                writer.close()
            await asyncio.sleep(3)
            await writer.drain()
    except Exception as e:
        cf.info(e)
        cf.info(
            'connection closed by peer {} after [ {:.1f} ] seconds '.format(
                peer,
                timeit.default_timer() - Hosts.peer[peer]))
        Hosts.peer.pop(peer)
        cf.info('peers connected: 【 {} 】🦧'.format(len(Hosts.peer)))
        if Hosts.peer:
            list_ = Hosts.sort_by_time()
            host_id, host_time = list_[0]
            time_diff = round(timeit.default_timer() - host_time, 1)
            cf.info('most patient peer: {}, {} seconds 🐢'.format(
                host_id, time_diff))


async def main(port):
    server = await asyncio.start_server(handler, '0.0.0.0', port)
    async with server:
        await server.serve_forever()


def endlessh():
    parser = argparse.ArgumentParser(description='Run a fake ssh server')
    parser.add_argument("--port",
                        "-p",
                        help="The port to bind the ssh server to (default 22)",
                        default=22,
                        type=int,
                        action="store")
    args = parser.parse_args()
    asyncio.run(main(args.port))
