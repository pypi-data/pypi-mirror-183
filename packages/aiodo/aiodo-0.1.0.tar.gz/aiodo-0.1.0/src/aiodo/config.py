import logging.config
import pathlib


def load_toml(filename):
    import tomllib
    with open(filename, "rb") as f:
        return tomllib.load(f)


def load_python(filename):
    import runpy
    return runpy.run_path(filename)


Loaders = {
    ".toml": load_toml,
    ".py": load_python,
}

def configure(filename, log_level="INFO"):
    path = pathlib.Path(filename)
    config = Loaders[path.suffix](path)

    log_config = config.get("log")
    if log_config:
        logging.config.dictConfig(log_config)
    else:
        fmt = "%(asctime)s %(threadName)s %(levelname)s %(name)s %(message)s"
        logging.basicConfig(level=log_level.upper(), format=fmt)

    logging.debug("Preparing server %r...", config["name"])
    services = config["services"]
    if isinstance(services, dict):
        # ensure all services have a name
        for name, service in services.items():
            service.setdefault(name)
        config["services"] = services = list(services.values())
    for service in services:
        devices = service["devices"]
        if isinstance(devices, dict):
            # ensure all devices have a name
            for name, device in devices.items():
                device.setdefault(name)
            service["devices"] = list(devices.values())
    logging.debug("Finished loading configuration")
    return config


import logging.config
import os
import pathlib
import sys

import config


DEFAULT_CONFIG = {
    "logging": {
        "version": 1,
        "formatters": {
            "standard": {
                "format": "%(asctime)s %(threadName)s %(levelname)s %(name)s %(message)s",
            }
        },
        "handlers": {
            "default": {

                "class": "logging.StreamHandler",
                "formatter": "standard",
            }
        },
        "loggers": {
            "": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": True,
            }
        }
    }
}

def get_app_name(name=None):
    if name is None:
        name = os.getenv("DOLPHIN_APP") or pathlib.Path(sys.argv[0]).stem
    return name


def configure(filename, app_name=None):
    app_name = get_app_name(app_name)

    prefix = app_name.upper()

    cfg = config.config(DEFAULT_CONFIG, ('env', prefix), filename).as_attrdict()

    logging.config.dictConfig(cfg["logging"])

    services = cfg["services"]
    if isinstance(services, dict):
        # ensure all services have a name
        for name, service in services.items():
            service.setdefault(name)
        cfg["services"] = services = list(services.values())
    for service in services:
        devices = service["devices"]
        if isinstance(devices, dict):
            # ensure all devices have a name
            for name, device in devices.items():
                device.setdefault(name)
            service["devices"] = list(devices.values())
    return cfg