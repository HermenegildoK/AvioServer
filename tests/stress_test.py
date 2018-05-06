# -*- coding: utf-8 -*-
import sys
import asks
import trio
from datetime import datetime

asks.init('trio')


async def worker(s, worker_num):
    r = await s.get(path=f'/{worker_num}')
    print(worker_num)
    print(r.text)


async def main(max_multiplier):
    """very dummy stress test"""
    max_concurrent_conections = 16
    s = asks.Session(connections=max_concurrent_conections)
    s.base_location = 'http://127.0.0.1:8000'
    s.endpoint = '/test/connections'
    async with trio.open_nursery() as nursery:
        for i in range(
                1,
                max_concurrent_conections*int(max_multiplier)+1
        ):
            nursery.start_soon(worker, s, i)


def run_stress_test(max_multiplier):
    start_time = datetime.utcnow()
    trio.run(main, max_multiplier)
    print(datetime.utcnow() - start_time)


if __name__ == "__main__":
    run_stress_test(sys.argv[1])
