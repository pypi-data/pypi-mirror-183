import argparse
import asyncio
import contextlib
import logging
import socket
from typing import Sequence
import urllib.parse
from aiodo import registry

from connio import connection_for_url
from zeroconf.asyncio import AsyncZeroconf, AsyncServiceInfo

from .config import configure
from .network import get_ips



async def register_services(zeroconf: AsyncZeroconf, services: list[AsyncServiceInfo]):
    logging.info("Start registering services (%d)...", len(services))
    tasks = [zeroconf.async_register_service(service) for service in services]
    background_tasks = await asyncio.gather(*tasks)
    result = await asyncio.gather(*background_tasks)
    logging.info("Finished registering services")
    return result


@contextlib.asynccontextmanager
async def Zeroconf():  
    async with AsyncZeroconf() as zeroconf:
        try:
            yield zeroconf
        finally:
            logging.info("Unregistering services...")
            await zeroconf.async_remove_all_service_listeners()
            await zeroconf.async_unregister_all_services()
            logging.info("Finished unregistering services")


def parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", default=None)
    parser.add_argument("-c", "--config", required=True)
    return parser    


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    return parser().parse_args(args=args)


def service_info(config: dict[str]) -> AsyncServiceInfo:
    name = config["name"]
    logging.info("Preparing service %s...", name)
    serv_type = f"_{config['protocol']}._tcp.local."
    serv_name = f"_{name}.{serv_type}"
    serv_url_str = config["bind"]
    serv_url = urllib.parse.urlparse(serv_url_str)
    addrs = get_ips()
    hostname = serv_url.hostname
    if hostname in {"", "0", "0.0.0.0"}:
        addresses = addrs
    else:
        addresses = [socket.gethostbyname(hostname)]
    serv = AsyncServiceInfo(
        serv_type, serv_name,
        parsed_addresses=addresses,
        port=serv_url.port, properties=dict(devices=config["devices"])
    )
    return serv


class Device:

    def __init__(self, config):
        self.config = config
        self.device = None


class Service:

    def __init__(self, config):
        self.config = config
        self.service_info = service_info(config)


async def run(args=None):
    args = parse_args(args)
    config = configure(args.config, args.app)
    services = []
    all_devices = []
    for serv_config in config["services"]:
        device_configs = serv_config["devices"]
        for dev_config in device_configs:
            creator = registry.device(dev_config["type"]).load()
            device = creator(dev_config)
            all_devices.append(device)

        serv = service_info(serv_config)
        services.append(serv)
    
    async with Zeroconf() as server:
        await register_services(server, services)
        await asyncio.sleep(100)


def main():
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        logging.info("Ctrl-C Pressed. Bailing out")


if __name__ == "__main__":
    main()