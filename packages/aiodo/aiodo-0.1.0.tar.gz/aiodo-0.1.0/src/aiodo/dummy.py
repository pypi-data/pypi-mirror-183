import asyncio
import random


class Dummy:

    def __init__(self, config):
        self.config = config

    async def pressure(self):
        result = random.random()
        await asyncio.sleep(result)
        return result * 1E-9


def get_device(config):
    return Dummy(config)